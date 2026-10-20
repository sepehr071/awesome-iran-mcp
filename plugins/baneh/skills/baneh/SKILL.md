---
name: baneh
description: "Unofficial read-only Baneh: search appliances, TVs, electronics, find the cheapest in-stock price. Use when the user asks about Baneh (baaneeh.com) or wants electronics, appliances or other goods in Iran."
---

# Baneh

Unofficial read-only Baneh: search appliances, TVs, electronics, find the cheapest in-stock price.

The tools below come from the `baneh-mcp` MCP server. If they are not available, install it with `claude mcp add baneh -- uvx baneh-mcp`, or add `"baneh": {"command": "uvx", "args": ["baneh-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `bn_search`: Search Baneh products by name in Persian or English, with price (Toman), stock and rating.
- `bn_find_cheapest`: Find the cheapest products whose title contains every word of the query, one list sorted by price (Toman).
- `bn_browse`: List products of a category and/or brand, optionally in a price range, sorted by price or rating.
- `bn_categories`: List shop categories with slug and product count, biggest first.
- `bn_brands`: List brands (about 150, e.g. LG, Samsung, Bosch, Xiaomi) with slug and product count, biggest first.
- `bn_product`: Get one product: price (Toman), stock, rating, brand, categories, spec attributes, highlights, description, images.
- `bn_reviews`: Get buyer reviews of one product, newest first: rating 1-5, author, date, text.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `BANEH_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Some prices are unusually low or high: they are the shop's own data, not a bug. Searches default to in-stock items only.
