---
name: iran-crypto
description: "Unofficial read-only Iranian crypto exchanges: prices in Toman, order books, trades, candles. Use when the user asks about Iran Crypto Exchanges (nobitex.ir) or wants live gold, coin, currency or crypto prices in Iran."
---

# Iran Crypto Exchanges

Unofficial read-only Iranian crypto exchanges: prices in Toman, order books, trades, candles.

The tools below come from the `iran-crypto-mcp` MCP server. If they are not available, install it with `claude mcp add iran-crypto -- uvx iran-crypto-mcp`, or add `"iran-crypto": {"command": "uvx", "args": ["iran-crypto-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ic_list_exchanges`: List the supported Iranian crypto exchanges, their native price unit and what each can answer.
- `ic_list_markets`: List the coins an exchange trades against Toman (IRT) or USDT.
- `ic_compare_price`: Compare one coin's price on every supported exchange in one call, cheapest first, with the spread.
- `ic_get_ticker`: Get the live price, best bid and ask, 24h range, change and volume of one coin on one exchange.
- `ic_get_orderbook`: Get the top bids and asks of one coin's order book on one exchange, with the spread.
- `ic_recent_trades`: Get the most recent public trades of one coin on one exchange, newest first.
- `ic_candles`: Get recent OHLC candles of one coin from Nobitex or Wallex, oldest first.
- `ic_top_movers`: List the biggest 24h gainers or losers on one exchange, with illiquid coins filtered out.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_CRYPTO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Public market data only: no keys, no trading. Every IRT price is already Toman and USDT markets are USDT. Check the order book before treating a spread between exchanges as an opportunity. Sites: Nobitex, Wallex, Bitpin, Ramzinex, Tabdeal, OMPFinex, Exir.
