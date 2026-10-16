---
name: 30book
description: "Unofficial read-only 30book: search Iranian printed books, compare editions and prices. Use when the user asks about 30book (30book.com) or wants ebooks, audiobooks or printed books in Iran."
---

# 30book

Unofficial read-only 30book: search Iranian printed books, compare editions and prices.

The tools below come from the `30book-mcp` MCP server. If they are not available, install it with `claude mcp add 30book -- uvx 30book-mcp`, or add `"30book": {"command": "uvx", "args": ["30book-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sb_search`: Search books by title: price, final_price, discount_pct, in_stock, publisher, id.
- `sb_browse`: Books of a category (bta-N-M or btf-N-M-K; bts-N sections are landing pages only), genre, nation, award list or tag.
- `sb_publisher`: One publisher's books plus a short about text. Try sort='bestselling' or 'cheapest'.
- `sb_author`: Books by one author or translator (default newest first).
- `sb_bestsellers`: Site-wide best sellers (10 pages).
- `sb_new_releases`: Newest books (10 pages).
- `sb_deals`: Best sellers (or one subject) by biggest discount. Some publishers inflate list prices: compare final_price.
- `sb_find_publisher`: Look up publisher ids by name. Pass the id to sb_search(publisher_id=...) or sb_publisher.
- `sb_find_person`: Look up author / translator ids by name. Pass the id to sb_author or sb_search(author_id=...). The box matches
- `sb_book`: One book: authors, translators, publisher, price, final_price, discount_pct, in_stock, ISBN, pages, cover, size,
- `sb_similar`: Similar books, more by the author and (translations) by the translator, up to 20 each.
- `sb_reviews`: Reader comments (author, date, stars, text cut to 400 chars unless full_text, likes) and the rating summary;
- `sb_categories`: Category sections (کتاب عمومی, ...) or, for one section, its subjects (تاریخ, ...). Codes go to
- `sb_collections`: Home-page genres, nations, award lists and tags; ids go to sb_browse(kind=...).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SIBOOK_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Lists are slow (2 to 5 s each). Prefer one good query over many.
