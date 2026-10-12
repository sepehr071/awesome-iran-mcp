---
name: payping
description: "PayPing merchant account for agents: balance, sales, invoices; create invoices and payment links. Use when the user asks about PayPing (payping.ir) or wants to manage their own PayPing merchant account in Iran."
---

# PayPing

PayPing merchant account for agents: balance, sales, invoices; create invoices and payment links.

The tools below come from the `payping-mcp` MCP server. If they are not available, install it with `claude mcp add payping -- uvx payping-mcp`, or add `"payping": {"command": "uvx", "args": ["payping-mcp"], "env": {"PAYPING_TOKEN": "${PAYPING_TOKEN:-}"}}` to the client's MCP servers config. It needs [uv](https://docs.astral.sh/uv/). Restart the session after installing.

## Tools

- `payping_get_profile`: Show the PayPing account behind PAYPING_TOKEN: username, name, email, phone and verification flags.
- `payping_get_balance`: Current PayPing wallet balance in Toman (money received and not yet withdrawn).
- `payping_get_sales_summary`: Sales totals for a period: total amount (Toman), transaction count and daily averages.
- `payping_list_transactions`: List payments (newest first) with amount (Toman), payer, description, isPaid and payment code, plus the
- `payping_get_payment`: Full detail of one payment by its payment code: amount, dates, payer, card, fees, refund state and
- `payping_list_withdrawals`: List settlements (withdrawals to your bank account): date, amount (Toman), code and whether it was paid
- `payping_get_withdrawal`: Detail of one settlement by code: amount (Toman), request and payout dates, IBAN, bank tracking number.
- `payping_list_customers`: List saved customers (code, name, phone, email, business name) with the total count.
- `payping_get_customer`: One customer by code: name, contact details, address, national id, memo.
- `payping_list_products`: List products (PayPing "financial items"): code, title, price (Toman), stock, active, has a payment link.
- `payping_get_product`: One product by code: title, description, price (Toman), stock, tax, image, category.
- `payping_list_coupons`: List discount coupons: name, type (0 = percent, 1 = Toman), amount, code, active, products it applies to.
- `payping_get_coupon`: One coupon by code: amount, expiry, max uses, number of buyers and their total spend.
- `payping_list_invoices`: List invoices: code, number, title, status (0 draft, 1 awaiting payment, 2 paid, 3 overdue, 4 cancelled),
- `payping_get_invoice`: One invoice by code with its items, customer, status and payment code, plus `url`, the public page where
- `payping_create_customer`: Save a new customer in the PayPing account and return it with its `code` (needed for invoices).
- `payping_create_product`: Create a product (financial item) and return its `code`. Then payping_create_payment_link makes a public
- `payping_create_payment_link`: Make a permanent public payment page for a product and return its `url` (https://ppng.ir/d/...), which
- `payping_create_coupon`: Create an active discount coupon and return its `code`. Creates real data: confirm with the user first.
- `payping_create_invoice`: Create an invoice for a saved customer, ready to pay, and return its `code`, `payCode` and `url` (the
- `payping_send_invoice`: Send an invoice to its customer by SMS/email from PayPing. Messages a real person: confirm with the user

## Rules

- This server acts on the user's own account (`PAYPING_TOKEN`). Confirm with the user before any call that creates, sends, edits or deletes something.
- On timeouts or HTTP 403 outside Iran, set `PAYPING_MCP_PROXY` to an HTTP proxy with an Iranian IP.
