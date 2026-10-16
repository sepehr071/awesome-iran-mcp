---
name: divar
description: "Unofficial read-only Divar: search Iran's classified ads, cheapest and best-value ads, price checks. Use when the user asks about Divar (divar.ir) or wants to find or price-check classified ads: homes, cars, phones and more in Iran."
---

# Divar

Unofficial read-only Divar: search Iran's classified ads, cheapest and best-value ads, price checks.

The tools below come from the `divar-mcp` MCP server. If they are not available, install it with `claude mcp add divar -- uvx divar-mcp`, or add `"divar": {"command": "uvx", "args": ["divar-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dv_categories`: The Divar category tree (236 nodes, up to 4 levels): slug, Persian name, path and whether it is a leaf.
- `dv_filters`: Every filter a category supports: key, type, Persian label, unit and the allowed options.
- `dv_filter_options`: Allowed values of a filter: brand and model keys (161 car brands), districts, or any option list.
- `dv_suggest`: What Divar's search box would suggest for some text, and which categories the text belongs to.
- `dv_parse_query`: Turn a plain Persian request into dv_search arguments: city, neighbourhoods, price bounds, category and leftover words.
- `dv_market`: Asking-price statistics of a search: min, p10, p25, median, p75, p90, max, mean; split by district and by day.
- `dv_appraise`: Is an ad's price (or a price you have in mind) high or low compared with similar ads? Percentile, verdict, confidence.
- `dv_status`: Is Divar reachable and how fast: version, a live latency check, caches and local watch state.
- `dv_cities`: City ids for a name (1,177 cities; Tehran is 1, Mashhad 3). Returns id, name, URL slug, province id and centre.
- `dv_districts`: Neighbourhoods (محله) of one city with ids, centre point and the main streets inside (Tehran has about 450).
- `dv_neighbours`: Neighbourhoods adjacent to a district, to widen a neighbourhood search to the surrounding area.
- `dv_locate`: The city, neighbourhood and street address of a GPS point.
- `dv_place_search`: Map autocomplete: turn a landmark or street name into coordinates and a bounding box.
- `dv_place_mapping`: Convert old Divar place ids to the current ones (Divar merged and renumbered places).
- `dv_boundary`: Neighbourhood borders of a city from Divar's GeoJSON: the city's bounding box, or one neighbourhood's polygon.
- `dv_post`: Everything public about one ad: price in Toman, specs, features, description, images, map position, seller type.
- `dv_posts`: Details of up to 10 ads in one call (compact: specs and one image, description cut at 300 characters).
- `dv_compare`: Side by side: the price of each ad and only the specs that differ (the identical ones are listed once).
- `dv_seller`: The seller behind an ad: how many personal and business ads they have, the business card (name, brand_token) and their ads.
- `dv_dealer`: A business account's public page: name, active ad count, member since and its first 11 ads.
- `dv_similar`: Ads similar to one ad: same brand/model (or category) and neighbourhood, widening step by step until enough are found.
- `dv_search`: Search Divar ads in one or more cities by category, text and filters; compact cards, prices in Toman.
- `dv_count`: How many active ads match a search, in one cheap call (capped: 10,000 means '10,000 or more').
- `dv_cheapest`: The cheapest ads of a search, cheapest first. Skips negotiable ads, placeholder or absurd prices and far-below-median outliers.
- `dv_best_for_budget`: Within a budget: the best-value ads (furthest below their peers' median) and the most you can get (closest to the budget).
- `dv_find_deals`: Ads priced well below the median of the same search, without a budget: scored deals, with bait and junk prices removed.
- `dv_new_since`: Ads published after a moment, newest first: poll this to watch a search (a new flat, a cheap car) without repeats.
- `dv_export`: The ads of a search as CSV or JSON lines text, ready to save to a spreadsheet or analyse.
- `dv_nearby`: Ads on the map around a GPS point, nearest first, with coordinates, distance, price chips and a thumbnail.
- `dv_watch`: Save a search and later get only the ads that appeared since the last check; stored in a local file, nothing is pushed.
- `dv_price_trend`: The median asking price of a search over the days you have checked it: records one point per day in a local file.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DIVAR_MCP_PROXY` to an HTTP proxy with an Iranian IP.
