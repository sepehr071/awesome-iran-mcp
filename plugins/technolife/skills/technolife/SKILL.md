---
name: technolife
description: "Unofficial read-only Technolife: search electronics, compare sellers and installment prices, deals. Use when the user asks about Technolife (technolife.com) or wants to buy electronics, appliances or other goods in Iran."
---

# Technolife

Unofficial read-only Technolife: search electronics, compare sellers and installment prices, deals.

The tools below come from the `technolife-mcp` MCP server. If they are not available, install it with `claude mcp add technolife -- uvx technolife-mcp`, or add `"technolife": {"command": "uvx", "args": ["technolife-mcp"]}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `tl_categories`: Find category pages and their urls for tl_category_products.
- `tl_category_products`: List the products of a category, brand or promotion page with prices, discount, stock and rating.
- `tl_category_filters`: List the filters of a category, brand or promotion page: brands, categories, price range and attributes with their codes.
- `tl_store_info`: Read one of Technolife's info pages as plain text.
- `tl_faq`: Search Technolife's help-center FAQ and return matching questions with plain-text answers.
- `tl_shop_reviews`: Read customer reviews of the Technolife shop itself (service, delivery), newest first, rating 1-5, with staff replies.
- `tl_find_location`: Turn an address or landmark into coordinates with its province and city.
- `tl_reverse_geocode`: Describe coordinates as an address with province, city and neighbourhood.
- `tl_deals`: List current in-stock discounts (Technolife's main deal list, تکنوآف) and, on page 0, the timed home-page deals (تکنو تایم).
- `tl_campaigns`: List current campaigns, or show one campaign's sections and products.
- `tl_seller`: Get a marketplace seller's reputation (rating 0-5, on-time %, fault-free %, time on Technolife) and its products.
- `tl_product`: Get one product's offers: price per color, seller and warranty, stock, delivery time, insurance and installment prices.
- `tl_compare`: Compare 2-5 products side by side: price, stock, rating and every spec.
- `tl_reviews`: Read customer reviews of a product: average 0-5, star distribution, AI summary with pros/cons, and the reviews.
- `tl_price_basket`: Get the exact total for a set of seller items: discounts, insurance, quantity limits, cash vs installment price.
- `tl_suggest`: Turn a product name into Technolife product codes (typeahead, up to 30 products, no prices).
- `tl_search`: Search Technolife products with prices, discount, stock and rating.
- `tl_find_cheapest`: Find the cheapest in-stock products for a search, one flat list sorted by the real price after discount.
- `tl_find_brand`: Look up a brand by its Persian name: filter code and brand page.

## Rules

- Prices are Toman. Convert before comparing with a Rial figure from anywhere else.
- Read-only: no login, basket, booking, order or payment. Give the user the link to finish on the site.
- Keep request rates low. These are undocumented site APIs that can change or rate-limit.
- On timeouts or HTTP 403 outside Iran, set `TECHNOLIFE_MCP_PROXY` to an HTTP proxy with an Iranian IP.
