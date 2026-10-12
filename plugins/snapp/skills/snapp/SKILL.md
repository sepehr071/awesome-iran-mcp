---
name: snapp
description: "Unofficial read-only Snappfood & SnappMarket: search food and groceries, compare prices, deals. Use when the user asks about Snappfood & SnappMarket (snappfood.ir) or wants food or groceries delivered in Iran."
---

# Snappfood & SnappMarket

Unofficial read-only Snappfood & SnappMarket: search food and groceries, compare prices, deals.

The tools below come from the `snapp-mcp` MCP server. If they are not available, install it with `claude mcp add snapp -- uvx snapp-mcp`, or add `"snapp": {"command": "uvx", "args": ["snapp-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `food_search`: Search dishes by name near a delivery point, with price, discount and restaurant.
- `food_find_cheapest`: Find the cheapest way to get a dish: scans menus of nearby open restaurants plus FoodParty deals.
- `food_restaurants`: List restaurants delivering to a point, with rating, delivery fee, ETA and coupon info.
- `food_menu`: Get one restaurant's menu: every item with price, discount, packaging fee and availability.
- `food_order_costs`: Get the extra costs and conditions of ordering from one restaurant.
- `food_reviews`: Read recent customer reviews of a restaurant (rating, text, what they ordered, vendor reply).
- `food_party_deals`: List today's FoodParty flash deals (deep discounts, limited stock, time window) still in stock.
- `food_meal_for_one`: List single-person meals (at most 299k Toman, free delivery), cheapest first.
- `food_discounted_vendors`: List restaurants running a discount now, plus the short "Gem" hunt discount if one is live.
- `find_location`: Turn a place name or address into latitude/longitude.
- `reverse_geocode`: Describe coordinates in words (point of interest, street, neighbourhood).
- `list_cities`: List cities Snappfood serves, with id, names and center coordinates.
- `market_search`: Search a grocery product across all SnappMarket stores delivering to the point.
- `market_find_cheapest`: Find the cheapest in-stock offers for a grocery product near the point.
- `market_stores`: List SnappMarket stores delivering to the point, with delivery fee, minimum order and rating.
- `market_store_info`: Get one store's delivery fee, minimum order, opening hours, rating and coupons for the point.
- `market_store_products`: Browse or search the products of one store.
- `market_categories`: List SnappMarket product categories and sub-categories with their ids.
- `market_product`: Get one product's details and price in one store.
- `market_party_deals`: List current SnappMarket "market party" flash deals near the point, biggest discount first.
- `market_reviews`: Read a store's 30 most relevant customer comments, rating 0-5.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SNAPP_MCP_PROXY` to an HTTP proxy with an Iranian IP.
