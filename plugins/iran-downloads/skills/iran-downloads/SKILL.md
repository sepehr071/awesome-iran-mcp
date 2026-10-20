---
name: iran-downloads
description: "Unofficial read-only metadata search of Soft98, P30Download, Downloadly and VGDL. Links only. Use when the user asks about Iran Software Downloads (soft98.ir) or wants Android apps or software and game download listings in Iran."
---

# Iran Software Downloads

Unofficial read-only metadata search of Soft98, P30Download, Downloadly and VGDL. Links only.

The tools below come from the `iran-downloads-mcp` MCP server. If they are not available, install it with `claude mcp add iran-downloads -- uvx iran-downloads-mcp`, or add `"iran-downloads": {"command": "uvx", "args": ["iran-downloads-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dl_list_sources`: List the four download-site sources and their latest-listing categories; call this first for valid ids.
- `dl_search`: Search the download sites by name and return metadata (title, item page url, category, date, short summary).
- `dl_latest`: Return the newest uploads of the download sites (soft98 has no latest listing), merged and sorted by date.
- `dl_item`: Return the details of one download item: name, version, size, category, date, description and system requirements.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_DOWNLOADS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Metadata only: it returns the item page URL on the source site and never a download link. Say that the user must check each item's licence on that page.
