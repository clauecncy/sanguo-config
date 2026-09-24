"""Journaled multi-file publishing with optimistic checks and retained rollback data."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import uuid
from contextlib import contextmanager
from datetime import datetime
from project_data import atomic_json, read_json


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def safe_target(root, relative):
    if Path(relative).is_absolute() or '..' in Path(relative).parts:
        raise ValueError('Target must be a relative path without parent traversal')
    root = root.resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or path == root:
        raise ValueError('Target must stay inside project')
    parts = path.relative_to(root).parts
    if parts[0] in ('.git', '.agents', '.codex') or path.name == 'inventory.json':
        raise ValueError('Material transaction cannot modify private metadata or inventory')
    return path


@contextmanager
def material_lock(root):
    lock = root / '.materials.lock'
    stream = open(lock, 'a+b')
    acquired = False
    try:
        if stream.seek(0, os.SEEK_END) == 0:
            stream.write(b'0')
            stream.flush()
        stream.seek(0)
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        acquired = True
        yield
    finally:
        if acquired:
            stream.seek(0)
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
        stream.close()
        # Keep the lock inode: removing it can allow a second concurrent writer.


def rollback(root, directory, *, dry_run=False):
    directory = directory.resolve()
    if not directory.is_relative_to((root / 'notes/backups').resolve()):
        raise ValueError('Recovery journal must be a project backup')
    journal = read_json(directory / 'transaction.json')
    if journal['status'] == 'rolled_back':
        return
    # Check every target before restoring any, so later user edits are never clobbered.
    for row in journal['files']:
        target = safe_target(root, row['path'])
        current = digest(target.read_bytes()) if target.exists() else None
        if current not in (row['before'], row['after']):
            raise ValueError('Recovery conflicts with later edit: ' + row['path'])
        old = directory / 'before' / row['path']
        if row['before'] is not None and (not old.is_file() or digest(old.read_bytes()) != row['before']):
            raise ValueError('Invalid recovery backup: ' + row['path'])
    if dry_run:
        return
    for row in reversed(journal['files']):
        target = safe_target(root, row['path'])
        if row['before'] is None:
            if target.exists():
                retained = directory / 'rolled-back-new' / row['path']
                retained.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target), str(retained))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(directory / 'before' / row['path'], target)
    journal['status'] = 'rolled_back'
    atomic_json(directory / 'transaction.json', journal)


def publish(root, changes, *, expected=None, check=None):
    """Call under material_lock; staged bytes and backups are kept for recovery."""
    root = Path(root).resolve()
    for p in (root / 'notes/backups').glob('*/transaction.json'):
        if read_json(p)['status'] == 'publishing':
            raise ValueError('Recover interrupted material transaction first: ' + str(p.parent))
    rows = []
    for relative, data in changes.items():
        if not isinstance(data, bytes):
            raise TypeError('Publish accepts bytes only')
        target = safe_target(root, relative)
        before = digest(target.read_bytes()) if target.exists() else None
        if expected is not None and relative in expected and before != expected[relative]:
            raise ValueError('Concurrent edit: ' + relative)
        if before != digest(data):
            rows.append(dict(path=relative, before=before, after=digest(data)))
    if not rows:
        if check:
            check()
        return None
    directory = root / 'notes/backups' / (datetime.now().strftime('%Y-%m-%d-%H%M%S') + '-materials-' + uuid.uuid4().hex[:8])
    for row in rows:
        target = safe_target(root, row['path'])
        if row['before'] is not None:
            old = directory / 'before' / row['path']
            old.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, old)
        stage = directory / 'staged' / row['path']
        stage.parent.mkdir(parents=True, exist_ok=True)
        stage.write_bytes(changes[row['path']])
    journal = dict(status='publishing', files=rows)
    atomic_json(directory / 'transaction.json', journal)
    try:
        for row in rows:
            target = safe_target(root, row['path'])
            current = digest(target.read_bytes()) if target.exists() else None
            if current != row['before']:
                raise ValueError('Concurrent edit: ' + row['path'])
            target.parent.mkdir(parents=True, exist_ok=True)
            temp = target.with_name(target.name + '.' + uuid.uuid4().hex + '.tmp')
            try:
                shutil.copy2(directory / 'staged' / row['path'], temp)
                os.replace(temp, target)
            finally:
                if temp.exists():
                    temp.unlink()
        if check:
            check()
        journal['status'] = 'committed'
        atomic_json(directory / 'transaction.json', journal)
    except BaseException:
        rollback(root, directory)
        raise
    return directory
