---
name: shopino
description: "Unofficial read-only Shopino: search fashion across Iranian shops, compare prices, sizes, stock. Use when the user asks about Shopino (shopino.app) or wants clothes, shoes or bags in Iran."
---

# Shopino

Unofficial read-only Shopino: search fashion across Iranian shops, compare prices, sizes, stock.

The tools below come from the `shopino-mcp` MCP server. If they are not available, install it with `claude mcp add shopino -- uvx shopino-mcp`, or add `"shopino": {"command": "uvx", "args": ["shopino-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sh_search`: Search products across all Shopino shops by keyword: price to pay, discount, stock and selling shop.
- `sh_find_cheapest`: Find the cheapest in-stock products for a keyword across all shops, one flat list sorted by price to pay (Toman).
- `sh_browse`: List products of a category, a shop, a product tag or a curated listing, with sorting, price range and filters.
- `sh_filters`: List the filter values sh_search / sh_browse accept: size systems with their sizes, sort orders,
- `sh_categories`: List Shopino's category tree (clothing, bags, shoes, accessories, watches, jewelry, gold, cosmetics, ...)
- `sh_brands`: Without shop_id: the official brand shops Shopino features (each is a shop: browse it with
- `sh_deals`: List today's featured deals from the Shopino home page: the flash sale (شگفت انگیز) with its end
- `sh_campaign`: Open a Shopino campaign or landing page: its product rows (with prices) and its tabs.
- `sh_blog_search`: Search the Shopino blog (style guides and model galleries: manteau, dress, bag, shoe models, ...),
- `sh_blog_post`: Read one Shopino blog post as plain text, with its category id for sh_browse.
- `sh_product`: Get one product's full record: price and discount (Toman), every color / size variant with its own
- `sh_similar`: Find products like this one at other shops, with prices, discount, stock and shop.
- `sh_shops`: Find Shopino shops (online and Instagram shops) by name, category group, gender or courier city,
- `sh_shop`: Get a shop's profile: rating, customer rating, buyer survey (satisfied, quality, price, on-time

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SHOPINO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
