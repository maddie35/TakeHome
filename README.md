# Phase 3 prototype: article-structure checker

Automated check for the Phase 1 problem "article structure is inconsistent"
(and its title/heading corollaries), run against the live Connectors /
Skills / Plugins slice of claude.com/docs, evaluated against the Phase 2
style guide + Context article template (`standard.py`).

## What it does

1. `fetch.py` pulls every page in the slice (`corpus.py`, sourced from
   `claude.com/docs/llms.txt`) as raw markdown via Mintlify's `.md` suffix,
   and caches it in `raw/`.
2. `evaluate.py` sends each cached page to Claude with the standard as a
   rubric and asks it to return a structured evaluation: page type
   (context / task / other), a flagged bool, and a list of specific rule
   violations with the offending text quoted. Results go to
   `results.json`, and flagged pages print to the console.

## Setup

```bash
pip install -r requirements.txt
```

Set your API key (get one at console.anthropic.com -> API Keys):

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

PowerShell:

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

## Run

```bash
python fetch.py
python evaluate.py
```

`fetch.py` needs no API key. `evaluate.py` does.

## Scope and known limitations

- The corpus is the Connectors/Skills/Plugins slice only (~37 pages), not
  the whole docs site -- matching the slice the Phase 1 audit covered.
- Only the Context article template was fully specified in Phase 2, so
  that's the only content-type template checked structurally. Task
  articles are still checked against the universal title/heading rules,
  but not against a fixed section-order template (none was written for
  them yet).
- The "context vs. task vs. other" classification is Claude's judgment
  call per page, not a lookup table -- worth spot-checking against the
  flagged list.
- This is a structure/title checker only. It does not check prose quality,
  the "inconsistent terminology" problem, or the nav-label-vs-title
  mismatch problem -- those are different checks with different mechanics.
