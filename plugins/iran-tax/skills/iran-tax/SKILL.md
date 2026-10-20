---
name: iran-tax
description: "Unofficial read-only Iranian tax: goods IDs and VAT, activity codes, property values, tax laws. Use when the user asks about Iran Tax (tax.gov.ir) or wants e-invoice goods IDs, VAT rates, activity codes, property values or tax laws and circulars in Iran."
---

# Iran Tax

Unofficial read-only Iranian tax: goods IDs and VAT, activity codes, property values, tax laws.

The tools below come from the `iran-tax-mcp` MCP server. If they are not available, install it with `claude mcp add iran-tax -- uvx iran-tax-mcp`, or add `"iran-tax": {"command": "uvx", "args": ["iran-tax-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tx_goods_search`: Find e-invoice goods/service IDs (شناسه کالا و خدمات) and their VAT rate by description or ID.
- `tx_regulations_search`: Search the official tax regulation database (laws, circulars, rulings, opinions), newest first.
- `tx_regulation_text`: Return the full text of one tax law, circular, ruling or opinion, or just one article of it.
- `tx_activity_codes`: Find tax activity codes (کد فعالیت / اینتاکد) with their VAT status and official profit ratios.
- `tx_property_value`: Return the official property transaction value (ارزش معاملاتی املاک) per square metre at a map point.
- `tx_faq_search`: Search the tax administration's official FAQ (پرسش های متداول) and return matching questions with links.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `IRAN_TAX_MCP_PROXY` to an HTTP proxy with an Iranian IP.
- The first goods-ID search for a phrase takes 15 to 30 s; repeats are cached. The tax sites often refuse foreign connections; outside Iran the user needs IRAN_TAX_MCP_PROXY. Sites: tax.gov.ir, stuffid.tax.gov.ir (goods IDs), regulation.tax.gov.ir (laws and circulars).
