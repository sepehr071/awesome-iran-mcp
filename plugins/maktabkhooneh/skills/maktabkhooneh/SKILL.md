---
name: maktabkhooneh
description: "Unofficial read-only Maktabkhooneh: search Persian online courses, compare prices, find free ones. Use when the user asks about Maktabkhooneh (maktabkhooneh.org) or wants online courses, lessons or certificates in Iran."
---

# Maktabkhooneh

Unofficial read-only Maktabkhooneh: search Persian online courses, compare prices, find free ones.

The tools below come from the `maktabkhooneh-mcp` MCP server. If they are not available, install it with `claude mcp add maktabkhooneh -- uvx maktabkhooneh-mcp`, or add `"maktabkhooneh": {"command": "uvx", "args": ["maktabkhooneh-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `mkh_search`: Full-text search of courses by title/topic: price, discount, hours, rating, students, teachers.
- `mkh_browse`: List courses of a category (or all about 5700) with the site's own filters: type, level, hours, rating, publisher, feature.
- `mkh_free_courses`: List the free courses (final_price 0, about 740 of them), optionally in one category: hours, rating, students.
- `mkh_cheapest`: Cheapest paid courses for a topic or category, ascending by final_price (what the customer pays).
- `mkh_deals`: Currently discounted courses, biggest discount first (discount_pct, price before and final_price after).
- `mkh_course`: One course: prices (full vs content-only), discount end, level, hours, teachers, publisher, prerequisites, FAQ.
- `mkh_curriculum`: The chapters and lessons of a course with type (lecture, quiz, project...) and duration (mm:ss).
- `mkh_reviews`: Learner reviews of a course (stars 1-5, text, date, instructor reply) plus the star histogram.
- `mkh_categories`: Category tree (about 680 nodes in 11 top-level groups): slugs for mkh_browse, mkh_free_courses, mkh_cheapest, mkh_deals.
- `mkh_teacher`: A teacher's profile (bio, students, rating, teaching hours, links) and their courses with prices.
- `mkh_organizations`: Course publishers (universities, companies, Maktabkhooneh itself, about 180) with the id used as a filter.
- `mkh_organization`: A publisher's totals (courses, students, rating) and its most popular courses.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `MAKTABKHOONEH_MCP_PROXY` to an HTTP proxy with an Iranian IP.
