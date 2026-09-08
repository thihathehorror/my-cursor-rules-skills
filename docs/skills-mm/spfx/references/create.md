# Create SPFx Project

## CLI for Microsoft 365 ရှိကြောင်း စစ်

`m365 version` မောင်း။ Command fail (not found) ရင် globally install:

```
npm install -g @pnp/cli-microsoft365@latest --silent --no-fund --no-audit
```

## Environment check

Node / npm / prerequisites အတွက် `m365 spfx doctor`။ Node မကိုက်ရင် `fnm` သို့ `nvm` ရှာပြီး compatible version ပြောင်းကြည့်။ Node ပြောင်းပြီး `m365 spfx doctor` **ပြန်မောင်း** — Node version တိုင်း global packages သီးခြား၊ ရှိပြီး CLI for Microsoft 365 ပျောက်နိုင်။ Doctor က packages ပျောက်ဟု ပြရင် (ဥပမာ `yo`, `@microsoft/generator-sharepoint`) `npm install -g --silent --no-fund --no-audit` ဖြင့် globally install။ Version manager မရှိ၊ compatible Node မရှိ၊ သို့ အလိုအလျောက် မပြင်နိုင်သော errors ကျန်ရင် **ရပ်ပြီး user ကို ဘာပြင်ရမည် ပြော**။

## Scaffold the project

```
yo @microsoft/sharepoint --solution-name "<name>" --framework react --component-type webpart --component-name "<WebPartName>" --skip-install --no-insight
```

**Extension** အတွက် `--extension-type` ပေး (web parts မှာ ချန်):

```
yo @microsoft/sharepoint --solution-name "<name>" --component-type extension --extension-type ApplicationCustomizer --component-name "<Name>" --framework none --skip-install --no-insight
```

**Critical: အထက် flags ဖြင့် non-interactive mode အမြဲ။** Interactive mode (arrow-key) က agent terminals မှာ မယုံကြည်ရ၊ template မှားရွေး။ User တောင်းသည့်အတိုင်း flags ညှိ။

User က **legacy gulp** toolchain အတိအလင်း လိုမှသာ generator `--use-gulp`။

## Install dependencies

Generated project directory မှ `npm install --silent --no-fund --no-audit`။

## Packaging (user deploy လိုမှ)

`sharepoint/solution` ထဲ deployable `.sppkg` — ပရောဂျက် toolchain:

- Heft (v1.22+): `heft build --production` ပြီး `heft package-solution --production`
- gulp (≤ v1.21.1): `gulp bundle --ship` ပြီး `gulp package-solution --ship`
