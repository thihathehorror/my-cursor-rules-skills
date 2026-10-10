---
name: spfx-enterprise-design-core
description: >-
  [MM] SPFx web parts/extensions core design guidance။ Layout, hierarchy,
  commanding, text, empty states, responsive — SPFx UX တည်ဆောက်/review သည့်အခါ။
---

# SPFx Enterprise Design Core

**SPFx UX ဒီဇိုင်း သို့ review** လုပ်သည့်အခါ သုံး — repo တစ်ခုတည်းမဟုတ်။ SharePoint web parts/extensions အတွက် Microsoft guidance encode — AI editor က **consistent, accessible, performant** UX အကြံပေးနိုင်ရန်။

Key MS references (လိုမှသာ ဖတ်):
- Web part design overview: https://learn.microsoft.com/sharepoint/dev/design/design-guidance-overview
- Design a web part: https://learn.microsoft.com/sharepoint/dev/design/design-a-web-part
- Design considerations for web parts: https://learn.microsoft.com/sharepoint/dev/spfx/web-parts/basics/design-considerations-for-web-parts
- Web part levels, titles, descriptions, commanding, layout patterns, empty states, accessibility, examples, icons: https://learn.microsoft.com/sharepoint/dev/design/

---

## 1. When to apply this skill

**SPFx UI ပြောင်းလဲမှု မဆို**:

- **Web parts** အသစ် သို့ သိသိသာသာ ပြင်
- UI ထည့်သော **SPFx extensions** အသစ် (Application/Field Customizers, Command Sets)
- ပြောင်းလဲမှုများ:
  - Layout, card structure, grid behavior
  - Web part **titles, descriptions, commands**
  - **Empty, loading, error, placeholder** experiences
  - Breakpoints ကြား **responsive behavior**
  - **Information architecture** (content groupings, levels, flows)

**မသုံး**:
- Build/toolchain-only (Heft/webpack, packaging)
- User-facing surface မရှိ pure back-end/service
- **ဤ repo classic visual clone** — type, color, spacing, hover, animation, `@media` breakpoints → `classic-visual-parity` (ဤ skill ၏ “no pixel-perfect” နှင့် 480/1024 rules **မသက်ရောက်**)

---

## 2. Web part structure & levels

SPFx web parts ကို **levels ရှင်း** + hierarchy ဖြင့် ဒီဇိုင်း:

1. **Web part level**
   - Title: ရှင်း၊ action- သို့ outcome-oriented (ဥပမာ "Permissions risk heatmap", "PRH" မဟုတ်)
   - Description: စာကြောင်း ၁–၂ — _ဘာလုပ်သလဲ?_ နှင့် _ဘာကြောင့် အရေးပါသလဲ?_
   - Optional **subtitle/context**: scope သို့ key filter (ဥပမာ "Current site", "Last 30 days")။

2. **Section / region level**
   - ဆက်စပ် content ကို visually သီးခြား regions (cards, panels, tabs)။
   - Region တိုင်း **label (heading) ရှင်း** + purpose။

3. **Item level**
   - Row/card/tile တိုင်း တစ်ခုတည်းနဲ့ နားလည်ရ: label, primary metric/state, key action။
   - **Progressive disclosure**: high-value info အရင်; details = drill-ins။

Implementation snippet (React):
```ts
// Example web part root structure
return (
  <section aria-label="Permissions risk heatmap" className={styles.webPartRoot}>
    <header className={styles.header}>
      <h2 className={styles.title}>Permissions risk heatmap</h2>
      <p className={styles.description}>
        Highlight sites and groups with the highest sharing and access risk.
      </p>
      {renderHeaderCommands()}
    </header>

    <main className={styles.content}>
      {renderMainContent()}
    </main>
  </section>
);
```

---

## 3. Layout & responsive design

Grid နှင့် responsive patterns:
- https://learn.microsoft.com/sharepoint/dev/design/grid-and-responsive-design
- https://learn.microsoft.com/sharepoint/dev/design/layout-patterns

Core rules:

1. **Fixed widths မဟုတ် — responsive layouts**
   - CSS `grid` / `flex` + min/max widths ဦးစားပေး။
   - Primary flows မှာ horizontal scroll ရှောင်; cards wrap။

2. **Breakpoints** (heuristics) — generic SPFx သာ
   - **Small (< 480px)**: single-column, stacked; မလို chrome ပုန်း။
   - **Medium (480–1024px)**: two-column cards, condensed table, commands နည်း။
   - **Large (> 1024px)**: full grid/table, full command bar.
   - **ခြွင်းချက် (ဤ repo classic clone):** `DBS-FFW-classicsite/2025/style.css` မှ `@media` widths ကူး (အများအားဖြင့် 1200 / 1024 / 959 / 768 / 640 / 480)။ Fluent-only 480/1024 heuristics **မအစား**။

3. **Pixel-perfect မယုံ** (generic SPFx)
   - **Content resilience**: labels ပိုရှည်၊ ဘာသာပြန်စာ၊ data ကွဲပြား။
   - **ခြွင်းချက်:** ဤ repo classic → SPFx က `DBS-FFW-classicsite/2025/style.css` နဲ့ **pixel match လို**။

CSS snippet:
```scss
.webPartRoot {
  display: flex;
  flex-direction: column;
}

.contentGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 12px;
}

@media (max-width: 480px) {
  .contentGrid {
    grid-template-columns: 1fr;
  }
}
```

---

## 4. Web part titles, descriptions & UI text

Key references:
- Titles & descriptions: https://learn.microsoft.com/sharepoint/dev/design/web-part-titles-and-descriptions
- UI text guidance: https://learn.microsoft.com/sharepoint/dev/design/ui-text-for-web-parts

