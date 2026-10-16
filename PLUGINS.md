# Plugins, skills and the update flow

How the `iran-mcp` plugin marketplace is built, which agents can use it, and what happens when a server changes.

## What gets generated

`python scripts/catalog.py` writes everything below from the submodules in `servers/` (and, for a hosted server, the server card it publishes). Never edit these by hand.

```
.claude-plugin/marketplace.json        the `iran-mcp` marketplace: one entry per plugin
plugins/<name>/                        one plugin per server (22)
  .claude-plugin/plugin.json           manifest: version + the MCP server, pinned to that version
  skills/<name>/SKILL.md               when to use the server, its tools, its rules
plugins/iran-<bundle>/                 bundles (7): a manifest with `dependencies` and nothing else
  .claude-plugin/plugin.json
```

- `<name>` is the package name without `-mcp` (`digikala`, `30book`, ...).
- A server plugin's `version` is the server's release on PyPI. Its MCP server runs `uvx <package>@<version>`.
  A hosted server's plugin (`swapwallet`) points its MCP server at the URL and takes `version` from the
  `server.json` in its repo.
- Bundles are `iran-all` (every read-only site server) plus one per category with two or more servers:
  `iran-food`, `iran-shopping`, `iran-beauty`, `iran-travel`, `iran-health`, `iran-books`. `payping`, `bale` and
  `swapwallet` act on the user's own account, so no bundle includes them.
- Bundles have no `version`. Claude Code then versions them by git commit, so a changed member list reaches users.
- Skill text comes from `skill()`, `USE` and `NOTES` in `scripts/catalog.py`. Tool lists come from the server code,
  or a hosted server's card. A server whose repo ships `skills/<key>/SKILL.md` (`swapwallet`) keeps its own rules: they
  replace the generated ones, so the skill here and the one in its own plugin say the same thing. SwapWallet's
  `swapwallet@swapwallet` plugin runs the same server, so users install one of the two.

Check after every change:

```bash
python scripts/catalog.py
claude plugin validate .            # must end with "Validation passed" (bundle "no version" warnings are expected)
```

## Compatibility

Skills are the portable part: every agent below reads `SKILL.md`. The MCP server and the bundles depend on the
agent's plugin system.

| Agent | Install | Skill | MCP server | Bundles | Status |
|---|---|---|---|---|---|
| Claude Code (CLI, desktop, VS Code) | `claude plugin install <name> --marketplace sepehr071/awesome-iran-mcp` | yes | yes | yes | Tested |
| Grok Build | `grok plugin marketplace add sepehr071/awesome-iran-mcp`, then `grok plugin install <name>@<marketplace> --trust` | yes | detected | no | Tested (grok 1.0.45) |
| GitHub Copilot CLI | `copilot plugin marketplace add sepehr071/awesome-iran-mcp`, then `copilot plugin install <name>@iran-mcp` | likely | likely | unknown | Docs only |
| Codex CLI | `npx skills add sepehr071/awesome-iran-mcp -a codex` + MCP config | yes | manual | no | Docs only |
| Cursor | `npx skills add ... -a cursor` + MCP config | yes | manual | no | Docs only |
| Antigravity (IDE and CLI) | `npx skills add ... -a antigravity` (or `-a antigravity-cli`) + `mcp_config.json` | yes | manual | no | Docs only |
| Gemini CLI, OpenCode, Windsurf, Cline, ~60 more | `npx skills add sepehr071/awesome-iran-mcp` (pick skills and agents) | yes | manual | no | Tested (skill discovery only) |

Notes:

- **Grok Build** reads `.claude-plugin/marketplace.json` as is. A marketplace added from a local path registers
  under the folder name (`awesome-iran-mcp`), not `iran-mcp`. Run `grok plugin marketplace list` to see the name.
  It installs a single plugin with its skill and MCP server. It ignores `dependencies`, so a bundle installs alone,
  without its members.
- **Copilot CLI** reads `.claude-plugin/marketplace.json` according to GitHub's docs. It supports relative-path
  sources and kebab-case names, which this marketplace uses. Not tested here.
- **Codex CLI** has its own marketplace (`.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json`). Third-party
  reports say it also reads the Claude marketplace for skills, but it registers MCP servers only from a Codex
  manifest. Unverified. Until a Codex manifest is generated, use `npx skills` plus the MCP config.
- **Cursor** reads `.cursor-plugin/marketplace.json` only. Not generated yet.
- **Manual MCP config**: every skill states the command for its server, for example
  `"digikala": {"command": "uvx", "args": ["digikala-mcp"]}`. Antigravity keeps it in `mcp_config.json`
  (`~/.gemini/antigravity/` or `.agents/` in a project). Codex keeps it in `~/.codex/config.toml`
  (`codex mcp add digikala -- uvx digikala-mcp`). Cursor keeps it in `~/.cursor/mcp.json`.
  A hosted server (`swapwallet`) is added by URL instead, in a shape that differs per client (`serverUrl` in
  Windsurf, `codex mcp add swapwallet --url ...`, Settings → Connectors in Claude Desktop). Its skill lists each one.

