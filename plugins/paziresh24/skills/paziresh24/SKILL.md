---
name: paziresh24
description: "Unofficial read-only Paziresh24: find Iranian doctors, profiles, prices, reviews and free slots. Use when the user asks about Paziresh24 (paziresh24.com) or wants a doctor, clinic or lab appointment in Iran."
---

# Paziresh24

Unofficial read-only Paziresh24: find Iranian doctors, profiles, prices, reviews and free slots.

The tools below come from the `paziresh24-mcp` MCP server. If they are not available, install it with `claude mcp add paziresh24 -- uvx paziresh24-mcp`, or add `"paziresh24": {"command": "uvx", "args": ["paziresh24-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `pz_doctor`: Full profile of one doctor: specialties, about text, medical council code, rating averages, insurance contracts, online visit (channels, price in Toman), and every office/hospital/clinic with address, phone, map, first free slot and services (ids, price, duration, weekly hours).
- `pz_first_available`: Whether a doctor can be booked now and the nearest free slot, for in-person and online visits and per center (Tehran time).
- `pz_reviews`: Patient reviews of a doctor (stars 1-5 for behaviour, explanation and treatment, text, visit reason, center, verified visit), paged, plus on the first page a summary: rating averages, counts and average waiting time per center.
- `pz_faq`: Answers from the official Paziresh24 FAQ: how booking works, cancelling or moving an appointment, online visits (channels, prescriptions), payment and refunds.
- `pz_suggest`: Turn words into pz_search_doctors arguments: matching cities (city slug), specialties (specialty slug) and the site's type-ahead query completions (use one as `text`).
- `pz_search_doctors`: Search Paziresh24 doctors (or hospitals and clinics) by city, specialty, name, online visit, gender, degree, with sorting and paging.
- `pz_resolve_url`: Turn a paziresh24.com link into its kind ('doctor' or 'center') and slug, plus the clean URL.
- `pz_center`: Profile of a hospital or clinic: type, address, phone, website, map, about text, departments, and its doctors (slug, department, specialty, basic insurance flags).
- `pz_free_days`: Days with at least one free appointment for one service of a doctor at one center, over the whole booking window (often 6-8 weeks), with the weekly days off and holidays in that window.
- `pz_free_slots`: Free appointment start times (Tehran HH:MM) per day for one service of a doctor at one center, for a date range.
- `pz_visit_price`: Exact price of one service in Toman: the doctor's fee, VAT and the payable total (what the online-visit invoice shows), plus Paziresh24's refund-on-cancel setting.
- `pz_holidays`: Official Iranian public holidays and occasions between two dates (Persian occasion name and the Hijri date).

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `PAZIRESH24_MCP_PROXY` to an HTTP proxy with an Iranian IP.
