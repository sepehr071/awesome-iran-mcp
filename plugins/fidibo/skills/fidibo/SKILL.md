---
name: fidibo
description: "Unofficial read-only Fidibo: search Persian ebooks and audiobooks, compare prices, free books. Use when the user asks about Fidibo (fidibo.com) or wants ebooks, audiobooks or printed books in Iran."
---

# Fidibo

Unofficial read-only Fidibo: search Persian ebooks and audiobooks, compare prices, free books.

The tools below come from the `fidibo-mcp` MCP server. If they are not available, install it with `claude mcp add fidibo -- uvx fidibo-mcp`, or add `"fidibo": {"command": "uvx", "args": ["fidibo-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `fd_search`: Search ebooks and audiobooks by title, author or keyword; cards with price (Toman), rating, authors.
- `fd_browse`: List books of a category (or all) in a chosen order, with free / Plus / price filters.
- `fd_bestsellers`: Top sellers of the week, month or all time, per kind and category (Toman).
- `fd_new`: Newest books and audiobooks, per kind and category (Toman).
- `fd_free`: Free ebooks and audiobooks (price 0), per kind and category.
- `fd_categories`: List category and sub-category slugs (with Persian titles) of one top level.
- `fd_book`: One book's full record: price (Toman), format, pages or duration, size, people, rating and star
- `fd_reviews`: Reader reviews of a book: text (cut at 400 chars unless full_text), 1-5 stars, date, likes, replies, total count.
- `fd_similar`: Books like this one: bestsellers of its category, the book itself left out (Toman).
- `fd_author`: An author's, translator's or narrator's profile and books (Toman).
- `fd_publisher`: A publisher's profile and books (Toman).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `FIDIBO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
