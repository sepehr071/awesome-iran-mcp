---
name: basalam
description: "Unofficial read-only Basalam marketplace: search products, cheapest offers, shops, reviews. Use when the user asks about Basalam (basalam.com) or wants electronics, appliances or other goods in Iran."
---

# Basalam

Unofficial read-only Basalam marketplace: search products, cheapest offers, shops, reviews.

The tools below come from the `basalam-mcp` MCP server. If they are not available, install it with `claude mcp add basalam -- uvx basalam-mcp`, or add `"basalam": {"command": "uvx", "args": ["basalam-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `bs_search`: Search Basalam products and return a page of cards with prices in Toman.
- `bs_find_cheapest`: List the cheapest in-stock offers for a query, cheapest first, prices in Toman.
- `bs_categories`: Browse Basalam's category tree and return ids for the category_id filter of bs_search.
- `bs_product`: Get one product: price in Toman, discount, stock, options (colors, sizes), attributes, rating and its shop.
- `bs_vendor`: Get a Basalam shop's profile: city, product count, shipping methods, activity and notice.
- `bs_vendor_products`: List one shop's products with prices in Toman, searchable and sortable.
- `bs_reviews`: Read customer reviews of a product with the star histogram, newest first.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `BASALAM_MCP_PROXY` to an HTTP proxy with an Iranian IP.
