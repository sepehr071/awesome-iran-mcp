---
name: okala
description: "Unofficial read-only Okala: grocery stores that deliver to you, compare prices across stores. Use when the user asks about Okala (okala.com) or wants food or groceries delivered in Iran."
---

# Okala

Unofficial read-only Okala: grocery stores that deliver to you, compare prices across stores.

The tools below come from the `okala-mcp` MCP server. If they are not available, install it with `claude mcp add okala -- uvx okala-mcp`, or add `"okala": {"command": "uvx", "args": ["okala-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ok_login`: Log in to the user's Okala account, which unlocks Okala's real text search in ok_search
- `ok_login_verify`: Finish a login started with ok_login: the code the user received by SMS. Saves the login on this
- `ok_account`: Whether the server is logged in to Okala (and as which phone, masked). Logged in = ok_search uses
- `ok_logout`: Delete the saved Okala login on this machine; the server continues as a guest.
- `ok_categories`: Category tree (id, slug, Persian name, children) of everything sold near a point, or in one store.
- `ok_search`: Find products by text, best matches first, then cheapest (Toman). `mode` tells which way ran:
- `ok_compare`: Which nearby store sells the same product cheapest. Fetches a category (and/or brand) from every store
- `ok_store_products`: A whole category of one store (the API returns all of it at once), sorted and optionally filtered by
- `ok_product`: One product in one store: price and discount (Toman), stock, max per order, brand, category,
- `ok_brands`: Brand ids for ok_compare (`brand_id`) and slugs. Okala publishes only a short list of featured brands;
- `ok_deals`: Deal rows running now, with their end time (UTC) and top products (Toman, discount, store).
- `ok_offer`: Every product of one deal row (from ok_deals), Toman. Without store_id: across all open stores that
- `ok_locate`: Turn an address into coordinates (lat, lon) for every other tool, plus the street address of the best hit.
- `ok_stores`: List the Okala stores (supermarkets, bakeries, fruit shops, chains) that deliver to a point, in the
- `ok_store`: One store as seen from the delivery point: whether it delivers there now, minimum order (Toman),
- `ok_store_reviews`: Read customers' reviews of a store: 1-5 stars, comment, date and the reasons they ticked

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `OKALA_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- One exception to no login: real text search needs the optional SMS login (`ok_login`), which stays read-only. Ask the user before starting it.
