"""Keep one successful screenshot batch; never touch event or public evidence."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import time
import uuid

IMAGE_SUFFIXES = {'.png','.jpg','.jpeg','.webp','.bmp','.tif','.tiff','.heic'}

def retry_windows(operation):
    # Antivirus/indexers may briefly hold a newly closed image or directory.
    for attempt in range(6):
        try:
            return operation()
        except PermissionError as exc:
            if getattr(exc,'winerror',None) not in (5,32,33) or attempt==5: raise
            time.sleep(0.05*(attempt+1))

def replace_directory(source, target):
    retry_windows(lambda: os.replace(source,target))

def checked_path(path, boundary):
    path, boundary = Path(path), Path(boundary).resolve()
    resolved = path.resolve()
    if resolved == boundary or not resolved.is_relative_to(boundary):
        raise ValueError(f'Cleanup target outside permitted directory: {path}')
    for part in [path, *path.parents]:
        if part.resolve() == boundary: break
        if part.exists() and (part.is_symlink() or getattr(part.lstat(),'st_file_attributes',0) & stat.FILE_ATTRIBUTE_REPARSE_POINT):
            raise ValueError(f'Refusing linked cleanup path: {part}')
    return resolved

def remove_owned(path, boundary):
    """Verify the absolute target and all children before recursive deletion."""
    path = checked_path(path,boundary)
    if not path.exists(): return
    if path.is_dir():
        for child in path.rglob('*'): checked_path(child,boundary)
        retry_windows(lambda: shutil.rmtree(path))
    else:
        retry_windows(path.unlink)

class EvidenceBatch:
    def __init__(self, user_base, images):
        self.base = Path(user_base) / 'evidence'
        if self.base.resolve() != Path(user_base).resolve() / 'evidence':
            raise ValueError('Evidence directory must not redirect outside the account')
        self.current = self.base / 'current'
        token = uuid.uuid4().hex
        self.stage = self.base / ('.pending-'+token)
        self.previous = self.base / ('.previous-'+token)
        self.published = False
        self.had_previous = False
        sources = [Path(p).resolve() for p in images]
        if not sources: raise ValueError('An image batch must contain at least one image')
        for source in sources:
            if source.suffix.lower() not in IMAGE_SUFFIXES or not source.is_file() or not source.stat().st_size:
                raise ValueError(f'Invalid or empty screenshot: {source}')
        # Validate the existing tree before changing anything.
        checked_path(self.current,self.base)
        if self.current.exists():
            for child in self.current.rglob('*'): checked_path(child,self.base)
        self.stage.mkdir(parents=True)
        try:
            records = {}
            for source in sources:
                raw = source.read_bytes()
                sha = hashlib.sha256(raw).hexdigest()
                name = sha + source.suffix.lower()
                (self.stage / name).write_bytes(raw)
                records[name] = {'file':name,'sha256':sha,'bytes':len(raw)}
            (self.stage / 'manifest.json').write_text(json.dumps({'files':list(records.values())},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        except BaseException:
            remove_owned(self.stage,self.base)
            raise

    def publish(self):
        if self.current.exists():
            replace_directory(self.current,self.previous)
            self.had_previous = True
        replace_directory(self.stage,self.current)
        self.published = True

    def rollback(self):
        if self.published: remove_owned(self.current,self.base)
        if self.had_previous and self.previous.exists(): replace_directory(self.previous,self.current)
        if self.stage.exists(): remove_owned(self.stage,self.base)

    def commit(self):
        # Called only after the new inventory has been read back and validated.
        if self.previous.exists(): remove_owned(self.previous,self.base)

def cleanup_incoming(user_base, paths):
    """Delete only explicit successful inputs in this user's incoming directory."""
    boundary = Path(user_base) / 'evidence' / 'incoming'
    removed=[]
    for raw in paths:
        path=Path(raw)
        if path.resolve().is_relative_to(boundary.resolve()) and path.is_file():
            remove_owned(path,boundary)
            removed.append(str(path))
    return removed
