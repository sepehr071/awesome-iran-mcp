## Summary

<!-- What this PR does, in a few lines. For a new server: its repo, PyPI link, tool count, and what it's for. -->

## Type

- [ ] New package server
- [ ] New hosted server
- [ ] Server version bump (servers this repo doesn't own)
- [ ] Scripts (`scripts/catalog.py`, `scripts/banner.py`)
- [ ] Docs

## Checklist

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the rules behind each item.

**Every PR**
- [ ] Generated files were not edited by hand; `python scripts/catalog.py && python scripts/banner.py` was rerun
      (with `fonttools==4.66.1 brotli==1.2.0`) and its output is committed
- [ ] `claude plugin validate .` passes
- [ ] `README.md` and `README.fa.md` say the same thing; counts match `servers.json`

**New server or version bump**
- [ ] In the server repo: `uv run ruff check .`, `uv run pytest -q` and `uv run pytest -m live -q` pass
- [ ] Read-only for sites (no login, basket, booking, order or payment), or every write is confirmed with the user
- [ ] Prices in Toman; optional `<NAME>_MCP_PROXY` env var supported
- [ ] Released from a `v*` tag by CI: on PyPI with trusted-publishing provenance, and in the MCP Registry
- [ ] Submodule URL is a `sepehr071` repo (the maintainer's fork if the server isn't ours)
- [ ] Added to `SERVERS` or `REMOTE` in `scripts/catalog.py` and `APPS` in `scripts/banner.py`, with a logo in `assets/logos/`
- [ ] Rows added in both READMEs, `AGENTS.md` ("Pick a server") and `llms.txt`
- [ ] Banners checked: the logo grid fits the panel

**Hosted server**
- [ ] Server card live at `<origin>/.well-known/mcp/server-card.json`, with tool annotations and `authentication`
- [ ] Sign-in is OAuth or none

## Test plan

<!-- Commands you ran and what they printed, e.g. "catalog.py: 21 servers, 324 tools". -->
