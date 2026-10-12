---
name: asalbanoo
description: "Unofficial read-only Asal Banoo: search cosmetics and skin care, compare prices, sizes, deals. Use when the user asks about Asal Banoo (asalbanooshop.com) or wants cosmetics, skin and hair care or perfume in Iran."
---

# Asal Banoo

Unofficial read-only Asal Banoo: search cosmetics and skin care, compare prices, sizes, deals.

The tools below come from the `asalbanoo-mcp` MCP server. If they are not available, install it with `claude mcp add asalbanoo -- uvx asalbanoo-mcp`, or add `"asalbanoo": {"command": "uvx", "args": ["asalbanoo-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ab_search`: Search Asal Banoo products by keyword: price, discount, stock and rating of each match.
- `ab_find_cheapest`: Find the cheapest in-stock products for a keyword, one flat list sorted by current price (Toman).
- `ab_browse`: List the products of a category or brand (or the whole shop) with sorting, price range, stock and attribute filters.
- `ab_filters`: List the attribute filters of a category or brand listing (volume, hair type, skin type, gender, origin...)
- `ab_categories`: List Asal Banoo's product categories (about 70: skin, make-up, hair, perfume, kids) with slugs and counts.
- `ab_brands`: List the brands Asal Banoo sells (about 250) with their slugs and product counts, biggest first.
- `ab_deals`: List the discounted in-stock products right now, biggest discount first (the site's "تخفیفات" page).
- `ab_shop_info`: Read one of the shop's policy pages as plain text: FAQ as question/answer pairs, other pages as text.
- `ab_blog_posts`: List Asal Banoo blog posts (skin and hair care guides, routines, "X vs Y" comparisons), newest first.
- `ab_blog_post`: Read one blog post as plain text, plus the products and categories it links to.
- `ab_product`: Get one product's record: price and discount (Toman), stock (with the exact count when low),
- `ab_reviews`: Read customers' reviews and questions about a product (1-5 stars, newest first) with the shop's answers.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `ASALBANOO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
