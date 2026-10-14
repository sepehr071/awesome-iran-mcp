# Contributing

How pull requests to awesome-iran-mcp work: what goes where, the rules every PR follows, and the flow for adding
or updating a server. Commands and repo layout are in [AGENTS.md](AGENTS.md); how plugins are built and released is
in [PLUGINS.md](PLUGINS.md).

## Where a change goes

| Change | Where |
|---|---|
| A bug, new tool or behaviour change in a server | That server's own repo (`servers/<name>-mcp` is a submodule) |
| A new server in the list | A PR here (flow below) |
| A new version of a server | A release in the server's repo, then the pin moves here |
| Catalog, banner or plugin generation | A PR here, in `scripts/` |
| Docs | A PR here; change `README.md` and `README.fa.md` together |

## Rules

### Every PR

- One topic per PR. Adding a server and changing `scripts/` for an unrelated reason are two PRs.
- Never edit generated files by hand: `servers.json`, `TOOLS.md`, `.mcp.json`, `plugins/`, `.claude-plugin/`,
  `assets/banner.svg`, `assets/banner.fa.svg`, `assets/social.svg`. Change the source (`scripts/catalog.py`,
  `scripts/banner.py`, or the server's repo) and rerun the scripts.
- Rerun both scripts and commit what they produce, so the PR matches a clean rebuild:
  `python scripts/catalog.py && python scripts/banner.py`. Install `fonttools==4.66.1 brotli==1.2.0` first (the
  versions the nightly sync uses); other versions re-encode the banner fonts and make the diff noisy.
- `claude plugin validate .` passes.
- `README.md` and `README.fa.md` say the same thing. The server and tool counts in both READMEs, `AGENTS.md` and
  `llms.txt` match `servers.json` (`catalog.py` updates most of them; check the rest).
- Commit messages follow Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`).
- No secrets, tokens or personal data in code, tests, fixtures or screenshots.

### Every server

- **Read-only for sites.** No login, basket, booking, order or payment. The tools hand the user a link to finish on
  the site. A server that writes to the user's own account (like `payping-mcp`, `bale-mcp`) needs that account's
  token as a required env var, and its skill tells the agent to confirm before every write.
- **Prices in Toman.** Convert Rial before returning it.
- **Python package on PyPI**, run with `uvx <name>-mcp`, MIT licence.
- **Tools** use the `@tool("Title")` decorator from the server's `registry.py`, with a short prefix
  (`dk_`, `ey_`, ...). The first docstring line is the one-line summary `catalog.py` puts in `TOOLS.md` and the skill,
  so make it stand alone. Mark tools with `read_only_hint` when they are read-only.
- **Proxy.** Ignore system proxy settings and read an optional `<NAME>_MCP_PROXY` env var, so users outside Iran can
  route through an Iranian IP.
- **Gentle on the site.** Cap concurrency, retry at most once, and turn HTTP errors into messages the model can act
  on (rate limits say to wait).
- **Tests.** Offline tests with a mocked transport run by default; tests against the real site are marked `live`
  and excluded by default (`addopts = "-m 'not live'"`). `uv run ruff check .`, `uv run pytest -q` and
  `uv run pytest -m live -q` all pass.
- **Metadata.** An MCP Registry `server.json` (name, title, description, version, package, env vars) whose
  `version` matches `pyproject.toml`, and `<!-- mcp-name: <registry name> -->` in the README.
- **Releases** come from a `v*` tag through CI: PyPI trusted publishing (with provenance attestations), the MCP
  Registry and a GitHub Release. No releases uploaded by hand.
- **Skill (optional).** A repo that ships `skills/<key>/SKILL.md` replaces the generated rules with its own. It must
  still say the server is read-only (or what it writes, and to confirm first) and give its rate limits.

### Servers this repo doesn't own

Any server whose repo is not under `sepehr071`: community servers, and official servers run by the site itself.
The code ships to users of this repo, so the maintainer reviews every version before it reaches them.

- **The submodule points to a fork under `sepehr071`,** never to the author's repo. The maintainer creates the fork
  (`sepehr071/<name>-mcp`); the PR sets `.gitmodules` to `https://github.com/sepehr071/<name>-mcp.git`. The author
  keeps their repo and PyPI package and keeps releasing as usual.
- **The fork moves only after review.** The nightly sync follows the fork's `main`, so nothing new arrives until the
  maintainer syncs the fork. Never click "Sync fork" without reading the upstream diff.
- **Every version is pinned.** Plugins and `.mcp.json` run `uvx <package>@<version>`, taken from the fork's
  `server.json`. A PyPI version cannot be replaced once published, so the pin is the code that was reviewed.
- **Provenance is required.** The release on PyPI must carry a trusted-publishing attestation that points to the
  reviewed tag in the author's repo. A release without one is not pinned.
- **The version must exist on PyPI** before the fork moves to it. Otherwise `catalog.py` stops, instead of falling
  back to the author's newest release.
- **An official server says so** in its `server.json` description, and the site links the repo (for example in its
  `llms.txt`). The maintainer checks both.

### Hosted servers

A server the site runs itself (like `swapwallet-mcp`), added by URL. Everything above that applies to a repo
applies here too, plus:

- Its repo has an MCP Registry `server.json` with `remotes`.
- The server publishes a server card at `<origin>/.well-known/mcp/server-card.json`, with its `tools` (with
  annotations) and `authentication`. `catalog.py` reads the tools from the card.
- Sign-in is OAuth or none. `catalog.py` stops on anything else.
- Every tool that changes something is approved by the user outside the agent, or the skill tells the agent to
  confirm first.

## Flow: add a package server

1. **Build and release the server** in its own repo, following the rules above. Tag `v0.1.0` and let CI publish it.
2. **Open an issue here** with the repo, the PyPI link and what the server does. If the repo is not under
   `sepehr071`, the maintainer forks it and replies with the fork URL.
3. **Branch** from `main` in your fork of this repo.
4. **Add the submodule:**
   `git submodule add https://github.com/sepehr071/<name>-mcp.git servers/<name>-mcp`
5. **Register it:**
   - `SERVERS` in `scripts/catalog.py`: `"<name>-mcp": ("<category>", "<site url>")`, next to its category.
   - `APPS` in `scripts/banner.py`: English name, Persian name, logo file, padding.
   - The logo in `assets/logos/<name>.png` (square, at least 128 px).
6. **Regenerate:** `python scripts/catalog.py && python scripts/banner.py`.
7. **Docs:**
   - A row in the server's category table in both `README.md` and `README.fa.md`.
   - A row in the "Pick a server" table in `AGENTS.md`, and any rule the server adds to "Rules every server follows".
   - A line in `llms.txt`.
   - Check that every server and tool count changed.
8. **Check:** `claude plugin validate .`, and look at the banners (the logo grid must still fit the panel).
9. **Open the PR** with the template filled in.

## Flow: add a hosted server

Same as above, except step 4 adds the server's repo (through the fork if it isn't under `sepehr071`), and step 5
adds it to `REMOTE` instead of `SERVERS` in `scripts/catalog.py`. The server card must be live before the PR,
because `catalog.py` reads it.

