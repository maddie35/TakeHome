# Template: Context articles

A context article explains what something is and when to use it. It provides important conceptual information, but does not tell a user how to do something.

---

## Template rules

### CTX-ORDER — Section order is fixed

Sections appear in the order below and may not be reordered.

### CTX-OMIT — Sections may be omitted, not added

Sections marked *conditional* may be hidden when they do not apply. No section outside this list may be added. If content does not fit a section, it belongs on a different page.

### CTX-TITLES — Section titles are fixed or lightly editable

Fixed titles may not be changed. Editable titles allow minor wording changes only, for example "What is/are ___" becomes "What are desktop extensions?" All titles follow TITLE-CASE.

### CTX-NO-STEPS — No how-to or step content

A context article contains no numbered procedures and no imperative instructions telling the reader to perform an action in a product. Link to a task article instead.

**Conformance:** a violation is any ordered list of user actions, or any imperative sentence directing the reader to click, select, enter, navigate, or configure something.

---

## Sections

| Order | Section | Required | Title | Contains |
| --- | --- | --- | --- | --- |
| 1 | What is/are ___ | Required | Editable | One to three sentences defining the thing. Present tense. No comparisons, no benefits. |
| 2 | Types | Conditional | Fixed | The taxonomy, as a table where more than two items exist. |
| 3 | When to use it | Required | Editable | The conditions under which a reader chooses this over the alternatives. |
| 4 | How it works | Required | Editable | The mechanism. Explanation only; no procedures. |
| 5 | Security considerations | Conditional | Fixed | Risks and what the reader should weigh. No configuration steps. |
| 6 | Availability | Conditional | Fixed | Who can use it, where they can use it, or when they can use it. |
| 7 | Related articles | Required | Fixed | Links out, including to the task articles this page defers to. |

**Note: Security considerations** explains what the risk is and why it matters. Anything a reader would *do* about it — toggling a setting, blocking a tool, reviewing a permission — belongs in the task article and is linked from here.
