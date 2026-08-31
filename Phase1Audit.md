# Phase 1 - Audit: Skills, Plugins, and Connectors

## Summary

Skills, Plugins, and Connectors are documented as features of the products that use them rather than as a layer users navigate to in their workflow. Connectors is split, at the top-level, by artifact type instead of by what the user's trying to do. Article structure varies from page to page: prerequisites appear in three formats, titles mix verb tenses, and reference and how-to material sits inside conceptual pages. The top-priority change is restructuring the information architecture based on the users' perspective/intent, and then establishing a fixed template for each article type. 

## Scope and method

This audit covers the Connectors, Skills, and Plugins sections of claude.com/docs, read directly against the published pages. 

---

## P0 — Costs user time

### a. Navigation is organized by product offering, not user intent

The Connectors section splits into product categories rather than tasks. A user who wants to connect Gmail and a user who wants to ship an MCP server both land in the same undifferentiated navigation tree.

**Why it matters:** users can't tell which branch is theirs, so they browse or use Search instead of navigating.

**Fix:** restructure around _use_ versus _build_, with a shared reference layer. Proposed information architecture tree towards the end of this page.

### b. Article structure is inconsistent across every page type

There's no template for a task page or a context page, so they're all structured differently.

**Why it matters:** beyond user friction, inconsistent structure negatively impacts AEO (agentic engine optimization). Predictable headings mean predictable chunk boundaries, so a question about limits returns a limits section rather than a paragraph from the middle of a build guide. 

**Fix:** fixed templates per article type, enforced through Mintlify custom templates, such as:

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

### c. "What should I build: MCP, plugin, or both?" is buried

This page answers the question a user has before they know which type they need. It currently sits inside Building connectors, but third-party connectors section has building-related articles, meaning it's buried below those.

**Why it matters:** the decision guide is not visible enough for the people who need it.

**Fix:** move it to the top of the build path.

---

## P1 — Causes confusion

### d. Navigation labels don't match page titles

**Why it matters:** this is an accessibility failure under WCAG 2.4 AA, Consistent Identification. Users navigating by heading or landmark rely on the link text matching the page title to confirm if they landed in the right place. Users with cognitive or memory disabilities are also affected by this issue.

**Fix:** navigation label and page title must match exactly.

### e. Terminology is used interchangeably without being defined as interchangeable

"Third-party connectors" and "custom connectors" appear to refer to the same thing, but nothing explicitly says so.

**Fix:** pick one term per concept, or in the least, explicitly state "also called" in the article. Add a glossary covering MCP, MCP App, MCPB, and the connector types.

### f. Article and section titles follow no convention

- **Verb tense:** "Get started with connectors" vs. "Creating custom skills," both task articles.
- **Case:** some sections use title case, for example "Plugin Directory: Community vs. Anthropic Verified."

**Fix:** sentence case throughout. Establish tilting convention, i.e., task titles start with a present-tense verb.

### g. Prerequisites are formatted three ways

- "Enterprise Managed Auth for connectors": complete sentences with an intro line.
- "Get started with connectors": brief phrases, no intro.
- "Submitting to the Connectors Directory": headed "Before you start," complete sentences with an intro.

**Why it matters:** users (and AI agents) learn the shape of a docs site and rely on it. Three shapes means checking each page from scratch.

**Fix:** one heading name, one format, specified in the template.

### h. "Get started with connectors" calls itself a tutorial

The intro refers to the article as a tutorial and includes a "What you'll learn" list.

**Why it matters:** the page tells the user how to do something; it does not teach. Screen reader users encountering "tutorial" expect an actual learning module. The left-hand menu already provides the table of contents, so the bullet list is redundant.

**Fix:** rewrite the intro along the lines of "This guide walks you through setting up and using Claude's connector integrations to enhance your workflow," and drop the list unless user data supports keeping it — in which case apply it everywhere.

### i. "Desktop extensions" is mostly context in a section of task pages

The page is conceptual where the other articles in the section are more procedural. Also, its closing "Getting started" section has only 1 hyperlink.