Native manifests for Codex (`.agents/plugins/`, `.codex-plugin/`) and Cursor (`.cursor-plugin/`) can be generated
by `catalog.py` the same way, if those agents need one-command installs.

## When a server changes in its own repo

The chain from a commit in a server repo to a user's machine:

1. **Server repo**: you push to `main`. To release, bump `version` in `pyproject.toml` and `server.json`, then push a
   `v*` tag. CI publishes to PyPI, the MCP Registry and GitHub Releases.
2. **This repo, nightly** (`.github/workflows/sync.yml`, 03:17 UTC, or run it by hand from the Actions tab):
   `git submodule update --remote` moves every submodule to its latest `main`. Then `catalog.py` and `banner.py`
   regenerate everything, and the bot commits `chore: sync servers to latest` if anything changed.
3. **Generated plugin**: `plugin.json` gets the new `version` and `uvx <package>@<version>`. `SKILL.md` gets the
   new tool list.
4. **User's machine**: Claude Code sees a new plugin version and installs it. The next session starts
   `uvx <package>@<version>`, and uv downloads that release once.

### What each kind of change does

| Change in the server repo | Plugin version | What users get |
|---|---|---|
| Commits on `main`, no release | unchanged | Existing installs: nothing, the plugin still pins the last release. New installs copy the current `SKILL.md`, whose tool list follows `main`, so it can name a tool the pinned release doesn't have yet. Release soon after adding tools |
| Release (version bump + tag, published to PyPI) | new | The new server and the new skill, at their next plugin update |
| Version bumped on `main` but not on PyPI yet | unchanged | Nothing breaks. `released()` falls back to the newest version on PyPI. The next sync after the publish picks up the new version |
| New or renamed tool | with the release | The skill lists it after the release. A renamed tool breaks anything that called the old name |
| New or renamed env var in `server.json` | with the release | Required vars are passed through as `${VAR:-}`. Optional ones (like the proxy) are read from the user's environment |
| Hosted server: new tools on the server, or a new `server.json` | new if `server.json`'s `version` changed | The new skill at their next plugin update; without a version bump, existing installs keep the old one. The server itself changes whenever its owner deploys it |

### Changes in this repo

| Change | What to do | What users get |
|---|---|---|
| Skill wording (`skill()`, `USE`, `NOTES`) | Run `catalog.py`, commit | Server plugins keep their version, so users only get it with the next server release. To push it sooner, release a patch of that server |
| Bundle membership (new server, new category) | Run `catalog.py`, commit | New bundle version. Users get the added plugins at their next update |
| New server | See "Add a server" in `AGENTS.md`. `catalog.py` adds its plugin and bundle membership | A new plugin in `/plugin` Discover. Bundles pick it up at the next update |
| Removed server | Remove it from `SERVERS`, run `catalog.py` | The plugin disappears from the marketplace. Installed copies stay on users' machines until they uninstall it |

### How users receive updates

Claude Code's auto-update is off by default for third-party marketplaces like this one. Users choose one of these:

- **Turn on auto-update once**: `/plugin`, then the **Marketplaces** tab, then `iran-mcp`, then **Enable auto-update**.
  New versions install in the background and load in the next session.
- **Update by hand**: in `/plugin`, open the **Marketplaces** tab, select `iran-mcp` and choose **Update marketplace**.
  From a shell, run `claude plugin update digikala@iran-mcp`. Then start a new session or run `/reload-plugins`.
- **Grok Build**: `grok plugin marketplace update`, then `grok plugin update`.

### Why the version is pinned

Bare `uvx digikala-mcp` downloads the newest release on first use and then keeps running that cached copy. It does
not upgrade on its own (see the uv docs on tools). Pinning `digikala-mcp@<version>` in the plugin makes the plugin
version and the server version move together. A plugin update is then a server update. `.mcp.json` pins the same
versions, so pulling this repo updates it too. For a server whose repo isn't under `sepehr071`, `catalog.py` pins
only a release that is on PyPI and never falls back to a newer, unreviewed one ([CONTRIBUTING.md](CONTRIBUTING.md)).

People who added a server without the plugin (`claude mcp add ... -- uvx digikala-mcp`, `npx skills`
plus a manual config) stay on their cached copy. To upgrade, they run `uvx digikala-mcp@latest --help` once (or
`uv cache clean digikala-mcp`) and restart the client.

## Release checklist for a server

1. In the server repo: `uv run ruff check .`, `uv run pytest -q`, `uv run pytest -m live -q`.
2. Bump `version` in `pyproject.toml` and `server.json`. Commit, push, tag `v<version>`, push the tag.
3. Wait for the server's release CI to publish on PyPI.
4. Here: run the Sync workflow by hand, or wait for the nightly run. Locally:
   `git submodule update --init --remote && python scripts/catalog.py && python scripts/banner.py`.
5. `claude plugin validate .`, then commit the new pins and generated files.
6. Optional smoke test with a throwaway config, so your own settings stay untouched:

   ```bash
   export CLAUDE_CONFIG_DIR=$(mktemp -d)
   claude plugin marketplace add ./
   claude plugin install digikala@iran-mcp
   claude mcp list | grep plugin:          # expect "✔ Connected"
   ```
