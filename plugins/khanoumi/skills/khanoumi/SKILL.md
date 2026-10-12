---
name: khanoumi
description: "Unofficial read-only Khanoumi: search cosmetics and skin care, compare prices, shades, reviews. Use when the user asks about Khanoumi (khanoumi.com) or wants cosmetics, skin and hair care or perfume in Iran."
---

# Khanoumi

Unofficial read-only Khanoumi: search cosmetics and skin care, compare prices, shades, reviews.

The tools below come from the `khanoumi-mcp` MCP server. If they are not available, install it with `claude mcp add khanoumi -- uvx khanoumi-mcp`, or add `"khanoumi": {"command": "uvx", "args": ["khanoumi-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `kh_search`: Search Khanoumi products by keyword: price, discount and stock of each match, sponsored items removed.
- `kh_find_cheapest`: Find the cheapest in-stock products for a keyword, one flat list sorted by payable price (Toman).
- `kh_browse`: List the products of a category, brand(s) or campaign tag with sorting, price range and filters.
- `kh_filters`: List the filters of a category, brand, tag or search: sub-categories, brands, colors and attribute facets
- `kh_categories`: List Khanoumi's category tree with ids, URL paths and product counts.
- `kh_brands`: Find brands by name (about 3,200 brands) with their slugs.
- `kh_deals`: List today's featured deals from the Khanoumi home page (the daily pink box "جعبه صورتی" and the other
- `kh_store_info`: Get Khanoumi's order rules: packaging cost, shipping fees and times, returns, payment and refunds,
- `kh_blog_search`: Search the Khanoumi magazine (مجله خانومی): buying guides, skin and hair care routines, ingredient
- `kh_product`: Get one product's full record: price and discount (Toman), every shade / size / seller variant with its
- `kh_reviews`: Read customer comments on a product, newest first, with a verified-buyer flag and photos.
- `kh_similar`: List alternatives to a product (about 20) or the products the shop pairs with it, with prices and stock.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `KHANOUMI_MCP_PROXY` to an HTTP proxy with an Iranian IP.
