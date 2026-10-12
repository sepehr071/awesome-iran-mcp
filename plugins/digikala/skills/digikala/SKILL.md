---
name: digikala
description: "Unofficial read-only Digikala: search products, compare sellers, price history, reviews, deals. Use when the user asks about Digikala (digikala.com) or wants to buy electronics, appliances or other goods in Iran."
---

# Digikala

Unofficial read-only Digikala: search products, compare sellers, price history, reviews, deals.

The tools below come from the `digikala-mcp` MCP server. If they are not available, install it with `claude mcp add digikala -- uvx digikala-mcp`, or add `"digikala": {"command": "uvx", "args": ["digikala-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dk_search`: Search Digikala products by name, with price (Toman), discount, seller and rating.
- `dk_find_cheapest`: Find the cheapest in-stock products that really match a query, one flat list sorted by price.
- `dk_best_for_budget`: Rank the best-rated in-stock products within a budget, with the reasoning shown.
- `dk_suggest`: Autocomplete a vague or partial query into better search words, categories and brands.
- `dk_filters`: List the filters Digikala offers for a category or a search: features, colors, sellers, price range.
- `dk_categories`: Find category codes for dk_category_products and main-category ids for dk_best_sellers.
- `dk_category_products`: List the products of one category with sort and filters (price in Toman, brand, features, stock).
- `dk_brand_products`: List a brand's products on Digikala with sort and price filters (Toman), plus the brand id for brand_ids.
- `dk_seller`: Get a marketplace seller's reputation (rating 0-5, on-time shipping, cancellations, returns) and products.
- `dk_deals`: List today's Incredible Offers (flash deals), biggest discount first, in-stock only.
- `dk_best_sellers`: List Digikala's current best-selling products, overall or in one main category.
- `dk_fresh_search`: Search or browse Digikala Fresh (the supermarket: dairy, groceries, drinks, hygiene).
- `dk_product`: Get one product's price, stock, rating, specs and every seller's offer (cheapest first).
- `dk_price_history`: Get about 30 days of daily buy-box prices (Toman) per color/variant, with lowest and highest.
- `dk_reviews`: Read customer reviews of a product: stars 1-5 (null = no stars given), text, pros/cons, verified buyer flag.
- `dk_questions`: Read customers' questions about a product and up to 2 answers each (answered_by: buyer, seller, ...).
- `dk_similar`: List products similar to one product (same kind, other models and brands).
- `dk_compare`: Compare 2-4 products side by side: price and rating, then the spec rows where they differ.
- `dk_shortlist`: Re-price up to 10 products in one call: today's price, cheapest offer, stock, rating and 30-day low.
- `dk_installments`: Get the Digipay credit-line offers available when buying a product, in Toman.
- `dk_plus_plans`: List Digikala Plus membership plans (free shipments) with their price in Toman and benefits.
- `dk_gold_prices`: Get Digikala's live 18k gold price per gram and gold coin prices, in Toman.
- `dk_location`: Turn an address into coordinates, or coordinates into an address with Digikala's city_id and state_id.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DIGIKALA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
