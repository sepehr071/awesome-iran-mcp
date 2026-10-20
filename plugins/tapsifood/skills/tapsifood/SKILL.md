---
name: tapsifood
description: "Unofficial read-only Tapsi Food: search dishes and restaurants, menus, reviews, flash deals. Use when the user asks about Tapsi Food (tapsi.food) or wants food or groceries delivered in Iran."
---

# Tapsi Food

Unofficial read-only Tapsi Food: search dishes and restaurants, menus, reviews, flash deals.

The tools below come from the `tapsifood-mcp` MCP server. If they are not available, install it with `claude mcp add tapsifood -- uvx tapsifood-mcp`, or add `"tapsifood": {"command": "uvx", "args": ["tapsifood-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tf_search_dishes`: Search dishes by name near a delivery point, with price, discount and restaurant.
- `tf_search_vendors`: Search restaurants and stores by name or cuisine near a delivery point.
- `tf_restaurants`: List restaurants (or grocery stores) delivering to a point, with rating, delivery fee, minimum order and ETA.
- `tf_deals`: List the Tap Time flash deals (تپ تایم): discounted dishes with a limited stock, near a point.
- `tf_discounted_vendors`: List the vendors in Tapsi Food's 'Food Shots' (فودشات) discount campaign near a point.
- `tf_find_location`: Turn a place name or address into latitude/longitude.
- `tf_reverse_geocode`: Describe coordinates as an address with province and city.
- `tf_list_cities`: List the cities Tapsi Food shows, with a center point and whether it delivers there.
- `tf_menu`: Read a vendor's live menu: every dish (one entry per size/variation) with price, discount and stock.
- `tf_vendor_info`: Get a vendor's delivery fee to a point, minimum order, packaging, ETA, open_now, hours, address and rating spread.
- `tf_reviews`: Read customer reviews of a vendor, newest first, with the rating of each ordered dish.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TAPSIFOOD_MCP_PROXY` to an HTTP proxy with an Iranian IP.
