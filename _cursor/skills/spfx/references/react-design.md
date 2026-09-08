# React SPFx Design Guidelines — Copilot UI Contract v2.1

(Fluent UI v9 + SharePoint + Host Awareness)

**ဤ repo ခြွင်းချက် (အောက် MUST တိုင်းကို နိုင်):** DBS-FFW-classicsite → SPFx page UI = **visual clone**။ `classic-visual-parity` load။ ထို pages မှာ Fluent v9, host-theme colors, “MUST NOT hardcode colors” **မသုံး**။ Project pin = Fluent **v8** + classic `style.css` / `sass/` values။ Classic ကိုက် custom HTML/CSS required။ ဤဖိုင်၏ Fluent-default rules = classic clone **မဟုတ်**သော generic SPFx UI သာ။

Fluent UI v9 နဲ့ ကိုက်ညီ၊ SharePoint experiences နဲ့ ညှိ၊ host environments ကြား လိုက်လျောသော UI ထုတ်ရန် normative guidance။

## 1. Scope

ထုတ်သော UI အမျိုးအစား:

- primitive (button, input, badge)
- composite (toolbar, card, feed item)
- assembly (feed, dashboard section, form)
- template (full page သို့ multi-region flow)

Agents က request တိုင်း full-page experience ဟု **မယူဆရ**။

### Classic clone (ဤ repo) — Fluent visual rules ကျော်

Task = DBS-FFW-classicsite classic page / chrome UI ဆို:

- Sections 2–6, 8, 12 (Fluent v9, host theme, no hardcoded colors, Fluent defaults) **မသုံး**။
- Section 10 a11y (keyboard, focus, names) **သုံး** — classic type, color, spacing, hover, animation **မပြောင်း**။
- Classic markup ကို custom HTML/CSS ပြန်ဖန် **လိုအပ်** — “MUST NOT recreate Fluent with custom HTML/CSS” ဤနေရာ **မသက်ရောက်**။

## 2. Platform

Generated UI MUST သုံး:

- React
- TypeScript
- SPFx-compatible patterns
- @fluentui/react-components
- @fluentui/react-icons

Agents MUST NOT Fluent components ကို custom HTML/CSS ဖြင့် ပြန်ဖန်။

Import မတိုင်မီ ပရောဂျက် `package.json` မှ Fluent UI version အတည်ပြု။ Installed SPFx နဲ့ ကိုက် version သုံး; ပရောဂျက် မကြေညာသော version မယူဆ။

## 3. Core Rules

- ရရှိနိုင်လျှင် Fluent UI v9 components MUST သုံး
- Custom UI မတိုင်မီ Fluent primitives မှ compose MUST
- Accessible, responsive output MUST
- Output minimal + implementation-ready SHOULD
- လိုအပ်မှ small custom styling MAY

## 4. Theme and Host Precedence

အစဉ်:

1. Accessibility and legibility
2. Host surface integration
3. SharePoint alignment
4. Brand expression via tokens

- Host မှ theme, colors, typography inherit MUST
- Colors သို့ surfaces hardcode MUST NOT
- Neutral, adaptive surfaces SHOULD

## 5. Theme Application

Generated UI MUST theme integration ပြ။

- Theming သက်ဆိုင်ရင် FluentProvider MUST
- Theme-aware tokens MUST (fixed colors မဟုတ်)
- Theme ကို props သို့ context မှ လက်ခံ SHOULD
- Host theme မရှိရင် Fluent defaults fallback MUST

## 6. SharePoint Alignment

- ရှိလျှင် SharePoint themes လေးစား MUST
- Zones, columns, dynamic width လိုက် MUST
- Patterns: cards, lists, panels, sections SHOULD
- Specified မဟုတ်လျှင် app-shell layout မယူဆ MUST NOT

## 7. Container Context Rules

Agents MUST context ခန့်မှန်း။

### Inline / Conversational

- Single-column layout MUST
- Scannability ဦးစားပေး MUST
- Hover-only interactions မယုံ MUST NOT
- Dense toolbars/forms ရှောင် SHOULD

### Embedded / Web Part

- Constrained width ယူဆ MUST
- Compact density MUST
- Padding နှင့် elevation လျှော့ MUST
- Vertical layouts ဦးစားပေး SHOULD
- Zones ကြား သန့်စင် resize MUST

### Full Page

- Multi-column layouts MAY
- ပိုခိုင် hierarchy MAY

## 8. Component Composition Rules

- Fluent subcomponents (ဥပမာ CardHeader) MUST
- Component anatomy လက်ဖြင့် ပြန်ဖန် MUST NOT
- Proper Text hierarchy (size/weight) MUST
- Arbitrary spacing ရှောင် MUST

## 9. Interaction Consistency

- Interaction states တသမတ် (hover/active/focus) MUST
- Icon variants သင့် (filled vs regular) SHOULD
- Inconsistent icon styles မရော MUST NOT

## 10. Accessibility

- Semantic structure MUST
- Keyboard navigation MUST
- Labels/accessible names MUST
- Tab order ထိန်း MUST
- Overlays အတွက် focus စီမံ MUST
- Loading/empty/error states ပြ MUST

## 11. Performance

- Lightweight composition SHOULD
- Excessive nesting ရှောင် SHOULD
- အကြောင်းမရှိ heavy components ရှောင် SHOULD

## 12. Styling

- Fluent defaults ဦးစားပေး MUST
- Fixed widths မယူဆ MUST NOT
- Narrow views မှာ readability ထိန်း MUST
- Theme tokens SHOULD

## 13. Anti-Patterns

Agents MUST NOT:

- Fluent components လက်ဖြင့် ပြန်ဖန်
- Embedded contexts မှာ full-screen layouts ယူဆ
- Custom color systems သုံး
- Elevation အလွန်အကျွံ
- ကျဉ်းသော နေရာမှာ dense multi-column layouts
- Hover-only affordances ယုံ

## 14. Output

Generated output MUST:

- React + TypeScript
- Fluent UI v9-based
- Readable နှင့် implementation-ready

## 15. Data Access

- SharePoint သို့ Microsoft Graph data မဆို default **PnPjs** MUST — [pnpjs.md](./pnpjs.md)။
- Data calls = service သို့ hook — render ထဲ NEVER MUST။
- Async data တိုင်း loading, empty, error states ပြ MUST။

## 16. Validation

UI ပြောင်းပြီး `npm run build` MUST မောင်း၊ errors အားလုံး ပြင်၊ ပြီး workbench smoke-test (`heft start` on SPFx v1.22+, `gulp serve` on legacy — [toolchain.md](./toolchain.md))။
