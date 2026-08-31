# Phase 1 - Audit: Skills, Plugins, and Connectors

## Summary

The three primitives are documented as features of the products that use them rather than as a layer readers navigate on their own terms. Inside Connectors, the top-level split is by artifact type instead of by what the reader is trying to do, and the same page appears under two different categories. Below that, article structure varies page to page: prerequisites appear in three formats, titles mix verb tenses, and reference material sits inside conceptual pages.

The highest-value change is restructuring navigation around reader intent, with a fixed template per article type underneath it. The template work matters as much as the navigation. Consistent structure is what lets a retrieval system return the right section instead of a whole page, and it is the only part of this that a checker can enforce.

## Scope and method

This audit covers the Connectors, Skills, and Plugins sections of `claude.com/docs`, read directly against the published pages. Findings cite specific pages so each one can be verified.

---

## P0 — Costs readers time

### Navigation is organized by product offering, not reader intent

The Connectors section splits into artifact categories rather than tasks. A reader who wants to connect Gmail and a reader who wants to ship an MCP server need almost nothing in common, but both land in the same undifferentiated tree.

**Why it matters:** readers cannot tell which branch is theirs, so they browse instead of navigating.

**Fix:** restructure around use versus build, with a shared reference layer. Proposed tree in Question 3.

### The same page appears under two categories

On the Connectors overview, "Types of connectors" and "Ways to connect" both link to `/custom/remote-mcp`, under two different labels. Desktop extensions has the same problem.

**Why it matters:** the two axes are not mutually exclusive, which means the categories are not doing the work categories are supposed to do.

**Fix:** merge both sections into one decision table with one row per option.

### "What should I build: MCP, plugin, or both?" is buried

This page answers the question a reader has *before* they know which primitive they need. It currently sits three levels deep inside Building connectors.

**Why it matters:** the decision guide is unreachable by the people who need it most.

**Fix:** move it to the top of the build path.

### Article structure is inconsistent across every page type

There is no fixed shape for a task page or a context page, so no two are alike.

**Why it matters:** beyond reader friction, inconsistent structure defeats retrieval. Predictable headings mean predictable chunk boundaries, so a question about limits returns a limits section rather than a paragraph from the middle of a build guide. This is the AEO argument, and it is also what makes conformance checkable.

**Fix:** fixed templates per article type, enforced through Mintlify custom templates.

*Task and how-to articles:*
1. Prerequisites (if applicable)
2. Steps
3. Testing (if applicable)
4. Security (if applicable)
5. Related articles

*Context articles:*
1. What is it
2. Types (if applicable)
3. When to use it
4. How it works
5. Security (if applicable)
6. Availability (if applicable)
7. Related articles

---

## P1 — Causes confusion

### Navigation labels do not match page titles

**Why it matters:** this is an accessibility failure under WCAG 2.4 AA, Consistent Identification. Users navigating by heading or landmark rely on link text matching the page title to confirm they landed in the right place. Readers with cognitive or memory disabilities are affected most.

**Fix:** navigation label and page title must match exactly.

### Terminology is used interchangeably without being defined as interchangeable

"Third-party connectors" and "custom connectors" appear to refer to the same thing, but nothing says so.

**Fix:** pick one term per concept. Add a glossary covering MCP, MCP App, MCPB, and the connector types.

### Article and section titles follow no convention

- **Verb tense:** "Get started with connectors" against "Creating custom skills," both task articles.
- **Case:** some sections use title case, for example "Plugin Directory: Community vs. Anthropic Verified."

**Fix:** sentence case throughout. Task titles start with a present-tense verb.

### Prerequisites are formatted three ways

- *Enterprise Managed Auth for connectors:* complete sentences with an intro line.
- *Get started with connectors:* brief phrases, no intro.
- *Submitting to the Connectors Directory:* headed "Before you start," complete sentences with an intro.

**Why it matters:** readers learn the shape of a docs site and rely on it. Three shapes means checking each page from scratch.

**Fix:** one heading name, one format, specified in the template.

### "Get started with connectors" calls itself a tutorial

The intro refers to the article as a tutorial and includes a "What you'll learn" list.

**Why it matters:** the page tells the reader how to do something; it does not teach. Screen reader users encountering "tutorial" expect an actual learning module. The left-hand menu already provides the table of contents, so the bullet list is redundant.

**Fix:** rewrite the intro along the lines of "This guide walks you through setting up and using Claude's connector integrations to enhance your workflow," and drop the list unless user data supports keeping it — in which case apply it everywhere.

### Ordered lists are used for non-sequential content

Numbered lists appear where unordered lists are appropriate, for example under Desktop extensions > Enterprise deployment.

**Why it matters:** scanning readers read a numbered list as steps. Using the convention loosely teaches readers to distrust it.

