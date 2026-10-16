---
name: shopino
description: "Unofficial read-only Shopino: search fashion across Iranian shops, compare prices, sizes, stock. Use when the user asks about Shopino (shopino.app) or wants clothes, shoes or bags in Iran."
---

# Shopino

Unofficial read-only Shopino: search fashion across Iranian shops, compare prices, sizes, stock.

The tools below come from the `shopino-mcp` MCP server. If they are not available, install it with `claude mcp add shopino -- uvx shopino-mcp`, or add `"shopino": {"command": "uvx", "args": ["shopino-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sh_search`: Search products across all shops by keyword: price to pay, discount, stock, selling shop.
- `sh_find_cheapest`: Find the cheapest in-stock products for a keyword across all shops, one flat list sorted by price to pay.
- `sh_browse`: List products of a category, shop, tag or curated listing, with sort, price range and filters.
- `sh_filters`: List the filter values sh_search / sh_browse accept: size systems and sizes, sorts, courier cities,
- `sh_categories`: List the category tree with ids, URL paths and levels, plus total product and shop counts.
- `sh_brands`: Without shop_id: featured official brand shops (browse one with sh_browse(shop_id=...)). With shop_id:
- `sh_deals`: List today's home-page deals (flash sale with end time, best sellers, themed rows), biggest discount
- `sh_campaign`: Open a campaign or landing page: its product rows (with prices) and tabs.
- `sh_blog_search`: Search the style blog (guides and model galleries), newest first; no query = latest posts.
- `sh_blog_post`: Read one blog post as plain text, with its category id for sh_browse (after sh_blog_search).
- `sh_product`: Get one product's full record: price, every color / size variant with its own price and stock, size
- `sh_similar`: Find products like this one at other shops (itself left out).
- `sh_shops`: Find shops by name, category group, gender or courier city, with rating, surveys, followers and product count.
- `sh_shop`: Get a shop's profile: ratings, buyer survey %, followers, product count, main categories, courier city,

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SHOPINO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
