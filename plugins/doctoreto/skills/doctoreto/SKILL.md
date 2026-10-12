---
name: doctoreto
description: "Unofficial read-only Doctoreto: Iranian doctors, visit fees, free appointment times, clinics, labs. Use when the user asks about Doctoreto (doctoreto.com) or wants a doctor, clinic or lab appointment in Iran."
---

# Doctoreto

Unofficial read-only Doctoreto: Iranian doctors, visit fees, free appointment times, clinics, labs.

The tools below come from the `doctoreto-mcp` MCP server. If they are not available, install it with `claude mcp add doctoreto -- uvx doctoreto-mcp`, or add `"doctoreto": {"command": "uvx", "args": ["doctoreto-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `dt_search_centers`: Find hospitals, clinics, infirmaries, laboratories, imaging centers and pharmacies with filters.
- `dt_center`: A center's page: address, coordinates, departments, services, accepted insurances, attributes, opening
- `dt_doctor`: A doctor's profile with every bookable service, its price in Toman and its next free time.
- `dt_free_slots`: Free appointment times of one service (office visit, phone/video call, clinic offer, lab admission).
- `dt_reviews`: Patient reviews in the site's order (doctors and centers newest first, offers oldest first): stars 1-5,
- `dt_health_articles`: Search Doctoreto's health magazine (about 5,000 articles) for background on a condition, test or treatment.
- `dt_search_offers`: Search Doctoreto clinic offers: fixed-price procedures and packages (ultrasound, echo, laser, dental,
- `dt_offer`: One clinic offer in full: price, discount, deposit, who performs it and where, description, terms,
- `dt_suggest`: Search-box suggestions: matching doctors (with hash id), speciality slugs, service tags and centers.
- `dt_search_doctors`: Search doctors on Doctoreto by city, speciality, neighborhood, service tag, name, gender, insurance and visit type.
- `dt_specialities`: List medical, paramedical and dental specialities with the slug dt_search_doctors needs.
- `dt_cities`: Find a city's slug (for search filters) and numeric id (for dt_suggest).
- `dt_neighborhoods`: Neighborhoods of a city (most doctors first) and nearby cities, each with a doctor count.
- `dt_insurances`: List basic and supplementary insurers with the ids dt_search_doctors(insurance_ids=...) takes.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `DOCTORETO_MCP_PROXY` to an HTTP proxy with an Iranian IP.