**Fix:** ordered lists only for sequential steps.

### Desktop extensions is mostly context in a section of task pages

The page is conceptual where its neighbors are procedural, and its closing "Getting started" section has no links out.

**Fix:** add links to related resources such as Build a desktop extension with MCPB.

---

## P2 — Polish

### Individual steps carry too much text

In Remote MCP, step 2 under "Adding a request header" runs long enough that scanning readers skip it, despite containing information they need.

**Fix:** split the constraint out of the step and into a callout.

> **2.** Select a header name from the list, or choose **Custom header** to enter a different name. The list offers standard authentication and routing header names, such as `authorization`, `x-api-key`, and `x-auth-token`, which every connector can use.
>
> > **Note:** Anthropic reviews and approves each custom header name before Claude sends it to a third-party server. This prevents the connector configuration from being used to send arbitrary header names. If you enter a header name that is not approved, Claude rejects the save with an error. To request approval for a custom header name, contact Claude support.

---

## What should be deleted or merged

No pages should be deleted outright. Three merges:

| Merge | Into |
| --- | --- |
| Get started with connectors + Directory connectors vs custom connectors | One getting-started page |
| What to build + Building custom connectors | One build overview |
| Types of connectors + Ways to connect (sections on Connectors overview) | One decision table |

### What happens to readers who land on the old URLs

- For merges, keep the URL of the more visited page and 301 the other to it.
- For merged sections, redirect to the anchor rather than the top of the page, so readers land on the content they came for.
- Note renames and merges on the destination pages for roughly a month, since a redirect preserves traffic but not context.

**Open question:** the Building custom connectors landing page may not survive as a page. Once transport, protocol features, and technical specifications move to Reference and testing becomes its own page, what remains is a link list. Resolving this needs the full page inventory.

---

## Proposed information architecture

**Connectors**
- Overview
- Getting started
- Use connectors
  - Prebuilt integrations (overview)
  - Google integrations
  - Connectors directory
  - Set up and authenticate
- Build connectors
  - What to build (overview)
  - Remote MCP servers
  - MCP apps and bundles
  - Submit to directory
  - Testing
- Reference
  - Limitations and constraints (from Building custom connectors, currently headed "Technical specifications")
  - Glossary

**Skills**
- Overview
- Create custom skills
- Test custom skills
- Reference

**Plugins**
- Overview
- Submit your plugin

---

## What it would take to get there

**Phase 0 — Establish the baseline.** Collect and analyze docs metrics and support tickets. Map all site content against the proposed tree to find pages with no clear home. This phase determines whether the structure above survives contact with the full inventory.

**Phase 1 — Content fixes with no URL changes.** Title case and verb tense, prerequisites format, list types, the "Get started" intro rewrite, the Remote MCP callout.

**Phase 2 — Additive changes.** Merge sections within pages, add the Glossary and the Reference shell. Still no URLs move.

**Phase 3 — The restructure.** Merged and moved pages with one-to-one redirect mapping.

Running the cheap phases first delivers visible improvement before anyone is asked to approve URL churn.

**Running alongside:** create custom templates in Mintlify and establish enforcement, since a template without a mechanism is a suggestion. Confirm stakeholders for anything touching navigation config, redirects, or renamed anchors that other teams may have linked to.

---

## What I would measure

Each of these is captured before the work starts and compared after.

### Retrieval quality (AEO)

- Test retrieval on 10 or more questions, scored on accuracy and completeness of the answer.
- Track MCP searches. Mintlify reports what AI agents query and where they fail to find answers, so this is a direct before-and-after comparison.

### Search behavior

- Search queries, click-through rate on results, and AI responses.
- Named predictions rather than general monitoring. Queries for "limits" and "timeout" currently return nothing useful because the content is headed "Technical specifications." Those queries should resolve once the block moves to Reference and is renamed.
- Mintlify tracks these and forwards events to configured analytics integrations, so the querying happens wherever those events already land.

### Support tickets

- Volume and question type for tickets tied to connector setup, not total volume.
- Export by category for the target window. At Affirm we used Zendesk, where I exported by category and read ticket content directly where the tags were not specific enough. A dashboard or category export is sufficient; Claude can assist with classification, with human review.

### Migration health

- Page analytics on merged and moved pages, checking that traffic holds after redirects.
- 404 rate, watched closely in the first 48 hours after any URL change. Whether Mintlify surfaces this directly is unconfirmed; Google Analytics or another integration covers it otherwise.
- Alerting on sudden drops in views or spikes in 404s.

**One caveat worth stating.** Docs metrics move for reasons unrelated to docs — a product launch, a pricing change, a popular external tutorial. A redirect that resolves to the top of a long page instead of the right section will not appear in any 404 count. Time on page and immediate bounce from redirect targets are the closest available signals.
