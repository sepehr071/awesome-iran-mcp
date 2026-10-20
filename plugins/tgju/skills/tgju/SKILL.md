---
name: tgju
description: "Unofficial read-only TGJU: live Iranian gold, coin, currency and crypto prices with daily history. Use when the user asks about TGJU Prices (tgju.org) or wants live gold, coin, currency or crypto prices in Iran."
---

# TGJU Prices

Unofficial read-only TGJU: live Iranian gold, coin, currency and crypto prices with daily history.

The tools below come from the `tgju-mcp` MCP server. If they are not available, install it with `claude mcp add tgju -- uvx tgju-mcp`, or add `"tgju": {"command": "uvx", "args": ["tgju-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tj_search_symbols`: Find TGJU symbols by name.
- `tj_list_categories`: Browse TGJU's market tree: folders (with ids) and symbols.
- `tj_category_table`: Live price table of one TGJU group: price, change, day high/low/open per symbol.
- `tj_get_prices`: Live price, day change, high and low for one or more TGJU symbols.
- `tj_market_summary`: Key Iranian market rates in one call: dollar, euro, dirham, pound, lira, gold gram and ounce, coins, silver, Brent, Bitcoin, Ethereum, Tether.
- `tj_price_history`: Daily history (open, low, high, close, change) of a TGJU symbol, for charts and trend questions.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TGJU_MCP_PROXY` to an HTTP proxy with an Iranian IP.
