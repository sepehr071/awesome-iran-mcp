# Changelog

## Unreleased

### Added

- **[exiryab-mcp](https://github.com/sshnevis/exiryab-mcp)**, ExirYab's official server, 3 tools: find a doctor by
  name, city and specialty, with clinics, phones, weekly hours and map links. Contributed by @sshnevis (#3).
- **[pasavard-mcp](https://github.com/ashkancapella/pasavard-mcp)**, Pasavard's official hosted server, 4 tools:
  Digikala and Snappshop prices tracked hourly, best picks per budget against each product's 30-day low. No sign-in.
  Its store links are affiliate links, and every result says so (#5).
- **[torob-mcp](https://github.com/sepehr071/torob-mcp)**, 26 tools: every Iranian shop's price for a product on
  Torob, price history, deal checks, installments and the cheapest shop for a whole basket.

### Changed

- The 18 unofficial shop servers present themselves as Chrome (TLS, HTTP/2 and headers), pace their calls, honour
  `Retry-After`, take a comma-separated proxy list and can clear a challenge page with an optional headless browser
  (`<package>[browser]`). On Torob the old client was blocked after 4-6 calls; the new one made 100 without a block.

### Fixed

- Bundle descriptions read as plain phrases: `iran-shopping` said "Everything for to buy electronics...".

## v1.5

The 19 package servers get leaner, safer and steadier, and Divar joins the catalog. Every server keeps its tool names
and parameters, and each one ships the changes as its next minor release.

### Added

- **[divar-mcp](https://github.com/sepehr071/divar-mcp)**, 31 tools for [Divar](https://divar.ir), Iran's largest
  classifieds site. It searches ads in any city (homes, cars, phones and more) with every filter of the category, and
  finds the cheapest and best-value ads. It compares ads, checks whether a price is fair against similar ads, shows
  market statistics by district and by day, and watches a search for new ads. It is read-only and needs no account.
- New banner: category tiles built from `servers.json`, so a new server no longer needs a logo in the banner.

### Fewer tokens

- About **62% fewer tokens per tool call** on average (median 57%, range 21% to 90%) across 181 live and fixture calls.
- The tool list (`list_tools`), paid once at the start of every session, is about **19% smaller** (11% to 30% by
  server).
- Each tool result is sent once, as compact JSON. It used to be sent twice: as indented JSON text and again as
  `structuredContent`. This alone saves roughly half of every response.
- Null, empty and duplicate fields are dropped, and so is `price` when it equals `final_price`. Zero or false defaults
  such as `discount_pct`, `free` and `available` are omitted too.
- Lower default result counts in many tools (for example `fd_search` 20 to 10, `food_menu` 100 to 30). The maximums
  are unchanged, so a higher `limit` returns the old amount.
- Long site text (reviews, descriptions, bios) is clipped at about 400 characters with a visible marker.
  `full_text=true` returns all of it.
- Shorter tool and parameter descriptions. Constraints, enums, one example and next-tool hints are kept.

| Server | `list_tools` tokens | Tool-call tokens |
|---|---|---|
| 30book-mcp | 4342 to 3195 (-26%) | -62% |
| asalbanoo-mcp | 4926 to 3931 (-20%) | -56% |
| bale-mcp | 3268 to 2537 (-22%) | -68% (mock) |
| digikala-mcp | 10256 to 8275 (-19%) | -61% |
| doctoreto-mcp | 7168 to 5926 (-17%) | -56% |
| fidibo-mcp | 4628 to 3566 (-23%) | -63% |
| flytoday-mcp | 10664 to 9039 (-15%) | -55% |
| jabama-mcp | 9743 to 8676 (-11%) | -58% |
| khanoumi-mcp | 5375 to 4261 (-21%) | -55% |
| masterkala-mcp | 4715 to 3618 (-23%) | -56% |
| mrbilit-mcp | 11792 to 10388 (-12%) | -56% |
| okala-mcp | 5970 to 4962 (-17%) | -64% |
| otaghak-mcp | 7484 to 6201 (-17%) | -61% |
| payping-mcp | 5773 to 4500 (-22%) | -70% (mock) |
| paziresh24-mcp | 5189 to 3982 (-23%) | -59% |
| shopino-mcp | 6567 to 5052 (-23%) | -57% (fixtures) |
| snapp-mcp | 7363 to 5523 (-25%) | -66% |
| taaghche-mcp | 5108 to 3593 (-30%) | -65% |
| technolife-mcp | 7389 to 5933 (-20%) | -57% |
| **All** | **127.7k to 103.2k (-19%)** | **832k to 320k (-62%)** |

Tokens were counted with `tiktoken` cl100k, an approximation of Claude's tokenizer, so read the ratios rather than the
absolute numbers. A typical flow (30book search, book, reviews, similar books) went from 20,074 to 7,194 tokens.

### Same answers

- Ranking and cheapest-price results match the previous release. In 106 of 111 ranking checks the top result was the
  same; the other 5 are site noise that the old code also shows against itself.
- Across 331 accuracy checks, every confirmed regression was fixed before release. Results that differ only because of
  a new default can be restored with a parameter.
- All `image` and `url` fields are kept.

### Security

- **30book:** search text and tag keys are escaped per path segment, so input such as `../login` can no longer reach
  other site paths. Response bodies are capped at 3 MB.
- **bale:** `bot_send_file` only sends files from allowed directories, set by `BALE_MCP_SEND_DIRS` (default: the
  download directory and the current directory). Downloads are capped at 20 MB. Tools that write files, mark messages
  read or wait for replies are no longer annotated read-only.
- **okala:** `ok_login` sends at most 3 SMS per hour across all numbers, and a race that let parallel calls pass the
  cap is fixed.
- Every server that returns site text tells the agent that reviews, descriptions and similar text are untrusted data,
  and clips long untrusted text.
- `pip-audit` found no known vulnerabilities where it was run. `mcp` is 2.3.0 and `httpx` 0.28.1 in every lock file.

### Performance and reliability

- Caches for repeat calls: cached calls are 6x to 11x faster in `30book`, and `tg_book` in `taaghche` went from 282 ms
  to 3 ms. First calls take about as long as before, because the site's own response time dominates.
- Independent requests run in parallel (for example `ok_deals`, `dt_free_slots`, `fd_author`, `mb_help`).
- Retries for transient failures on idempotent requests.
- Fixed: a `None` price crash and review paging in `masterkala`, a malformed `content-length` crash in `paziresh24`, a
  shared cache body in `snapp`, and a local fallback when sync fails in `bale`.

### Changes for callers

- No `structuredContent` and no `outputSchema`. Read `content[0].text`, which is compact JSON.
- Keys that used to be always present can be missing: nulls, `price` when it equals `final_price`, and zero or false
  defaults.
- Lower default result counts and clipped long text. In `30book`, `sb_book` returns `review_text` and `stats` only with
  `include_blurb=true`.
- `ok_store` lists only open slots unless `all_slots=true`, and `ok_stores` rows no longer carry `slot_from` and
  `slot_to`.
- `bot_send_file` refuses files outside the allowed directories.
- No tool was removed or renamed.

### Known limits

- Live checks were light or mocked where a site blocks or needs a token: Shopino, Bale and PayPing were checked with
  fixtures and mocks, and Flytoday and MrBilit with few live calls.
- Some failures seen on live sites also happen on the previous release: `fidibo` price-sort order, the `digikala` Fresh
  product redirect, two `flytoday` hotel tests, `mrbilit` train tests, the `okala` store-products sort and the
  `paziresh24` first-available check.
