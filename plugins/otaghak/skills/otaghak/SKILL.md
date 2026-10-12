---
name: otaghak
description: "Unofficial read-only Otaghak: search Iranian villas, availability, exact stay prices, reviews. Use when the user asks about Otaghak (otaghak.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Otaghak

Unofficial read-only Otaghak: search Iranian villas, availability, exact stay prices, reviews.

The tools below come from the `otaghak-mcp` MCP server. If they are not available, install it with `claude mcp add otaghak -- uvx otaghak-mcp`, or add `"otaghak": {"command": "uvx", "args": ["otaghak-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ot_help`: Read Otaghak's help center: the FAQ, or the guest terms (booking and cancellation rules,
- `ot_travel_guide`: Get the site's travel guide for a destination: guide text, the destination's FAQ (best season,
- `ot_room_calendar`: Get a room's calendar day by day: nightly price after and before discount (Toman), free or booked,
- `ot_price_quote`: Get the amount to pay (Toman) for a room, dates and guests: nights_total (the room page's
- `ot_holidays`: List Iranian public holidays (Fridays included) in a date range, with Jalali dates and weekdays.
- `ot_late_checkout`: Check whether a room offers late checkout, for how many hours and at what price (Toman, a unit
- `ot_room`: Get one room: description, capacity, rooms and beds, amenities, house rules, check-in/out times,
- `ot_reviews`: Get a room's rating (0-5), star histogram, six category scores, percent of guests who recommend it,
- `ot_similar_rooms`: Get 4-5 alternatives to a room (same city and type), as the room page shows them (or, while that list is
- `ot_host`: Check a host: response time, response and acceptance rates, member since, active rooms
- `ot_find_place`: Turn a place name into the city / province slugs that ot_search_rooms needs, or a room code into its room.
- `ot_search_rooms`: Search Otaghak stays (villas, cottages, apartments, eco-lodges) in a city, province or collection.
- `ot_search_filters`: List the search filters of a city, province or collection (or the whole site) with the codes ot_search_rooms takes.
- `ot_destinations`: Popular cities and collections (themed landing pages: discounted, jungle villas, villas with pool, ...).
- `ot_deals`: Current discounts: the home page's last-second deals and the most discounted stays (biggest percent first).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `OTAGHAK_MCP_PROXY` to an HTTP proxy with an Iranian IP.
