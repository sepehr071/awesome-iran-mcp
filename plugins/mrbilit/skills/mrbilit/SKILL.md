---
name: mrbilit
description: "Unofficial read-only MrBilit: Iranian flights, trains, buses, taxis and hotels, seats and prices. Use when the user asks about MrBilit (mrbilit.com) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# MrBilit

Unofficial read-only MrBilit: Iranian flights, trains, buses, taxis and hotels, seats and prices.

The tools below come from the `mrbilit-mcp` MCP server. If they are not available, install it with `claude mcp add mrbilit -- uvx mrbilit-mcp`, or add `"mrbilit": {"command": "uvx", "args": ["mrbilit-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `mb_search_buses`: Intercity buses on a date: company, terminal, times, price per seat, free seats, bus type, stops, refund penalties.
- `mb_bus_price_calendar`: Cheapest bus seat per day for a route; days without buses (or not on sale yet) are left out.
- `mb_bus_seats`: Seat map of one bus: free seat numbers, seats sold to women and to men, and a row-by-row layout.
- `mb_search_taxis`: Private door-to-door intercity taxis (whole car, up to 3 passengers) for a date, one offer per pick-up slot.
- `mb_notices`: Notices MrBilit currently shows on its pages (disruptions, rule changes, payment options), for a service or route.
- `mb_help`: Search MrBilit's official rules, FAQ and help-center guides; returns the best matching passages.
- `mb_travel_guide`: MrBilit's guide for a route or city (summary, FAQ, article) and matching travel-magazine posts.
- `mb_search_flights`: Search flights for a date: every bookable flight with price, seats left, baggage and times.
- `mb_flight_price_calendar`: Cheapest one-adult fare per day for a route over a date range, in one call.
- `mb_flight_fare_details`: Every fare of one flight with refund penalties, confirmed baggage, fare rules, notes and per-passenger prices.
- `mb_search_hotels`: Hotels and stays with a free room in a city for the dates, with the cheapest room price for the whole stay.
- `mb_hotel`: One hotel: stars, guest rating (0-5) and latest reviews, location, landmarks, check-in rules, amenities, FAQ.
- `mb_hotel_rooms`: Every room of a hotel with its exact price for the dates: whole stay, per night, rooms left, meals.
- `mb_hotel_calendar`: Cheapest one-night room price per night from today, up to about 48 days (often fewer).
- `mb_city_hotels`: Every listed hotel of a city, sold out ones included, with stars, rating and address; no prices.
- `mb_find_place`: Turn a city, airport, station or hotel name into the code a search takes.
- `mb_companies`: List airlines (IATA code), rail operators or bus companies (id) with Persian and English names.
- `mb_search_trains`: Trains between two stations on a date with every class (wagon), its price per adult and free seats.
- `mb_train_price_calendar`: Cheapest train ticket per day (one adult) for a route, only days with free seats.
- `mb_train_price`: Exact price of one train class for a party: per adult, child, infant, foreigner and empty berth, and the total.
- `mb_train_stops`: Every station a train stops at, in order, with the date and local time at each.
- `mb_alternative_routes`: Alternatives when direct trains are full or dear: trips with one change, and nearby train, bus and flight routes.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `MRBILIT_MCP_PROXY` to an HTTP proxy with an Iranian IP.
