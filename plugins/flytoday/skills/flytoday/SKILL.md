---
name: flytoday
description: "Unofficial read-only Flytoday: Iranian and international flights, hotels, villas, trains, buses. Use when the user asks about Flytoday (flytoday.ir) or wants flights, trains, buses, hotels, villas or tours in Iran."
---

# Flytoday

Unofficial read-only Flytoday: Iranian and international flights, hotels, villas, trains, buses.

The tools below come from the `flytoday-mcp` MCP server. If they are not available, install it with `claude mcp add flytoday -- uvx flytoday-mcp`, or add `"flytoday": {"command": "uvx", "args": ["flytoday-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ft_find_bus_city`: Bus city ids (4 digits) for a city name, or the popular cities when query is empty.
- `ft_bus_calendar`: Cheapest bus seat price per day for the next weeks (the site's price strip), in one cheap call.
- `ft_search_buses`: Buses between two cities on a date: company, terminals, departure, bus type, seats left, price per seat.
- `ft_cip`: CIP / VIP airport lounge service with prices for a date and passenger mix, plus paid add-ons.
- `ft_esim_plans`: eSIM data plans for a country with data amount, validity days and price, cheapest first.
- `ft_visa`: Visa services of Flytoday: the country list with from-prices, or one country's prices, documents and process.
- `ft_activities`: Tours, tickets and experiences in a destination that are on sale in the date range, with from-prices.
- `ft_activity`: One activity: description, highlights, options with adult prices, and the cheapest days in the range.
- `ft_find_airport`: Find the IATA codes the flight tools need, for domestic and international places.
- `ft_search_flights`: Search flights for a date: every flight with times, airline (airline_fa: Persian name), seats left, price and fare_source_code.
- `ft_flight_calendar`: Cheapest one-adult fare per departure day around a date, in one cheap call (no search needed).
- `ft_flight_details`: Refund and change rules, confirmed baggage per segment and (international) entry notes of one fare.
- `ft_find_hotel_place`: Find the place ids the hotel and stay tools need. Which id goes where:
- `ft_search_hotels`: Priced hotels of a city (Iran) or region (abroad) for dates, one row per hotel with its cheapest room offer.
- `ft_hotel`: One hotel for dates: every room and meal-plan offer with whole-stay price, rooms left and cancellation terms,
- `ft_hotel_reviews`: Guest reviews of a hotel: score (1-10), text, pros, cons, trip type and nights. Mostly Persian text.
- `ft_search_stays`: Villas, apartments and other private stays in Iran for dates, cheapest first.
- `ft_stay`: One villa / apartment: details (capacity, rooms, facilities, rules, host), the per-night price calendar with
- `ft_find_station`: Train station codes (`station_code`) for a city name, or the 8 most popular stations when query is empty.
- `ft_search_trains`: Trains between two stations on a date: one row per train class (wagon) with price per adult and seats left.
- `ft_train_calendar`: Cheapest train price per day for the next ~16 days, with sold-out days flagged.
- `ft_train_stops`: Stops of one train with arrival and departure times, plus (with wagon_id) the class amenities and extra meals.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `FLYTODAY_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Searches are rate-limited per IP. Do not repeat a search the user did not ask for.