**Fix:** restructure/reorder articles, and add hyperlinks to the Getting started resources, such as [Build a desktop extension with MCPB](https://claude.com/docs/connectors/building/mcpb).

---

## P2 — Polish

### j. Ordered lists used for non-sequential content

Numbered lists sometimes appear where unordered lists should be used, for example, under Desktop extensions > Enterprise deployment.

**Why it matters:** AI and scanning users read a numbered list as steps. Using the convention loosely teaches users to distrust it.

**Fix:** ordered lists only for sequential steps.

### k. Individual steps carry too much text

In Remote MCP, step 2 under "Adding a request header" runs long enough that scanning users skip it, despite containing information they need.

**Fix:** split the constraint out of the step and into a callout, like this:

> **2.** Select a header name from the list, or choose **Custom header** to enter a different name. The list offers standard authentication and routing header names, such as `authorization`, `x-api-key`, and `x-auth-token`, which every connector can use.
>
> > **Important:** Anthropic reviews and approves each custom header name before Claude sends it to a third-party server. This prevents the connector configuration from being used to send arbitrary header names. If you enter a header name that is not approved, Claude rejects the save with an error. To request approval for a custom header name, contact Claude support.

---

## What should be deleted or merged

No pages should be deleted outright. Three merges:

| Merge | Into |
| --- | --- |
| Get started with connectors + Directory connectors vs custom connectors | One getting-started page |
| What to build + Building custom connectors | One build overview |
| Types of connectors + Ways to connect (sections on Connectors overview) | One decision table |

### What happens to users who land on the old URLs

- For merged pages, keep the URL of the more visited page and redirect the other to it.
- For merged sections, redirect to the new section anchor so users land on the content they came for.
- Note renames and merges on the destination pages for roughly a month.

**Open question:** the Building custom connectors landing page may not survive as a page. Once transport, protocol features, and technical specifications move to Reference and testing becomes its own page, only a list of links may remain. Resolving this needs the full page inventory.

---

## Proposed information architecture

**Connectors**
- Overview
- Getting started
- Use connectors
  - Prebuilt integrations (overview)
  - Google integrations > Drive, Gmail, Calendar
  - Microsoft 365 integration
  - Slack integration
  - GitHub integration
  - Connectors directory
  - Connector verification
  - Set up and authenticate 
- Build connectors
  - What to build (overview)
  - Third-party connectors with remote MCP
  - Desktop extensions > Build a desktop extension with MCPB
  - MCP > Getting started, Design guidelines, Transparency and theming, Superseding older widgets, Cross-platform compatibility, External links, Troubleshooting
  - Authentication > Enterprise Managed Auth for connectors, Lazy authentication for MCP servers
  - Testing your connector
  - Troubleshooting connectors
  - Submit to directory > Pre-submission checklist, Submitting to the Connectors Directory
  - Manage your listing after publishing
  - Managing your directory listing
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

**Phase 0 — Establish the baseline.** Collect and analyze docs metrics and support tickets. Map all site content against the proposed tree to find pages with no clear home, and adjust information architecture as needed.

**Phase 1 — Minor content fixes with no URL changes.** Title case and verb tense, prerequisites format, list types, the "Get started" intro rewrite, the Remote MCP callout.

**Phase 2 — Larger fixes with no URL changes.** Merge sections within pages, add the Glossary and the Reference shell. 

**Phase 3 — Restructure.** Merge and move pages with one-to-one redirect mapping. Add new pages as needed (e.g., Glossary). Create custom templates in Mintlify and establish enforcement. Confirm stakeholders for anything touching navigation config, redirects, or renamed anchors that other teams may have linked to.

---

## What I would measure

For each of these, measure before the work starts and after it finishes to compare:

### Retrieval quality (AEO)

- Test retrieval on 10 or more questions, scored on accuracy and completeness of the answer.
- Track MCP searches. Mintlify tracks this, including where AI agents fail to find answers, so this is a direct before-and-after comparison.

### Search behavior

- Measure search queries, click-through rate (CTR) on search results, and AI responses.
- Choose specific queries to measure, such as searches for "limits" and "timeout", and what we expect to happen (e.g., those searches should start resolving once the Technical specifications block moves to Reference and is renamed).
- Mintlify analytics tracks each of those, so we can review results in Mintlify, export to Google Sheets, or connect to analytics integration like Google Analytics. 

### Support tickets

- Track volume and question type for support tickets tied to connector setup.
- Depending on the tool that support uses, automate or manually export for target time window to analyze tickets. At Affirm, they used Zendesk so I exported tickets by category and reviewed ticket content manually as needed. Ideally, there’d be a dashboard to review or ability to export tickets by date and category/tag. Claude can assist with review/classification, with human review.

### Migration health

- Track page analytics on merged and moved pages, checking that traffic holds after redirects.
- Watch 404 rate closely in the first 48 hours after any URL change. Unsure if this is tracked in Mintlify; Google Analytics or another integration can cover it if not.
- Set up integration system or Claude to alert on sudden drops in views or spikes in 404s.
