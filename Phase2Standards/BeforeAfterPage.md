# Rewrite of "Third-party connectors with remote MCP"

Source page: `claude.com/docs/connectors/custom/remote-mcp`

---

## Before

```
# Third party connectors with remote MCP
## What are third party connectors?
### Finding connectors
## Adding custom connectors
### For Team and Enterprise plans
### For Free, Pro, and Max plans
### Enabling connectors in chat
## The Add custom connector dialog, field by field
## Authenticating with request headers
### Adding a request header
### Enter the full header value
## Managing connectors
## Security and privacy
### Best practices
### Tool actions
## Reporting issues
## Related topics
```

---

## After

```
# Third-party connectors with remote MCP
## What are third-party connectors?
## When to use third-party connectors
## How it works
### Finding connectors
## Security considerations
### Security best practices
### Tool actions
## Availability
## Related articles
```

### After: Full text
```
# Third-party connectors with remote MCP
Connect Claude to your tools using the Model Context Protocol
​
## What are third-party connectors?
Third-party connectors, also called custom connectors, are connectors you or a third-party build using the Model Context Protocol (MCP). You can:
- Connect Claude to existing remote MCP servers.
- Build your own remote MCP servers for any tool.

## When to use third-party connectors
If a prebuilt connector doesn’t exist for your preferred tool, you can use custom connectors to allow Claude to operate within your preferred software and leverage comprehensive context from your external tools.

## How it works 
You can build and connect your own MCP servers. For details, see [new article on how to create them].

Alternatively, you can add a third-party connector as long as you have the URL of that remote MCP server.

### Finding connectors
Browse the Connectors Directory to discover third-party MCP servers that are ready to use across all Claude products. Some are verified by Anthropic and others are community connectors. See [Connector verification].

> **Security notice:** Custom connectors allow connections to unverified services. Claude can access and perform actions within these services, so review the security considerations below.

## Security considerations
​
### Security best practices
- Only connect to servers from trusted organizations
- Carefully review requested permission scopes during authentication
- Be aware of prompt injection risks; Claude has built-in protections
- Monitor for unexpected changes in tool behavior
​
### Tool actions

Remote MCP servers let Claude invoke tools that can read data from applications, create or modify or delete data, and take actions on your behalf.

For how to review approvals, turn connectors off, and block individual tools, see [Manage your connectors].

## Availability 
All users have access to use third-party connectors with remote MCP.

## Related articles
[Links]
```

---

## What changed and why

**The page was doing two jobs.** Five of its twelve sections were procedures: adding a connector for each plan tier, enabling connectors in chat, a field-by-field dialog walkthrough, adding a request header, and entering a header value. Under CTX-NO-STEPS, none of that belongs on a context page. It moves to task articles, and the context page links to them. This is the change that matters; everything else follows from it.

**Section order now matches the template.** The before page opened with a definition, then jumped straight into procedure. The after page follows the fixed order: what it is, when to use it, how it works, security, availability, related.

**"Third party" became "third-party."** The before page used both forms, including in the title. Compound modifiers before a noun take a hyphen, and inconsistent forms of the same term hurt search and retrieval.

**"Related topics" became "Related articles."** CTX-TITLES fixes this wording. Across the section, the same final heading currently appears under at least two names.

**Two sections were dropped rather than moved.** "Managing connectors" and "Reporting issues" are both procedural and both duplicate content that belongs elsewhere. They become links.

**An Availability section was added.** The before page never stated who can use this. Under the template, availability is a fixed section using the same table on every primitive page.

**A long security paragraph became a callout.** The security notice was previously body text inside the connector-finding content, where scanning readers skip it. As a callout it stays visible without interrupting the sequence.

**What I did not fix here.** The page title is five words, at the TITLE-LEN maximum. A shorter title, "Third-party connectors," would conform more comfortably and would still match navigation — but renaming has a URL and redirect cost, so I flagged it rather than making it unilaterally.
