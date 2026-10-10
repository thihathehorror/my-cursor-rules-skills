# my-rules-skills-and-others

Gold-standard Cursor agent pack — synced from **DBS-FFW** (2026-08-31), plus Codegraph ensure/autosync hooks.

## Purpose

- **Reference** when upgrading other classic → SPFx migration projects
- **Copy source** for `.cursor/` rules, skills, hooks, MCP, and migration docs
- Includes live `active_context.md`, `progress.md`, and `docs/migration/` from DBS-FFW so you can re-read the full handoff example

## Contents

| Path | Description |
|------|-------------|
| `.cursor/rules/` | 15 active rules (+ archived dead stacks) |
| `.cursor/skills/` | 17 skills (Myanmar prose; `name` / paths / Status tokens stay English) |
| `.cursor/hooks/` | SoT sessionStart · ensure-codegraph · codegraph-autosync · preCompact · stop handoff |
| `.cursor/hooks.json` | Hook event wiring (`sessionStart`, `afterFileEdit`, `preCompact`, `stop`) |
| `.cursor/mcp.json` | Codegraph MCP (`codegraph` + `${workspaceFolder}`) |
| `.codegraph/.gitignore` | Keep index local — do not commit `codegraph.db` |
| `active_context.md` | DBS-FFW handoff example (Goal · Pins · DONE · NEXT · paste block) |
| `progress.md` | DBS-FFW slice inventory + suggested order |
| `codegraph.json` | DBS-FFW index excludes (retarget per project) |
| `docs/migration/` | PARITY · SITEASSETS · SITE_CHROME templates |
| `docs/rules-mm/` | Myanmar translation of `.cursor/rules/` (docs only) |
| `docs/skills-mm/` | Myanmar docs mirror of `.cursor/skills/` (`source:` frontmatter; not a second copy source) |

## Pins (all classic → SPFx projects)

| Item | Value |
|------|--------|
| SPFx | 1.20.x |
| Toolchain | gulp (not Heft) |
| React | 17 |
| UI | Fluent UI v8 |
| Reject | Heft/v9, classic master, secrets in chat |

## Codegraph hooks

| Hook | When | Role |
|------|------|------|
| `ensure-codegraph.sh` | `sessionStart` | `codegraph init` if `.codegraph/codegraph.db` missing (fail-open) |
| `codegraph-autosync.py` | `sessionStart` + `afterFileEdit` | Quiet `codegraph sync -q` (debounced, fail-open) |

- Sync root defaults to **workspace root** (uses root `codegraph.json` excludes).
- Optional: `CODEGRAPH_SYNC_ROOTS=DBS-FFW-SPFX,Other-SPFX` for multi-root sync.
- This pack repo itself has little/no app source — real index DB appears after deploy + `codegraph` CLI on a target project.

## Deploy to a new project

1. Copy pack into project root:
   ```bash
   cp -R my-cursor-rules-skills/.cursor/ /path/to/PROJECT/.cursor/
   cp my-cursor-rules-skills/codegraph.json /path/to/PROJECT/
   mkdir -p /path/to/PROJECT/.codegraph && cp my-cursor-rules-skills/.codegraph/.gitignore /path/to/PROJECT/.codegraph/
   ```
2. **Retarget paths** in rules `06`, `07`, `15`–`19`, `12` and skills (`classic-to-spfx-migration`, `classic-visual-parity`, etc.)
3. Copy `docs/migration/` and rewrite `PARITY.md` for that site's routes
4. Create project-specific `active_context.md` + `progress.md` (use DBS-FFW files here as format reference)
5. Adjust `codegraph.json` `exclude` for `{PROJECT}-classicsite/` and `{PROJECT}-SPFX/`
6. Ensure `codegraph` CLI is on PATH; open the project in Cursor — `ensure-codegraph` + autosync will init/sync, or run `codegraph init` once manually

## Active rules (15)

| Rule | Role |
|------|------|
| `00-core-fsm` | Mode A/B, scenarios, safety, deps gate |
| `01-react-standards` | React/TSX (glob) |
| `04-sharepoint-standards` | ASPX/master (glob) |
| `06-surface-quality` | SEO/UI/A11y + classic px exception (glob) |
| `07-testing-gate` | gulp test smoke (glob) |
| `08-chain-steps` | `..chain` STEP format (Mode B) |
| `11-active-rules-report` | Mode B chrome only |
| `12-codegraph` | Need/Skip policy (on-demand) |
| `13-context-handoff` | `active_context.md` / `progress.md` SoT |
| `14-security-appsec` | OWASP, secrets |
| `15-js-code-quality` | Classic JS (glob) |
| `16-landing-page-image-quality` | Image quality (glob) |
| `17-classic-host-and-assets` | One WP per page, no hub router |
| `18-bulk-migration-baseline` | Bulk wired/baseline wave (glob) |
| `19-migration-skill-auto-invoke` | Prompt → skill routing (always-on) |

Archived (inactive): WordPress, Laravel, FastAPI, Flutter, Express → `.cursor/rules/archive/`

## Sync source

Last synced from: `DBS-FFW/.cursor/` + root memory files + `docs/`

To refresh this pack from DBS-FFW, re-run the same rsync/cp steps or ask the agent to re-sync.
