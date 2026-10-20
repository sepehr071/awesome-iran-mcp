---
name: qavanin
description: "Unofficial read-only qavanin.ir: search Iranian laws and regulations, read full text and status. Use when the user asks about Qavanin (qavanin.ir) or wants laws, regulations, court votes or legal opinions in Iran."
---

# Qavanin

Unofficial read-only qavanin.ir: search Iranian laws and regulations, read full text and status.

The tools below come from the `qavanin-mcp` MCP server. If they are not available, install it with `claude mcp add qavanin -- uvx qavanin-mcp`, or add `"qavanin": {"command": "uvx", "args": ["qavanin-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `qv_law`: Read the full text of a law, regulation, court vote or opinion as sections (articles, notes, headings).
- `qv_law_info`: Metadata of a law: type, approving body, approval, notification and gazette dates and numbers, last status,
- `qv_amendments`: Which laws amended this one, which this one amends, and which of its articles were amended.
- `qv_article_history`: Every amendment of one article: type (اصلاحی...), date, the amending law and the replacing text.
- `qv_related`: Documents related to a law: other laws, and regulations, court votes and legal opinions that cite or
- `qv_search`: Search the Iranian law and regulation database (qavanin.ir, 168,000 documents) and list matching titles.
- `qv_lookup`: Find the ids that qv_search filters take: approving bodies, executing bodies, subjects, types, statuses, lists.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `QAVANIN_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- qavanin.ir is slow (1 to 15 s per call; a whole law can take 15 s). Prefer one good query over many.