Guidelines:

1. **Titles**
   - **Purpose နှင့် outcome** ဖော် — implementation မဟုတ်။
   - Jargon / internal project names ရှောင်။
   - ကောင်း: _"External sharing overview"_ vs မကောင်း: _"ExtShareV2"_။

2. **Descriptions**
   - စာကြောင်း ၁–၂၊ present tense၊ user benefit အရင်။
   - ဥပမာ: _"Track where external sharing is enabled and identify risky sites."_

3. **Labels & commands**
   - Actions = **verb-first**: _"Filter", "Export", "Open details"_။
   - State နှင့် action တူသော စကားလုံး မသုံး (ဥပမာ tab နှင့် command နှစ်ခုလုံး "Sharing")။

4. **Tone**
   - Professional, direct, neutral။
   - Error text မှာ အပြစ်မတင် — ဖြေရှင်းချက် အာရုံ။

---

## 5. Commanding patterns

Reference: https://learn.microsoft.com/sharepoint/dev/design/web-part-commanding

Principles:

1. **Primary vs secondary actions**
   - Main surface တိုင်း **primary action** တစ်ခု (ဥပမာ "New", "Configure", "Fix issues")။
   - Surface ရှုပ်ရင် secondary actions ကို menus မှာ စု။

2. **Contextual commands**
   - Row-level actions = row အနီး (action icons သို့ contextual menu)။
   - Web-part-level actions = header command bar။

3. **Selection-aware behavior**
   - လက်ရှိ selection အတွက် မမှန်သော commands disable သို့ ပုန်း။
   - Action က selection လိုရင် feedback ရှင်း။

Example command bar:
```tsx
<CommandBar
  items={[
    {
      key: 'newPolicy',
      text: 'New policy',
      iconProps: { iconName: 'Add' },
      onClick: handleNewPolicy
    },
    {
      key: 'export',
      text: 'Export',
      iconProps: { iconName: 'Download' },
      onClick: handleExport
    }
  ]}
/>
```

---

## 6. Placeholders, empty states, and fallbacks

Key refs:
- Placeholders & fallbacks: https://learn.microsoft.com/sharepoint/dev/design/placeholders-and-fallbacks
- Empty states: https://learn.microsoft.com/sharepoint/dev/design/empty-states

**First-run** နှင့် **no-data** experiences အတိအလင်း ဒီဇိုင်း:

1. **First-run / not configured**
   - **Web part ဘာလုပ်သလဲ**, **ဘာပျောက်သလဲ**, **next step ရှင်း** ပြ။
   - Config action ရှင်း: _"Open configuration"_ သို့ settings pane link။

2. **No data (configured ပြီး)**
   - Valid state အသိအမှတ်: _"No risky sites found in the last 30 days."_
   - ဖြစ်နိုင်ရင် meaningful next step: filter ပြောင်း၊ docs၊ alternate view။

3. **Fallback content**
   - Data တစ်စိတ်ပျောက်ရင် အားလုံး ပိတ်မည့်အစား **partial** content ပြ။

Example JSX:
```tsx
if (!isConfigured) {
  return (
    <Placeholder
      iconName="Settings"
      iconText="Set up this web part"
      description="Connect to a data source to see permissions risk for your sites."
      buttonLabel="Open configuration"
      onConfigure={openPropertyPane}
    />
  );
}

if (!items?.length) {
  return (
    <EmptyState
      title="No risky sites found"
      description="We didn't find any sites that match your risk filters for this period."
    />
  );
}
```

---

## 7. Accessibility basics (design side)

Reference: https://learn.microsoft.com/sharepoint/dev/design/accessibility

Design ဆုံးဖြတ်ချက်များ ပံ့ပိုးရမည်:

1. **Keyboard and focus**
   - Interactive elements အားလုံး Tab ရောက်နိုင်။
   - Visual focus indicator နောက်ခံနဲ့ ရှင်းမြင်ရ။

2. **Semantics**
   - Semantic elements: `<button>`, `<a>`, `<header>`, `<main>`, `<section>`, `<table>`။
   - Semantics ဖြည့်ရန် လိုမှသာ ARIA roles/labels။

3. **Color & contrast**
   - အဓိပ္ပာယ်ကို color တစ်ခုတည်း မယုံ (icons/text တွဲ)။
   - SharePoint theme tokens လေးစား + WCAG AA contrast။

Example focus treatment (SCSS):
```scss
.button {
  border-radius: 2px;

  &:focus-visible {
    outline: 2px solid var(--focusBorder, #005a9e);
    outline-offset: 2px;
  }
}
```

---

## 8. Performance-aware design decisions

Design ရွေးချယ်မှုက performance ထိ:

1. **Above-the-fold clarity**
   - Primary summary metrics သို့ table အမြန်ပြ; expensive details နောက်မှ။

2. **Progressive rendering**
   - ကြီးသော datasets အတွက် **lightweight summary view** + detail pages သို့ navigation အတိအလင်း။

3. **Config vs default behavior**
   - Safe, performant defaults (time windows တို၊ scoped data); power users က ချဲ့နိုင်။

---

## 9. How to use this skill in practice

AI editor ကို SPFx UX ဒီဇိုင်း/ညှိခိုင်းရင်:

1. **Identify** surface: web part vs extension, first-run vs daily use။
2. **Apply**:
   - Structure/layout = Section 2–3။
   - Titles, text, commanding = Section 4–5။
   - States နှင့် accessibility = Section 6–7။
3. **Propose** ဤ patterns လိုက်သော JSX/SCSS snippets။
4. **Check**: Enterprise tenant အတွက် နားလည်၊ accessible, responsive, performant လား?
