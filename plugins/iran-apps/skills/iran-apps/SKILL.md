---
name: iran-apps
description: "Unofficial read-only Cafe Bazaar and Myket: search apps, compare versions and ratings, top lists. Use when the user asks about Iran Apps (cafebazaar.ir) or wants Android apps or software and game download listings in Iran."
---

# Iran Apps

Unofficial read-only Cafe Bazaar and Myket: search apps, compare versions and ratings, top lists.

The tools below come from the `iran-apps-mcp` MCP server. If they are not available, install it with `claude mcp add iran-apps -- uvx iran-apps-mcp`, or add `"iran-apps": {"command": "uvx", "args": ["iran-apps-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ap_search`: Search Cafe Bazaar and/or Myket for apps and games by name; returns package names, ratings and store URLs.
- `ap_app`: Get one app's metadata from one store: version, rating and rating count, installs, size, update date, developer, price, description.
- `ap_compare`: Compare one package across Cafe Bazaar and Myket: version, rating, rating count, installs, size, update date, price.
- `ap_top`: List the top ('best') or newest ('new') apps or games of a store, per category or store-wide.
- `ap_categories`: List the category slugs of a store for apps and games, to pass as ap_top category.
- `ap_similar`: List apps the store shows as related to one app: Bazaar gives three groups (related, others also installed, similar), Myket one.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_APPS_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: Cafe Bazaar, Myket.
