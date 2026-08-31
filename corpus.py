"""
The corpus this prototype runs against: every page in the Connectors,
Skills, and Plugins slice of claude.com/docs, pulled from
https://claude.com/docs/llms.txt on 2026-08-30.

Each page is fetched as markdown via the ".md" suffix Mintlify exposes
for every docs page.
"""

BASE = "https://claude.com/docs"

PAGES = [
    # Connectors: core
    "/connectors/overview",
    "/connectors/getting-started",
    "/connectors/directory",
    "/connectors/verification",
    "/connectors/custom/remote-mcp",
    "/connectors/custom/desktop-extensions",
    # Connectors: building
    "/connectors/building/index",
    "/connectors/building/what-to-build",
    "/connectors/building/authentication",
    "/connectors/building/mcp",
    "/connectors/building/lazy-authentication",
    "/connectors/building/enterprise-managed-auth",
    "/connectors/building/directory-vs-custom",
    "/connectors/building/testing",
    "/connectors/building/troubleshooting",
    "/connectors/building/review-criteria",
    "/connectors/building/after-publishing",
    "/connectors/building/managing-your-listing",
    "/connectors/building/mcpb",
    "/connectors/building/submission",
    # Connectors: MCP apps
    "/connectors/building/mcp-apps/getting-started",
    "/connectors/building/mcp-apps/design-guidelines",
    "/connectors/building/mcp-apps/transparent-theming",
    "/connectors/building/mcp-apps/instance-supersession",
    "/connectors/building/mcp-apps/cross-compatibility",
    "/connectors/building/mcp-apps/external-links",
    "/connectors/building/mcp-apps/troubleshooting",
    # Connectors: pre-built
    "/connectors/google/drive",
    "/connectors/google/gmail",
    "/connectors/google/calendar",
    "/connectors/microsoft/365",
    "/connectors/github/index",
    "/connectors/slack/index",
    # Skills
    "/skills/overview",
    "/skills/how-to",
    # Plugins
    "/plugins/overview",
    "/plugins/submit",
]

URLS = [BASE + p + ".md" for p in PAGES]
