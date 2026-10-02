"""Expand a manually reviewed checkpoint into a public import payload (no OCR)."""
import argparse
import json
from pathlib import Path
from project_data import ROOT, read_json


def prepare(review):
    rows = []
    for row in review['reviewed']:
        red = row['advancement']
        rows.append(dict(row, image=review['source_directory'] + '/' + row['name'] + '-10级.png',
            observed_at='2026-09-12', platform='Steam', season='s2', level=10, scope='unspecified',
            reviewed=True, verified_fields=['effect_raw','level','activation_rate','advancement_confirmed'],
            trust_reason='2026-09-25逐图核验完整10级正文或满级预览右侧值；' +
                ('红度未展示，按用户2026-09-24/25明确约定记白板0。' if red == 0 else '截图展示红度' + str(red) + '。') +
                '仅公共详情，不代表账号拥有；不外推其他红度，不记录低级成长系数。'))
    if len({r['name'] for r in rows}) != len(rows):
        raise ValueError('Duplicate reviewed name')
    return dict(observations=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--status', action='store_true', help='Print counts and at most four remaining images without loading images')
    args = parser.parse_args()
    review = read_json(args.input)
    if args.status:
        images = sorted((ROOT / review['source_directory']).glob('*-10级.png'))
        reviewed = {row['name'] for row in review['reviewed']}
        pending = {row['name'] for row in review.get('needs_confirmation', [])}
        remaining = [p for p in images if p.stem.removesuffix('-10级') not in reviewed | pending]
        print(json.dumps(dict(total=len(images), reviewed=len(reviewed),
            needs_confirmation=sorted(pending), remaining=len(remaining),
            next_batch=[p.relative_to(ROOT).as_posix() for p in remaining[:4]]), ensure_ascii=False, indent=2))
    else:
        if args.output is None:
            parser.error('--output is required unless --status is used')
        payload = prepare(review)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('Prepared reviewed observations:', len(payload['observations']))
