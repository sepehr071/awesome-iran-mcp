---
name: tsetmc
description: "Unofficial read-only Tehran Stock Exchange (TSETMC): quotes, movers, order book, history, indices. Use when the user asks about TSETMC Tehran Stock Exchange (tsetmc.com) or wants Tehran stock exchange quotes, indices, order books or real versus legal trading in Iran."
---

# TSETMC Tehran Stock Exchange

Unofficial read-only Tehran Stock Exchange (TSETMC): quotes, movers, order book, history, indices.

The tools below come from the `tsetmc-mcp` MCP server. If they are not available, install it with `claude mcp add tsetmc -- uvx tsetmc-mcp`, or add `"tsetmc": {"command": "uvx", "args": ["tsetmc-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ts_search_symbols`: Find Tehran Stock Exchange instruments (shares, funds, rights, bonds) by ticker or name.
- `ts_get_quote`: Latest price, daily range, volume and key facts of one instrument on the Tehran Stock Exchange.
- `ts_market_movers`: Top traded instruments of a market today, ranked by gain, loss, volume, value or trade count.
- `ts_order_book`: Best five bid and ask levels (price, volume, order count) of one instrument.
- `ts_price_history`: Daily open, high, low, close, volume, trades and value of one instrument for its latest trading days, newest first.
- `ts_real_legal`: Buy and sell volume, value and buyer/seller counts split by real (individual) and legal (institutional) traders per day.
- `ts_indices`: TSE total index, market state and trading totals, plus every sector and market index with its change.
- `ts_index_history`: Daily close, high, low and percent change of a TSE index (total, equal-weight, sector...), newest first.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TSETMC_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Prices here are Rial (divide by 10 for Toman), not Toman. tsetmc.com serves mostly Iranian lines: outside Iran the user needs TSETMC_MCP_PROXY. The market trades Saturday to Wednesday mornings; after the close the order book is empty. Sites: tsetmc.com (Tehran Stock Exchange and Iran Fara Bourse).
