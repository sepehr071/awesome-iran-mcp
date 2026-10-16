---
name: paziresh24
description: "Unofficial read-only Paziresh24: find Iranian doctors, profiles, prices, reviews and free slots. Use when the user asks about Paziresh24 (paziresh24.com) or wants a doctor, clinic or lab appointment in Iran."
---

# Paziresh24

Unofficial read-only Paziresh24: find Iranian doctors, profiles, prices, reviews and free slots.

The tools below come from the `paziresh24-mcp` MCP server. If they are not available, install it with `claude mcp add paziresh24 -- uvx paziresh24-mcp`, or add `"paziresh24": {"command": "uvx", "args": ["paziresh24-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `pz_doctor`: Full profile of one doctor: specialties, about, rating averages, insurances, online visit (channels, price in Toman) and every center with address, phone, map, first free slot and services (ids, price, duration, hours).
- `pz_first_available`: Whether a doctor can be booked now and the nearest free slot, in person, online and per center (Tehran time).
- `pz_reviews`: Patient reviews (stars 1-5, text clipped to 400 chars, visit reason, center, verified visit), paged, plus on the first page a summary: rating averages, counts and waiting time per center.
- `pz_faq`: Answers from the official Paziresh24 FAQ: booking, cancelling or moving, online visits, payment and refunds.
- `pz_suggest`: Turn words into pz_search_doctors arguments: matching cities, specialties (with slugs) and the site's query completions (use one as `text`).
- `pz_search_doctors`: Search doctors (or hospitals and clinics) by city, specialty, name, visit type, gender and degree, sorted and paged.
- `pz_resolve_url`: Turn a paziresh24.com link into its kind ('doctor' or 'center'), slug and clean URL.
- `pz_center`: Profile of a hospital or clinic: type, address, phone, website, map, about, departments and its doctors (slug, department, specialty, basic insurances).
- `pz_free_days`: Days with a free appointment for one service at one center over the whole booking window (often 6-8 weeks), with weekly days off and holidays.
- `pz_free_slots`: Free appointment start times (Tehran HH:MM) per day for one service at one center, for a date range.
- `pz_visit_price`: Exact price of one service in Toman: fee, VAT and payable total (the online-visit invoice), plus the refund-on-cancel setting.
- `pz_holidays`: Official Iranian public holidays and occasions between two dates (Persian name, Hijri date).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `PAZIRESH24_MCP_PROXY` to an HTTP proxy with an Iranian IP.
