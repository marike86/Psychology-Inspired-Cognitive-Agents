#!/usr/bin/env python3
"""Validate the merged package AND a global installation (skill + agents).

Usage:
    python tests/validate_install.py

Checks frontmatter, name/directory agreement, reference-module integrity,
description format rules, and byte-identical package-vs-installed copies.
"""
from pathlib import Path
import hashlib
import os
import re
import sys

PKG = Path(__file__).resolve().parents[1]
HOME = Path(os.path.expanduser('~'))
GLOBAL_SKILL = HOME / '.trae-cn' / 'skills' / 'psychological-research-collective'
GLOBAL_AGENTS = HOME / '.trae-cn' / 'agents'

errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


# ---- package skill ----
skill_dir = PKG / '.trae' / 'skills' / 'psychological-research-collective'
skill_md = skill_dir / 'SKILL.md'
check(skill_md.exists(), 'package SKILL.md missing')
raw = skill_md.read_text(encoding='utf-8')
m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
check(m is not None, 'package SKILL.md has no parseable frontmatter')
if m:
    fm_text, body = m.group(1), m.group(2)
    check('name: psychological-research-collective' in fm_text, 'frontmatter name mismatch')
    desc_line = next((l for l in fm_text.splitlines() if l.startswith('description:')), '')
    check(bool(desc_line), 'frontmatter missing description')
    d = desc_line[len('description:'):].strip()
    check(not d.startswith(('"', "'")), 'description must be an unquoted plain scalar')
    check(': ' not in d, "description must not contain ': '")
    check('<' not in d and '>' not in d, "description must not contain '<' or '>'")
    check('TODO' not in d, 'description must not contain TODO')
    check(len(d) <= 250, f'description too long ({len(d)})')
    check(len(body.splitlines()) < 500, 'SKILL.md body must stay under 500 lines')

# ---- reference modules ----
refs = sorted((skill_dir / 'references').glob('*.md'))
check(len(refs) == 11, f'expected 11 reference modules, found {len(refs)}')
for r in refs:
    check(r.stat().st_size > 0, f'empty reference module: {r.name}')
    check(r.read_text(encoding='utf-8').lstrip().startswith('#'),
          f'reference module lacks a heading: {r.name}')

referenced = set(re.findall(r'references/([a-z0-9-]+\.md)', raw))
on_disk = {r.name for r in refs}
check(referenced <= on_disk, f'SKILL.md references missing modules: {sorted(referenced - on_disk)}')
check(on_disk <= referenced, f'orphan reference modules never referenced: {sorted(on_disk - referenced)}')

# ---- agents ----
pkg_agents = sorted((PKG / '.trae' / 'agents').glob('*.md'))
check(len(pkg_agents) == 8, f'expected 8 agents, found {len(pkg_agents)}')
for a in pkg_agents:
    t = a.read_text(encoding='utf-8')
    check(re.match(r'^---\n.*?\n---\n', t, re.S) is not None, f'agent missing frontmatter: {a.name}')
    check(re.search(r'^name:\s*' + re.escape(a.stem) + r'\s*$', t, re.M) is not None,
          f'agent name != filename: {a.name}')
    check('psychological-research-collective' in t,
          f'agent not repointed to merged skill: {a.name}')

# ---- AGENTS.md ----
ag = PKG / 'AGENTS.md'
check(ag.exists() and ag.stat().st_size < 32 * 1024, 'AGENTS.md missing or over 32KB')
check('psychological-research-collective' in ag.read_text(encoding='utf-8'),
      'AGENTS.md does not point at the merged skill')

# ---- global install parity (optional: skipped when not installed) ----
if GLOBAL_SKILL.is_dir():
    check(sha(GLOBAL_SKILL / 'SKILL.md') == sha(skill_md), 'global SKILL.md differs from package')
    for r in refs:
        gp = GLOBAL_SKILL / 'references' / r.name
        check(gp.exists() and sha(gp) == sha(r), f'global reference mismatch: {r.name}')
    g_agents = sorted(GLOBAL_AGENTS.glob('*.md')) if GLOBAL_AGENTS.is_dir() else []
    check(len(g_agents) == 8, f'expected 8 global agents, found {len(g_agents)}')
    for a in pkg_agents:
        gp = GLOBAL_AGENTS / a.name
        check(gp.exists() and sha(gp) == sha(a), f'global agent mismatch: {a.name}')
    scope = 'package + global install'
else:
    scope = 'package only (global install not detected)'

if errors:
    print('FAIL')
    for e in errors:
        print('  -', e)
    sys.exit(1)
print(f'PASS: {scope}')
print(f'  skill   : {skill_md}')
print(f'  modules : {len(refs)}')
print(f'  agents  : {len(pkg_agents)}')
