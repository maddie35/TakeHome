"""
The Phase 2 standard, verbatim from the style guide excerpt and Context
article template. This is the rubric the checker asks Claude to apply.
"""

STYLE_GUIDE = """
TITLES

All titles:
- Sentence case only.
  Yes: "Remote MCP servers"
  No:  "Remote MCP Servers"

Article titles:
- 2-3 words; 5 words maximum.
- Must match the navigation name.
- Task articles must start with a present tense verb.
  Yes: "Test your connector"
  No:  "Testing your connector"

Section titles:
- Present tense.
- Singular.
- Be consistent: if the first section is "Test as a custom connector," the
  subsequent section should read "Test a local server," not "Testing a
  local server."
- Be descriptive but brief. "Details" doesn't tell a reader (or an AI
  agent) what's in the section. Prefer "Desktop vs remote" over "When to
  use desktop vs remote" -- same information, fewer words.

HEADINGS

- Always begin with h2. (Page titles are h1.)
- Don't skip heading levels.
  Yes: h2 > h3 > h2 > h3 > h4
  No:  h2 > h4 > h2 > h3 > h4
"""

CONTEXT_ARTICLE_TEMPLATE = """
TEMPLATE: Context articles (informational / conceptual pages, not
step-by-step instructions)

Template rules:
- Section order is fixed and cannot be reordered.
- Sections may be omitted when not applicable (marked "if applicable"
  below).
- Section titles: some are fixed wording (sentence case, listed exactly
  below); the rest allow minor edits as needed
  (e.g. "What is/are ___" -> "What are desktop extensions?").
- Page titles can be edited but must be sentence case.
- No how-to or step instructions belong on a context article. Link out to
  a task/how-to article instead.

Fixed section order:
1. What is/are ___
2. Types (if applicable)
3. When to use it
4. How it works
5. Availability (if applicable)
6. Related articles
"""

FULL_STANDARD = STYLE_GUIDE + "\n" + CONTEXT_ARTICLE_TEMPLATE
