---
name: fidibo
description: "Unofficial read-only Fidibo: search Persian ebooks and audiobooks, compare prices, free books. Use when the user asks about Fidibo (fidibo.com) or wants ebooks, audiobooks or printed books in Iran."
---

# Fidibo

Unofficial read-only Fidibo: search Persian ebooks and audiobooks, compare prices, free books.

The tools below come from the `fidibo-mcp` MCP server. If they are not available, install it with `claude mcp add fidibo -- uvx fidibo-mcp`, or add `"fidibo": {"command": "uvx", "args": ["fidibo-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `fd_search`: Search Fidibo's ebooks and audiobooks by title, author or keyword: price in Toman, discount, free and
- `fd_browse`: List books of a category (or all of Fidibo) in a chosen order, with optional free / Fidibo Plus / price filters.
- `fd_bestsellers`: Top-selling Fidibo books of the week, month or all time, optionally per kind and category, with prices in Toman.
- `fd_new`: Newest Fidibo books and audiobooks, optionally per kind and category, with prices in Toman.
- `fd_free`: Free ebooks and audiobooks on Fidibo (price 0), optionally per kind and category.
- `fd_categories`: List Fidibo's categories and sub-categories (slug + Persian title) of one top level.
- `fd_book`: Get one book's full record: price and discount (Toman), format (ebook / audiobook), pages or duration, file size,
- `fd_reviews`: Read reader reviews of a book: text, 1-5 stars, date, likes and replies count, plus the total number of reviews.
- `fd_similar`: Find books like this one: the bestsellers of its category (the book itself left out), with prices in Toman.
- `fd_author`: An author's, translator's or narrator's profile and their books on Fidibo, with prices in Toman.
- `fd_publisher`: A publisher's profile and its books on Fidibo, with prices in Toman.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `FIDIBO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
