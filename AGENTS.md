# AGENTS.md

Guide for AI agents using or working on **awesome-iran-mcp**: 24 MCP servers for Iranian websites, 385 tools in
total. 22 are Python packages on PyPI, run as stdio servers with `uvx <package>`; all of them are unofficial except
`exiryab-mcp`, ExirYab's own server on its public API. Two are hosted by their sites:
`pasavard-mcp` (`https://pasavard.ir/api/mcp`, no sign-in) and `swapwallet-mcp` (`https://swapwallet.app/mcp`, OAuth
sign-in).

## Pick a server

| User wants to... | Server | Start with |
|---|---|---|
| Buy electronics, appliances, almost anything | `digikala-mcp` | `dk_find_cheapest`, `dk_best_for_budget`, then `dk_product`, `dk_price_history` |
| Every Iranian shop's price for one product, price history, whether now is a good time to buy | `torob-mcp` | `tb_cheapest`, `tb_sellers`, `tb_deal_check` |
| The best buy in a price range on Digikala or Snappshop, or whether today's price is good | `pasavard-mcp` | `best_lists`, then `best_list`; `search_products` |
| Find a flat, used car or phone in ads, or check if an ad's price is fair | `divar-mcp` | `dv_search`, `dv_cheapest`, `dv_best_for_budget`, `dv_appraise` |
| Compare a phone or laptop across sellers, with installments | `technolife-mcp` | `tl_find_cheapest`, `tl_product`, `tl_compare` |
| Gadgets and accessories | `masterkala-mcp` | `mk_find_cheapest`, `mk_product` |
| Clothes, shoes, bags | `shopino-mcp` | `sh_find_cheapest`, `sh_product` |
| Cosmetics, skin and hair care, perfume | `khanoumi-mcp`, `asalbanoo-mcp` | `kh_find_cheapest`, `ab_find_cheapest` |
| Cheapest food delivered to an address | `snapp-mcp` | `find_location`, then `food_find_cheapest`, `food_party_deals` |
| Groceries delivered to an address | `snapp-mcp`, `okala-mcp` | `market_find_cheapest`; `ok_locate`, `ok_stores`, `ok_compare` |
| Flights, trains, buses, taxis | `mrbilit-mcp`, `flytoday-mcp` | `mb_search_flights`, `mb_flight_price_calendar`; `ft_search_flights` |
| Hotels | `mrbilit-mcp`, `flytoday-mcp` | `mb_search_hotels`; `ft_search_hotels` |
| Villas, cottages, short stays | `jabama-mcp`, `otaghak-mcp` | `jb_search_stays`, `jb_price_quote`; `ot_search_rooms`, `ot_price_quote` |
| Tours, events, theater tickets | `jabama-mcp` | `jb_search_tours`, `jb_search_events` |
| CIP, eSIM, visas, activities abroad | `flytoday-mcp` | `ft_cip`, `ft_esim_plans`, `ft_visa`, `ft_activities` |
| A doctor with a free appointment | `paziresh24-mcp`, `doctoreto-mcp` | `pz_search_doctors`, `pz_first_available`; `dt_search_doctors`, `dt_free_slots` |
| A doctor by name, or a doctor's clinic address, phone, hours and map | `exiryab-mcp` | `ey_search_doctors`; `ey_cities`, `ey_specialties` for exact names |
| Clinics, labs, medical offers | `doctoreto-mcp` | `dt_search_centers`, `dt_search_offers` |
| Ebooks and audiobooks | `taaghche-mcp`, `fidibo-mcp` | `tg_search`, `tg_free_books`; `fd_search`, `fd_free` |
| Printed books | `30book-mcp` | `sb_search`, `sb_book`, `sb_deals` |
| Merchant payments (user's own PayPing account) | `payping-mcp` | `payping_get_balance`, `payping_get_sales_summary` |
| User's own Bale bot | `bale-mcp` | `bot_get_new_messages`, `bot_send_message` |
| User's own crypto wallet: balances, history, swaps, withdrawals | `swapwallet-mcp` | `get_total_balance`, `get_transactions`; `request_swap`, then `get_action_request` |

For the best price, query every server in a category (all doctor servers, all travel servers) and compare.
Full tool list: [TOOLS.md](TOOLS.md). Machine-readable catalog with env vars: [servers.json](servers.json).

## Install

```bash
claude mcp add digikala -- uvx digikala-mcp          # Claude Code
```

```json
{ "mcpServers": { "digikala": { "command": "uvx", "args": ["digikala-mcp"] } } }
```

SwapWallet is hosted, so it is added by URL: `claude mcp add --transport http swapwallet https://swapwallet.app/mcp`.
Other clients take the URL in their own shape; its skill and its
[setup for each client](https://github.com/SwapWallet/swapwallet-mcp#connect) list them. The user then signs in with
OAuth, in the client: Claude Code doesn't open a browser by itself, so tell the user to run `/mcp`, pick the server
and choose Authenticate. Pasavard is hosted too, with no sign-in:
`claude mcp add --transport http pasavard https://pasavard.ir/api/mcp`.

As Claude Code plugins (MCP server plus a skill with usage rules), from the `iran-mcp` marketplace:

```bash
claude plugin install digikala --marketplace sepehr071/awesome-iran-mcp     # one server
claude plugin install iran-all --marketplace sepehr071/awesome-iran-mcp     # all read-only site servers
```

Bundles: `iran-all`, `iran-food`, `iran-shopping`, `iran-beauty`, `iran-travel`, `iran-health`, `iran-books`.
Skills only, for any agent: `npx skills add sepehr071/awesome-iran-mcp`.

The server key in config is the package name without `-mcp`. [`.mcp.json`](.mcp.json) holds all 23.
Requires [uv](https://docs.astral.sh/uv/) (`pasavard-mcp` and `swapwallet-mcp` don't). Add only the servers the task needs: each one adds 3 to 31 tools.

## Rules every server follows

- Prices are **Toman**. Convert before comparing with any Rial figure from elsewhere.
- Site servers are **read-only**: no login, basket, booking, order or payment. Hand the user the link to buy.
- `okala-mcp` has an optional OTP login (`ok_login`), read-only, only for text search. Ask the user first.
- `pasavard-mcp` store links are affiliate links: say so when you share one. `cashback_url` returns part of the
  commission after a one-time phone sign-in on pasavard.ir; `buy_url` goes straight to the store.
- `payping-mcp` (`PAYPING_TOKEN`) and `bale-mcp` (`BALE_BOT_TOKEN`) write to the user's own account.
  Confirm with the user before any `payping_create_*`, `payping_send_invoice`, `bot_send_*`, `bot_edit_message`
  or `bot_delete_message` call.
- `swapwallet-mcp` acts on the user's own SwapWallet account. Its `request_*` tools only file a request that the
  user approves or cancels in Telegram within 15 minutes: tell them so, then call `get_action_request`, and never say
  a swap, transfer or withdrawal happened before it reports `EXECUTED`. Confirm a crypto withdrawal's network and
  address with the user first. Its skill covers the rest, including the `MCP_TELEGRAM_NOT_LINKED` and
  `MCP_TWO_FACTOR_ACTIVE` errors.
- Package servers, on timeouts or HTTP 403 outside Iran: set the server's `<NAME>_MCP_PROXY` env var (names in
  `servers.json`).
- Package servers call undocumented site APIs that can change or rate-limit. Keep request rates low.
  `exiryab-mcp` uses ExirYab's public API, limited to 60 requests per minute per IP.
- `30book-mcp` is slow (2 to 5 s per list). `flytoday-mcp` searches are rate-limited per IP.

## Working on this repo

```
servers/<name>-mcp/   git submodule, one per server (own repo, own issues, own releases)
scripts/catalog.py    rebuilds servers.json, TOOLS.md, .mcp.json, plugins/ and .claude-plugin/ from the submodules
plugins/              one Claude Code plugin per server (MCP server + skill) and bundle plugins (generated)
.claude-plugin/       marketplace.json for the `iran-mcp` plugin marketplace (generated)
PLUGINS.md            plugin layout, agent compatibility, and how a server release reaches users
scripts/banner.py     redraws assets/banner.svg and assets/banner.fa.svg from servers.json
assets/               banners (generated)
README.md / README.fa.md   English (default) and Persian docs; keep both in sync
```

- Update servers: `git submodule update --init --remote && python scripts/catalog.py && python scripts/banner.py`,
  then commit the new pins and generated files.
- Never edit `servers.json`, `TOOLS.md`, `.mcp.json`, `plugins/`, `.claude-plugin/` or the banners by hand.
  Skill text comes from `skill()`, `USE` and `NOTES` in `scripts/catalog.py`, except the rules of a server whose repo
  ships its own `skills/<key>/SKILL.md`, which come from that file. Check with `claude plugin validate .`.
- Add a server: `git submodule add https://github.com/sepehr071/<name>-mcp servers/<name>-mcp`, add it to
  `SERVERS` in `scripts/catalog.py` (and to `GROUPS` in `scripts/banner.py` if its category is new), run both scripts, add a row to both
  READMEs and the table above. Update the 24 / 385 counts written in both READMEs.
- Add a hosted server: `git submodule add <its repo> servers/<name>-mcp` and an entry in `REMOTE` in
  `scripts/catalog.py`, then the same `GROUPS`, README, table and count steps. Its repo needs an MCP Registry
  `server.json` with `remotes` (name, version, description, repository), and the server must publish a server card
  at `<origin>/.well-known/mcp/server-card.json` with its `tools` (with annotations) and `authentication`.
  `catalog.py` reads the tools from the card, marks the server read-only only when it needs no sign-in and every tool
  is `readOnlyHint`, and stops on any sign-in other than OAuth.
- Code changes to a server belong in that server's repo. Inside one: `uv sync`, `uv run ruff check .`,
  `uv run pytest -q` (offline), `uv run pytest -m live -q` (real site).
- Release a server: bump `version` in its `pyproject.toml` and `server.json`, push a `v*` tag; CI publishes to
  PyPI, the MCP Registry and GitHub Releases.
