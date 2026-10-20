---
name: iran-quake
description: "Unofficial read-only Iran earthquakes: latest, search, strongest, detail, stats (USGS, EMSC, IRSC). Use when the user asks about Iran Earthquakes (irsc.ut.ac.ir) or wants recent or past earthquake data in Iran."
---

# Iran Earthquakes

Unofficial read-only Iran earthquakes: latest, search, strongest, detail, stats (USGS, EMSC, IRSC).

The tools below come from the `iran-quake-mcp` MCP server. If they are not available, install it with `claude mcp add iran-quake -- uvx iran-quake-mcp`, or add `"iran-quake": {"command": "uvx", "args": ["iran-quake-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `eq_latest`: List the most recent earthquakes in Iran, newest first.
- `eq_search`: Search earthquakes in Iran by date range, magnitude, bounding box and place text.
- `eq_significant`: List the strongest recent earthquakes in Iran, largest magnitude first.
- `eq_detail`: Get one earthquake in full: location, depth_km, magnitude type and source quality fields.
- `eq_stats`: Count earthquakes in Iran over a window: by magnitude band, by place, plus the strongest event.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_QUAKE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- Sites: IRSC (Iranian Seismological Center), USGS, EMSC.
