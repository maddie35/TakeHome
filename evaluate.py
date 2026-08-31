"""
Runs every cached page in raw/ through Claude, asking it to evaluate the
page against the Phase 2 standard (standard.py) and flag structure
violations. Writes results.json and prints a summary of flagged pages.

Requires ANTHROPIC_API_KEY to be set in the environment.
"""

import json
import os
import pathlib
import sys

import truststore

truststore.inject_into_ssl()  # use the OS trust store (needed behind SSL-inspecting proxies)

import anthropic

from standard import FULL_STANDARD

RAW_DIR = pathlib.Path(__file__).parent / "raw"
OUT_PATH = pathlib.Path(__file__).parent / "results.json"
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")

EVAL_TOOL = {
    "name": "record_evaluation",
    "description": "Record the structural evaluation of a documentation page against the standard.",
    "input_schema": {
        "type": "object",
        "properties": {
            "page_type": {
                "type": "string",
                "enum": ["context", "task", "other"],
                "description": (
                    "context: explains a concept, no step-by-step instructions. "
                    "task: walks the reader through steps to accomplish something. "
                    "other: landing/index page, reference table, or a mix that doesn't "
                    "fit either template."
                ),
            },
            "flagged": {
                "type": "boolean",
                "description": "True if this page violates the standard in any way that a reviewer should act on.",
            },
            "violations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "rule": {
                            "type": "string",
                            "description": "Which specific rule from the standard was violated, quoted or closely paraphrased.",
                        },
                        "detail": {
                            "type": "string",
                            "description": "What on this exact page violates it -- quote the offending heading/title/section.",
                        },
                    },
                    "required": ["rule", "detail"],
                },
            },
            "summary": {
                "type": "string",
                "description": "One-sentence summary of the page's conformance, for a report a human will skim.",
            },
        },
        "required": ["page_type", "flagged", "violations", "summary"],
    },
}

SYSTEM_PROMPT = f"""You are auditing Claude's documentation site against a style guide and \
content-type template. You will be given one page's raw markdown. Evaluate ONLY structural \
conformance to the standard below -- title casing/length/tense, heading level structure \
(h2 start, no skipped levels), and, for pages you judge to be "context" articles, whether \
they follow the fixed Context article template section order.

Do not flag prose quality, grammar, or anything not covered by the standard. Be precise: \
every violation must cite the specific rule and the specific text on the page that breaks it. \
If a page is a "task" or "other" page, still check the universal title/heading rules, but do \
not apply the Context article template to it.

STANDARD:
{FULL_STANDARD}

Call record_evaluation exactly once with your findings."""


def slug_for_display(path: pathlib.Path) -> str:
    return path.stem.replace("__", "/")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY is not set. Set it and re-run:")
        print("  PowerShell:  $env:ANTHROPIC_API_KEY = 'sk-ant-...'")
        print("  bash:        export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    files = sorted(RAW_DIR.glob("*.md"))
    if not files:
        print(f"No cached pages found in {RAW_DIR}/. Run fetch.py first.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    results = []

    for i, path in enumerate(files, 1):
        page_id = slug_for_display(path)
        content = path.read_text(encoding="utf-8")
        print(f"[{i}/{len(files)}] evaluating {page_id} ...", end=" ", flush=True)

        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                tools=[EVAL_TOOL],
                tool_choice={"type": "tool", "name": "record_evaluation"},
                messages=[
                    {
                        "role": "user",
                        "content": f"PAGE: {page_id}\n\n{content}",
                    }
                ],
            )
        except anthropic.APIError as e:
            print(f"API ERROR: {e}")
            results.append({"page": page_id, "error": str(e)})
            continue

        tool_use = next(b for b in resp.content if b.type == "tool_use")
        evaluation = tool_use.input
        evaluation["page"] = page_id
        results.append(evaluation)

        flag = "FLAGGED" if evaluation["flagged"] else "ok"
        print(f"{flag} ({evaluation['page_type']}, {len(evaluation['violations'])} violation(s))")

    OUT_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")

    flagged = [r for r in results if r.get("flagged")]
    errors = [r for r in results if "error" in r]
    print(f"\n{len(results)} pages evaluated, {len(flagged)} flagged, {len(errors)} errors.")
    print(f"Full results written to {OUT_PATH}")

    if flagged:
        print("\n--- Flagged pages ---")
        for r in flagged:
            print(f"\n{r['page']}  [{r['page_type']}]")
            print(f"  {r['summary']}")
            for v in r["violations"]:
                print(f"  - {v['rule']}")
                print(f"      {v['detail']}")


if __name__ == "__main__":
    main()
