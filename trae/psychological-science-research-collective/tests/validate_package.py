#!/usr/bin/env python3
"""Local static validation; does not test the TRAE runtime."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
AGENTS = list((ROOT / '.trae/agents').glob('*.md'))
SKILLS = list((ROOT / '.trae/skills').glob('*/SKILL.md'))
REFS = list((ROOT / '.trae/skills/psychological-research-collective/references').glob('*.md'))

assert len(AGENTS) == 8, f'Expected 8 Subagents; found {len(AGENTS)}'
assert len(SKILLS) == 1, f'Expected 1 Skill; found {len(SKILLS)}'
assert len(REFS) == 11, f'Expected 11 reference modules; found {len(REFS)}'
assert (ROOT / 'AGENTS.md').exists()
assert (ROOT / 'AGENTS.md').stat().st_size < 32 * 1024

skill = SKILLS[0]
assert skill.parent.name == 'psychological-research-collective'

for f in AGENTS + SKILLS:
    s = f.read_text(encoding='utf-8-sig')
    assert s.startswith('---\n') and '\n---\n' in s[4:], f'Missing YAML frontmatter: {f}'
    fm = s.split('---', 2)[1]
    assert re.search(r'^name:', fm, re.M) and re.search(r'^description:', fm, re.M), f'Missing metadata: {f}'
    if f in AGENTS:
        assert re.fullmatch(r'[a-z][a-z0-9-]{0,48}[a-z0-9]', f.stem)

try:
    import yaml
except ImportError:
    print('PyYAML not installed: delimiter/required field checks passed; YAML parsing not checked')
else:
    for f in AGENTS + SKILLS:
        raw = f.read_text('utf-8')
        obj = yaml.safe_load(raw.split('---', 2)[1])
        assert isinstance(obj, dict) and obj.get('name') and obj.get('description')
        expected = f.stem if f in AGENTS else f.parent.name
        assert obj['name'] == expected, f'name mismatch in {f}: {obj["name"]} != {expected}'

# every reference module named in SKILL.md must exist on disk
body = skill.read_text('utf-8')
for ref in sorted({m for m in re.findall(r'references/([a-z0-9-]+\.md)', body)}):
    assert (skill.parent / 'references' / ref).exists(), f'Missing referenced module: {ref}'
assert len(body.splitlines()) < 500, 'SKILL.md should stay well under 500 lines'

print('PASS: 8 Subagents, 1 Skill, 11 reference modules, frontmatter, naming, '
      'reference integrity, AGENTS.md length (static only)')
