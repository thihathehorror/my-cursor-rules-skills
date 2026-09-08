# Site Pages chrome toggles (DBS-FFW)

> Docs ဘာသာပြန် — live fill-in = `docs/migration/SITE_CHROME.md`။ Column internal names = English။

Classic pages က **inline** chrome ထိန်း။ Full-bleed / SPA web part ပတ်လည် SharePoint chrome ဖျောက်ရန် modern host page လိုမှသာ Site Pages Yes/No columns သုံး။ Application Customizer မဟုတ်။ Cloned body UI ၏ Visual PASS အတွက် **မလို**။

## Columns (user တောင်းမှသာ)

Site Pages → **+ Add column** → **Yes/No**:

| Display name | Internal name | Default |
|--------------|---------------|---------|
| Show Header | `ShowHeader` | Yes |
| Show Footer | `ShowFooter` | Yes |
| Show Banner | `ShowBanner` | Yes |

Create ပြီး internal names အတည်ပြု။ မသုံးရင် Banner ချန်။

| Value | Effect |
|-------|--------|
| Yes / blank / column missing | Show (fail-open) |
| No | Hide |

Runtime: host page item ပေါ် `SPHttpClient`။ အသေးစိတ်: `references/site-chrome.md`။
