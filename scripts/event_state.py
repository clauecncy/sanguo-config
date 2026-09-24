"""Authoritative event state and generated compatibility projections."""
import copy
from material_transaction import json_bytes
from project_data import read_json


def validate_state(state, user, event):
    if state.get('user_id') != user or state.get('event_id') != event:
        raise ValueError('State ownership mismatch')
    pool = state['warehouse']
    support = pool['support']
    for group, limit in [('generals', 1), ('tactics', 2)]:
        names = [r['name'] for r in pool[group]]
        extra = [r['name'] for r in support[group]]
        if len(set(names + extra)) != len(names + extra):
            raise ValueError('Duplicate native/support identity')
        # A separately confirmed purple-slot pouch can raise this limit.
        limit += int(group == 'tactics' and state.get('extra_purple_support_confirmed') is True)
        if len(extra) > limit:
            raise ValueError('Support capacity exceeded')
    generals = {r['name'] for r in pool['generals'] + support['generals']}
    tactics = {r['name'] for r in pool['tactics'] + support['tactics']}
    seen_g, seen_t, seen_teams = set(), set(), set()
    for team in state['lineup']['teams']:
        if team['team'] in seen_teams or len(team['members']) > 3:
            raise ValueError('Invalid team')
        seen_teams.add(team['team'])
        for member in team['members']:
            if member['name'] not in generals or member['name'] in seen_g:
                raise ValueError('Unavailable/duplicate general: ' + member['name'])
            seen_g.add(member['name'])
            if len(member['tactics']) > 2:
                raise ValueError('Too many learned tactics')
            for name in member['tactics']:
                if name not in tactics or name in seen_t:
                    raise ValueError('Unavailable/duplicate tactic: ' + name)
                seen_t.add(name)
    if not state.get('source') or not state.get('verified_at'):
        raise ValueError('State requires source and verification date')


def projections(prefix, state):
    warehouse = copy.deepcopy(state['warehouse'])
    warehouse.update(user_id=state['user_id'], event_id=state['event_id'], generated_from='current_state.json')
    lines = ['# 当前演武状态', '', '自动生成，唯一编辑源：current_state.json。历史建议不代表当前配置。', '',
             state['stage'], '', '锁定状态：' + str(state['locked']), '']
    for team in state['lineup']['teams']:
        lines.append('## 部队 ' + str(team['team']) + ' / ' + team['formation'])
        for member in team['members']:
            lines.append('- ' + member['name'] + '：' + '、'.join(member['tactics']))
        lines.append('')
    lines += ['支援及可信边界：', '', state['warehouse']['support'].get('status', ''), '',
              '未确认锁定不等于未装备；清风支援来源推定与装备截图确认分开。', '']
    return {prefix + '/当前仓库.json': json_bytes(warehouse),
            prefix + '/当前状态.md': '\n'.join(lines).encode('utf-8')}


def read_current(path):
    target = path / 'current_state.json'
    return read_json(target) if target.exists() else None
