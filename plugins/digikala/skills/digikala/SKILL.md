---
name: digikala
description: "Unofficial read-only Digikala: search products, compare sellers, price history, reviews, deals. Use when the user asks about Digikala (digikala.com) or wants electronics, appliances or other goods in Iran."
---

# Digikala

Unofficial read-only Digikala: search products, compare sellers, price history, reviews, deals.

The tools below come from the `digikala-mcp` MCP server. If they are not available, install it with `claude mcp add digikala -- uvx digikala-mcp`, or add `"digikala": {"command": "uvx", "args": ["digikala-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dk_search`: Search products by name: price (Toman), discount, seller, rating, 20 per page.
- `dk_find_cheapest`: Find the cheapest in-stock products that really match a query, sorted by price (Toman).
- `dk_best_for_budget`: Rank the best-rated in-stock products within a budget (Toman) by a rating weighted by its count.
- `dk_suggest`: Autocomplete a vague or misspelled query into keywords, categories and brands.
- `dk_filters`: List the filters of a category or a search: attributes, colors, sellers, price range (Toman), brands.
- `dk_categories`: Find category codes for dk_category_products and main-category ids for dk_best_sellers.
- `dk_category_products`: List one category's products with sort and filters (price in Toman), strict order.
- `dk_brand_products`: List a brand's products with sort and price filters (Toman), plus the brand id for brand_ids.
- `dk_seller`: Get a seller's reputation (rating 0-5, on-time shipping, cancellations, returns) and products.
- `dk_deals`: List today's Incredible Offers (flash deals), biggest discount first, in-stock only.
- `dk_best_sellers`: List current best sellers, overall or in one main category; also returns the main categories' ids for category_id.
- `dk_fresh_search`: Search or browse Digikala Fresh (supermarket). category_code beats query and also returns sub-categories.
- `dk_product`: Get one product's price, stock, rating, specs and every seller's offer (cheapest first).
- `dk_price_history`: Get ~30 days of daily buy-box prices (Toman) per color/variant, with lowest and highest.
- `dk_reviews`: Read customer reviews: stars 1-5 (null = none), text, pros/cons, verified buyer flag.
- `dk_questions`: Read customers' questions (20 per page) with up to 2 answers each (answered_by: buyer, seller, ...).
- `dk_similar`: List products similar to one (same kind, other models and brands).
- `dk_compare`: Compare 2-4 products side by side: price and rating, then the spec rows where they differ.
- `dk_shortlist`: Re-price up to 10 products in one call: price, cheapest offer, stock, rating and 30-day low (Toman).
- `dk_installments`: Get the Digipay credit-line offers for a product, in Toman.
- `dk_plus_plans`: List Digikala Plus plans (free shipments per month: jet = same-day Tehran/Karaj, fresh = supermarket) with price in Toman and benefits.
- `dk_gold_prices`: Get the live 18k gold price per gram and gold coin prices, in Toman.
- `dk_location`: Turn an address into coordinates, or coordinates into an address with Digikala's city_id and state_id.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DIGIKALA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
