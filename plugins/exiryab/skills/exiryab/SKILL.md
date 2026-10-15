---
name: exiryab
description: "Official read-only ExirYab: find Iranian doctors by name, city and specialty, with clinics and maps. Use when the user asks about ExirYab (exiryab.com) or wants to find a doctor, clinic or lab, or book an appointment in Iran."
---

# ExirYab

Official read-only ExirYab: find Iranian doctors by name, city and specialty, with clinics and maps.

ExirYab (exiryab.com, اکسیریاب) is a directory of Iranian doctors. Its official MCP server (`exiryab`) calls ExirYab's public API: it finds doctors by name, city and specialty, and returns each doctor's profile link, clinics, phones, weekly hours and map links.

The tools below come from the `exiryab-mcp` MCP server. If they are not available, install it with `claude mcp add exiryab -- uvx exiryab-mcp`, or add `"exiryab": {"command": "uvx", "args": ["exiryab-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `ey_search_doctors`: Find an Iranian doctor on exiryab.com by name, city and/or specialty: the best match plus alternatives, each with profile URL, clinics, phones, working hours and map links.
- `ey_cities`: Cities that have doctors on exiryab.com, with their province and doctor count, most doctors first.
- `ey_specialties`: Medical specialties on exiryab.com with their doctor count, most doctors first; sub-specialties name their `parent`.

## Finding a doctor

- Call `ey_search_doctors` with at least one of `name`, `city`, `specialty`, in Persian. A partial name works, and a province works as `city`.
- Read `confidence` before answering. `high`: one clear match. `medium` or `low`: say you are not sure and show a few `alternatives` (name, specialty, city) so the user can pick. `ranking`: no name was given, these are the top doctors. `none`: nothing found; check the spelling with `ey_cities` or `ey_specialties` and search again.
- `understood.dropped_filters` and `warnings` say when the server ignored a city or specialty to find the name. Tell the user, e.g. "I found him, but in Isfahan, not Tehran".
- Alternatives with `match.kind` `similar` are other doctors of the same specialty and area, not people with the requested name.
- A word with several meanings («قلب»: cardiology or heart surgery): `ey_specialties` lists the options with doctor counts.

## Answering

- Give the doctor's profile `url`, then the clinic `address`, `phones`, `weekly_hours` (an empty list means closed that day) and one map link (`neshan` or `balad` for users in Iran, `google_maps` otherwise).
- There is no booking or payment here. The user calls the clinic or uses `online_booking_url` when the doctor has one.
- This is a directory, not medical advice.

## Rules

- Read-only: no login, booking or payment.
- The API allows 60 requests per minute per IP. Do not loop over many searches; one good query beats many.

Reference: https://exiryab.com/llms.txt
