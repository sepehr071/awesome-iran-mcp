---
name: milligold
description: "Unofficial read-only Milli.gold: live 18k gold price per milligram, history and platform stats. Use when the user asks about Milli.gold Prices (milli.gold) or wants live gold, coin, currency or crypto prices in Iran."
---

# Milli.gold Prices

Unofficial read-only Milli.gold: live 18k gold price per milligram, history and platform stats.

The tools below come from the `milligold-mcp` MCP server. If they are not available, install it with `claude mcp add milligold -- uvx milligold-mcp`, or add `"milligold": {"command": "uvx", "args": ["milligold-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `mg_get_price`: Get the current Milli.gold price of 18k melted gold, in Rial per milligram and per gram.
- `mg_price_history`: Get the Milli.gold 18k gold price series for a day, week or month, with high, low and change.
- `mg_platform_stats`: Get Milli.gold's headline numbers: users, trades, gold traded, gold held and branches.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `MILLIGOLD_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Prices come as Rial per milligram, Rial per gram and Toman per gram: say which unit you quote. This is Milli.gold's own price, not a market-wide gold quote.
