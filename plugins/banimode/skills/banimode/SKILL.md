---
name: banimode
description: "Unofficial read-only Banimode: search fashion, compare prices, sizes, stock and flash deals. Use when the user asks about Banimode (banimode.com) or wants clothes, shoes or bags in Iran."
---

# Banimode

Unofficial read-only Banimode: search fashion, compare prices, sizes, stock and flash deals.

The tools below come from the `banimode-mcp` MCP server. If they are not available, install it with `claude mcp add banimode -- uvx banimode-mcp`, or add `"banimode": {"command": "uvx", "args": ["banimode-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `bm_search`: Search Banimode fashion products by keyword and return priced cards with discount, color and sizes in stock.
- `bm_browse`: List the products of a category and/or brand, with the same filters and cards as bm_search.
- `bm_categories`: Find category ids by name, or walk the tree: no arguments lists the top sections, parent_id lists children.
- `bm_brands`: Find brand ids by name (Persian or Latin), or list the first brands when no name is given.
- `bm_deals`: List today's flash-sale products (deep time-limited discounts) with the time left.
- `bm_product`: Get one product: every color with its price, discount, stock per size, features and short description.
- `bm_reviews`: Read customer reviews of a product: stars (1-5, null if only text), text, date and the shop's answer.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `BANIMODE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
