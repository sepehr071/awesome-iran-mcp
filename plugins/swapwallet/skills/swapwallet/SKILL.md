---
name: swapwallet
description: "Crypto wallet: balances, P&L, history. Swaps, transfers and withdrawals need Telegram approval. Use when the user asks about SwapWallet (swapwallet.app) or wants to check or use their own SwapWallet crypto wallet in Iran."
---

# SwapWallet

Crypto wallet: balances, P&L, history. Swaps, transfers and withdrawals need Telegram approval.

SwapWallet is a custodial crypto exchange and wallet. Its MCP server (`swapwallet`) reads the user's own account and files money-moving requests that the user approves in Telegram.

The tools below come from SwapWallet's hosted MCP server at https://swapwallet.app/mcp (Streamable HTTP). If they are not available, add it to the client:

- Claude Code: `claude mcp add --transport http swapwallet https://swapwallet.app/mcp`
- Codex CLI: `codex mcp add swapwallet --url https://swapwallet.app/mcp`
- Gemini CLI: `gemini mcp add --transport http swapwallet https://swapwallet.app/mcp`
- Cursor: `"swapwallet": {"url": "https://swapwallet.app/mcp"}` under `mcpServers` in `~/.cursor/mcp.json`
- VS Code: `"swapwallet": {"type": "http", "url": "https://swapwallet.app/mcp"}` under `servers` in `.vscode/mcp.json`
- Windsurf: `"swapwallet": {"serverUrl": "https://swapwallet.app/mcp"}` under `mcpServers` in `~/.codeium/windsurf/mcp_config.json`
- Claude Desktop and claude.ai: Settings → Connectors → Add custom connector, with the URL

Restart the session after installing. The user then signs in once with OAuth. The client runs the sign-in, not the agent, and Claude Code doesn't open the browser by itself: run `/mcp`, pick the server and choose Authenticate, or run `claude mcp login <name>` with the name `claude mcp list` shows (`plugin:swapwallet:swapwallet` when installed as a plugin). Codex: `codex mcp login swapwallet`. Gemini CLI: `/mcp auth swapwallet`. Other clients show a sign-in button or prompt.

## Tools

- `get_total_balance`: The user's total portfolio value plus a per-token breakdown of every non-zero holding.
- `get_balance`: Balance and value of the given tokens only.
- `get_user_info`: The user's profile, verification level and account settings.
- `get_deposit_address`: The user's deposit address for a token on a network, creating one if needed.
- `get_profit_and_loss`: Realized and unrealized profit and loss, for all assets or the given tokens.
- `get_transactions`: Recent deposits, withdrawals, transfers and trades, newest first.
- `get_contacts`: The user's saved SwapWallet contacts, ten per page.
- `get_ibans`: The user's verified bank accounts, usable as a Rial withdrawal destination.
- `get_action_request`: The current status of a request created by one of the request_* tools: PENDING while the user has not answered, then EXECUTED, REJECTED, EXPIRED or FAILED.
- `request_swap`: Prices a swap between two tokens and sends it to the user's Telegram for approval.
- `request_transfer`: Prepares a transfer to another SwapWallet user and sends it to the user's Telegram for approval.
- `request_crypto_withdraw`: Prepares a crypto withdrawal and sends it to the user's Telegram for approval.
- `request_fiat_withdraw`: Prepares a Rial (IRT) withdrawal to one of the user's verified IBANs and sends it to their Telegram for approval.

## Reading the account

- Call the tools for balances, prices, profit and loss and history; never answer from memory.
- `get_total_balance` gives the whole portfolio; `get_balance` only the tokens you name.
- Amounts are decimal strings. `token` and `network` are enums: use the exact values in the tool's input schema.

## Moving money (request_* tools)

- `request_swap`, `request_transfer`, `request_crypto_withdraw` and `request_fiat_withdraw` never move money themselves. Each one prices the action and sends it to the user's Telegram (the SwapWallet bot) with Approve and Cancel buttons, then returns at once with status `PENDING`.
- Before calling one, confirm the amount, token, destination and (for crypto) the network with the user. A wrong network or address can lose funds.
- After calling one, tell the user to open Telegram and approve or cancel it there, and that it expires in 15 minutes. Show the returned preview (amounts, fees, destination); do not invent prices or fees.
- Never say a swap, transfer or withdrawal has happened until `get_action_request` reports `EXECUTED`. `PENDING` only means "waiting for the user in Telegram". The other outcomes are `REJECTED`, `EXPIRED` and `FAILED` (with a `failureReason`).
- Transfers go only to the user's saved contacts (`get_contacts`); toman withdrawals only to a verified IBAN (`get_ibans`).

## Known errors

- `MCP_TELEGRAM_NOT_LINKED`: the account is not linked to Telegram, so no request can be approved. Ask the user to link it in the SwapWallet app.
- `MCP_TWO_FACTOR_ACTIVE`: with two-factor authentication on, crypto withdrawals and transfers must be made in the app. Swaps and toman withdrawals still work.
- A missing scope means the user did not grant it on the consent page; they can reconnect and grant it.

Reference: https://swapwallet.app/docs/mcp
