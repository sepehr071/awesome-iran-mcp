---
name: 30book
description: "Unofficial read-only 30book: search Iranian printed books, compare editions and prices. Use when the user asks about 30book (30book.com) or wants ebooks, audiobooks or printed books in Iran."
---

# 30book

Unofficial read-only 30book: search Iranian printed books, compare editions and prices.

The tools below come from the `30book-mcp` MCP server. If they are not available, install it with `claude mcp add 30book -- uvx 30book-mcp`, or add `"30book": {"command": "uvx", "args": ["30book-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `sb_search`: Search 30book (about 200,000 printed books) by title. Each book has price (list), final_price (what you pay),
- `sb_browse`: List the books of a category (subject bta-N-M or topic btf-N-M-K; sections bts-N are only landing pages), a fiction genre, a national
- `sb_publisher`: One publisher's books with a short description of the publisher. Use to see a publisher's catalogue, best
- `sb_author`: Everything by one author or translator (title shows the Persian and Latin name). Default order: newest.
- `sb_bestsellers`: The site-wide best-selling books right now (10 pages of 20). Use for 'what is popular'.
- `sb_new_releases`: The newest books added to the store (10 pages of 20).
- `sb_deals`: Books with the biggest discount first: among the best sellers, or inside one subject. (The site's own
- `sb_find_publisher`: Look up publisher ids by name. Pass the id to sb_search(publisher_id=...) or sb_publisher.
- `sb_find_person`: Look up author / translator ids by name. Pass the id to sb_author or sb_search(author_id=...). The box matches
- `sb_book`: Full details of one book: title, authors, translators, publisher, price (list) and final_price in Toman,
- `sb_similar`: The lists on a book's page: similar books from the same topic, more by the same author and, for translations,
- `sb_reviews`: Reader comments on a book (name, Shamsi date, 1-5 stars, text, likes) plus the rating summary. Only the
- `sb_categories`: The top of the category tree: sections (کتاب عمومی, کتاب کودک و نوجوان, ...) and, for one section, its
- `sb_collections`: Curated collections linked from the home page: fiction genres, national literatures, literary award lists and

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `SIBOOK_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Lists are slow (2 to 5 s each). Prefer one good query over many.
