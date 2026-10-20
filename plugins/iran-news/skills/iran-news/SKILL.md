---
name: iran-news
description: "Unofficial read-only Persian news RSS: Mehr, Tabnak, Entekhab, Zoomit, Varzesh3, more. Use when the user asks about Iran News RSS (mehrnews.com) or wants news headlines or full news articles in Iran."
---

# Iran News RSS

Unofficial read-only Persian news RSS: Mehr, Tabnak, Entekhab, Zoomit, Varzesh3, more.

The tools below come from the `iran-news-mcp` MCP server. If they are not available, install it with `claude mcp add iran-news -- uvx iran-news-mcp`, or add `"iran-news": {"command": "uvx", "args": ["iran-news-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `nw_article`: Fetch one article page and return its full body text, split into parts for long stories.
- `nw_list_sources`: List the news sources with their group and category slugs; call this first to know valid `source` and `category` values.
- `nw_latest`: Return the newest headlines of one news source, optionally of one category.
- `nw_search`: Search recent headlines of several sources for a keyword (client-side over their current feeds, newest first).
- `nw_latest_all`: Return the newest headlines from every source (or the chosen ones), merged and sorted by time.
- `nw_tech_news`: Return the newest technology news (phones, laptops, AI, gadgets, apps, crypto, cars, security, games) with long summaries.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_NEWS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: Mehr, Khabaronline, Hamshahri, Tabnak, Entekhab, Asriran, Zoomit, Digiato, Varzesh3, Khabarvarzeshi.
