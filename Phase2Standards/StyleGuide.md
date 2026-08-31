# Style guide excerpt: Titles and headings

Rules are written so that a reviewer applies them the same way twice. Each rule has an ID for reference in review comments and automated output.

---

## Titles

### TITLE-CASE — Sentence case only

All titles use sentence case. Capitalize the first word and proper nouns only.

| | |
| --- | --- |
| Yes | Remote MCP servers |
| No | Remote MCP Servers |

Applies to page titles, section titles, and card titles.

### TITLE-LEN — Article titles are 2 to 3 words, 5 maximum

Count words in the page title. Hyphenated compounds count as one word.

| | |
| --- | --- |
| Yes | Test your connector |
| No | How to test your connector before submitting it |

### TITLE-NAV — Article titles match the navigation name

The navigation label and the page title must be identical strings.

**Why:** WCAG 2.4 AA, Consistent Identification. Users navigating by heading or landmark rely on link text matching the page title to confirm they arrived in the right place. Readers with cognitive or memory disabilities are affected most.

### TITLE-VERB — Task article titles start with a present-tense verb

| | |
| --- | --- |
| Yes | Test your connector |
| No | Testing your connector |

Applies to task articles only. Context article titles are noun phrases.

---

## Section titles

### SEC-TENSE — Present tense, consistent across the page

If the first section is "Test as a custom connector," the next is "Test a local server," not "Testing a local server."

### SEC-BRIEF — Descriptive but brief

A section title must convey what the section contains without reading the section.

| | |
| --- | --- |
| Yes | Desktop vs remote |
| No | Details |
| No | When to use desktop vs remote |

"Details" tells a reader — or a retrieval system — nothing about the content. The third example is accurate but longer than it needs to be.

---

## Headings

### H2-START — The first heading after the page title is an H2

The page title is H1. No other H1 appears on the page.

### H-SEQ — Heading levels do not increase by more than one

An H2 may be followed by an H2 or an H3, never an H4. Decreasing by any amount is valid: H4 to H2 is allowed.

| | |
| --- | --- |
| Yes | h2 > h3 > h2 > h3 > h4 |
| No | h2 > h4 > h2 > h3 > h4 |

**Scope.** Evaluate the heading sequence only. Bold inline text is not a heading. Do not evaluate heading wording, consistency, or whether subsections are balanced across the page — those are covered by SEC-TENSE and SEC-BRIEF.

**Conformance.** Report a violation only when a specific transition breaks the rule, citing both headings by text and level: "H2 'Display modes' to H4 'Safe areas' skips H3." If no transition breaks the rule, report nothing for this rule.