## Flow: release a new version of a server

1. In the server's repo: bump `version` in `pyproject.toml` and `server.json`, merge, push a `v*` tag. CI publishes
   to PyPI, the MCP Registry and GitHub Releases.
2. **Servers under `sepehr071`:** nothing else to do. The nightly sync moves the submodule, regenerates the catalog
   and plugins, and commits.
3. **Servers this repo doesn't own:** open an issue here with the new version. The maintainer reviews the upstream
   diff, checks the PyPI attestation, syncs the fork, and the nightly sync picks it up.

## Review

The maintainer checks every PR for:

- **A clean rebuild:** rerunning both scripts on the PR branch changes nothing.
- **`claude plugin validate .`** passes.
- **The server's own checks:** `ruff`, offline tests and live tests pass in the submodule at the pinned commit.
- **The code:** read-only (or confirmed writes), no hidden network calls, no secrets, sane error handling.
- **Release:** the pinned version is on PyPI with provenance, and is in the MCP Registry.
- **Ownership:** the submodule points to a `sepehr071` repo, and an official claim is backed by the site.
- **Wording:** generated skill text and bundle descriptions don't promise what the server can't do.
- **Docs:** both READMEs are in sync, and the counts match `servers.json`.

A PR that fails any of these gets "Request changes" with the list. Push fixes to the same branch; there's no need
for a new PR.
