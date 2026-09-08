---
name: spfx
description: >-
  [MM] SharePoint Framework (SPFx) development. Trigger: "create SPFx project",
  "new web part", "SPFx extension", "upgrade SPFx", "SPFx upgrade",
  "update SPFx version", "scaffold SPFx", "SPFx React", "SPFx design",
  "web part styling", "Fluent UI in SPFx", "PnPjs", "read SharePoint list",
  "call Microsoft Graph from SPFx". Yeoman create, CLI for Microsoft 365
  upgrade, gulp toolchain (ဤ repo: SPFx 1.20), React WP design, PnPjs data။
  ဤ repo ကို Heft သို့ migrate ရန် မသုံး။
argument-hint: 'Describe what you need: create, upgrade, design, or data access'
source: _cursor/skills/spfx/SKILL.md
---

# SPFx Development

User intent နဲ့ ကိုက်သော reference(s) ရွေး။ လိုအပ်သည် **သာ** loadပြီး steps တိကျ လိုက်နာ:

- **Project ဖန်** → [create.md](./references/create.md)
- **Project upgrade** → [upgrade.md](./references/upgrade.md)
- **React SPFx project UI** (components, styling, layout, accessibility) → [react-design.md](./references/react-design.md)။ **ဤ repo classic pages:** ထိုဖိုင်၏ Fluent v9 / host-theme rules အစား `classic-visual-parity` သုံး။
- **SharePoint / Microsoft Graph data ဖတ်/ရေး** → [pnpjs.md](./references/pnpjs.md)

## Global rules (SPFx task တိုင်း)

- **SharePoint နှင့် Microsoft Graph data operations အားလုံး default = PnPjs။** [pnpjs.md](./references/pnpjs.md)။ User အတိအလင်း တောင်းမှ သို့ dependency ထည့်မရမှသာ raw `SPHttpClient`/`MSGraphClientV3`။
- **`npm install` = synchronous + timeout အနည်းဆုံး ၃ မိနစ်။** SPFx dependency trees လေး။

## Toolchain decision rule

SPFx က v1.22.0 မှာ build system ပြောင်း။ `.yo-rc.json` (`@microsoft/generator-sharepoint.version`) သို့ `package.json` မှ version ဖတ်၊ ပြီး:

| Installed SPFx version | Toolchain |
| --- | --- |
| **v1.22.0 and newer** | **Heft** |
| **v1.0 – v1.21.1** | **gulp** (legacy) |

**ဤ repo:** SPFx **1.20 / gulp**။ Heft သို့ Fluent v9 **မupgrade**။ Heft skills ဤပရောဂျက်မှာ မရှိ — **မပြန်ဖန်**။
