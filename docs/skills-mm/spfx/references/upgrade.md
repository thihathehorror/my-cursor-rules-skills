# Upgrade SPFx Project

## CLI for Microsoft 365 ရှိကြောင်း စစ်

`m365 version` မောင်း။ Command fail (not found) ရင် globally install:

```
npm install -g @pnp/cli-microsoft365@latest --silent --no-fund --no-audit
```

## မစမီ

1. **Git state သန့် + committed။** Upgrade က ဖိုင်များစွာ ပြန်ရေး; user က diff ကြည့် / roll back ရန် baseline လို။ Working tree dirty ရင် commit သို့ stash အရင်တောင်း။
2. **လက်ရှိ version ရှာ။** `.yo-rc.json` (`@microsoft/generator-sharepoint.version`) နှင့် `package.json` ထဲ `@microsoft/sp-*` ဖတ်။ ဘာမှ မမောင်းမီ current + target versions ကြေညာ။
3. **Target version အတွက် Node/TypeScript compatibility စစ်။** SPFx version တိုင်း Node range သီးခြား။ Installed Node က target range ပြင်ပဆို build fail — အရင်ပြ (`မသေချာရင် m365 spfx doctor`)။

## Upgrade မောင်း

SPFx project root မှ CLI for Microsoft 365:

- User က target version ပေးရင်:
  ```
  m365 spfx project upgrade --toVersion <version> --output md
  ```
- Version မပေးရင် (latest supported):
  ```
  m365 spfx project upgrade --output md
  ```

## Upgrade apply

Generated report ဖတ်ပြီး စာရင်းအစဉ်အတိုင်း steps **အားလုံး** apply။ Report = file modifications, package version changes, configuration updates။ Sequential — order အရေးကြီး။ Step က customized ဖိုင်ပစ်မှတ်ထားရင် overwrite မဟုတ် merge သတိ။

## Verify

1. Dependencies ပြင်ရန် `npm install --silent --no-fund --no-audit`။
2. `npm run build` မောင်း — error တိုင်း ပြင်; build သန့်မှ upgrade ပြီး။
3. Build errors အဖြစ် ပေါ်သော **deprecated / removed APIs** ပြင်။
4. User ကို serve ခိုင်း (`heft start` on v1.22+, `gulp serve` on legacy), workbench smoke-test, commit မတိုင်မီ git diff ကြည့်ခိုင်း။
