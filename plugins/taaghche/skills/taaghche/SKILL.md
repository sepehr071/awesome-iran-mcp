---
name: taaghche
description: "Unofficial read-only Taaghche: search Persian ebooks and audiobooks, compare prices, read reviews. Use when the user asks about Taaghche (taaghche.com) or wants ebooks, audiobooks or printed books in Iran."
---

# Taaghche

Unofficial read-only Taaghche: search Persian ebooks and audiobooks, compare prices, read reviews.

The tools below come from the `taaghche-mcp` MCP server. If they are not available, install it with `claude mcp add taaghche -- uvx taaghche-mcp`, or add `"taaghche": {"command": "uvx", "args": ["taaghche-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tg_search`: Search ebooks and audiobooks by title, author or topic: price, discount, rating, format.
- `tg_suggest`: Search-box typeahead: up to about 10 matching book titles with id and publisher. For prices use tg_search.
- `tg_book`: One book: price, discount, format, pages or duration, people, rating breakdown, categories, ISBN.
- `tg_reviews`: Reader reviews, most liked first: rating, text, likes, reply count. Page with offset.
- `tg_similar`: Related books as separate lists (similar works, same author, same publisher): price, format, rating.
- `tg_browse`: List books of a category (or the whole catalog), 16 per page, by sort, format and price ceiling.
- `tg_bestsellers`: Hottest books now (Taaghche's trending ranking; no sales numbers are public), overall or per category.
- `tg_new_releases`: Newest books (most recently added first), overall or per category. Next: tg_book.
- `tg_free_books`: Free books and audiobooks (price 0), most downloaded first by default. Next: tg_book.
- `tg_categories`: Category tree: top-level groups (id) and standalone categories, each with a slug.
- `tg_author`: An author's profile (with a slug: nationality, life dates, bio) and their books, 16 per page.
- `tg_publisher`: A publisher's description and its books, 16 per page.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TAAGHCHE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
