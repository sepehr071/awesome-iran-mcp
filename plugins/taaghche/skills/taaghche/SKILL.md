---
name: taaghche
description: "Unofficial read-only Taaghche: search Persian ebooks and audiobooks, compare prices, read reviews. Use when the user asks about Taaghche (taaghche.com) or wants ebooks, audiobooks or printed books in Iran."
---

# Taaghche

Unofficial read-only Taaghche: search Persian ebooks and audiobooks, compare prices, read reviews.

The tools below come from the `taaghche-mcp` MCP server. If they are not available, install it with `claude mcp add taaghche -- uvx taaghche-mcp`, or add `"taaghche": {"command": "uvx", "args": ["taaghche-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tg_search`: Search Taaghche's ebooks and audiobooks by title, author or topic: price in Toman, discount, rating, format.
- `tg_suggest`: Typeahead of the Taaghche search box: up to about 10 book titles (with publisher) that match the text.
- `tg_book`: Everything about one book: price in Toman and discount, ebook or audiobook, pages or listening time, publisher,
- `tg_reviews`: Reader reviews of a book, most liked first: star rating, text, likes, number of replies.
- `tg_similar`: Books Taaghche suggests next to this one (similar works, other books of the same author and publisher),
- `tg_browse`: List books of a category (or the whole catalog) 16 at a time with a sort, a format and a price ceiling.
- `tg_bestsellers`: The hottest books right now (Taaghche's «داغ‌ترین» ranking, the closest thing to a bestseller list; no sales
- `tg_new_releases`: The newest books on Taaghche (most recently added first), overall or in one category and format.
- `tg_free_books`: Free books and audiobooks (price 0), by default the most downloaded first, overall or in one category.
- `tg_categories`: Taaghche's category tree for ebooks and audiobooks: top-level groups (with their category id and the
- `tg_author`: An author's profile (nationality, life dates, biography; with a slug) and their books, 16 at a time.
- `tg_publisher`: A publisher's description and its books, 16 at a time.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TAAGHCHE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
