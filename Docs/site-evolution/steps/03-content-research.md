# Step 03 — Content research

## Goal

Produce a research brief for content that can be found publicly (mainly 1762/1786 and historical framing), without publishing anything until editorial gate.

## Prerequisites

- [x] Step 01 open questions known
- [x] Awareness that REAA lineage topics are sensitive
- [x] Step 02 routes frozen (`/documentos/1762/`, `/documentos/1786/`, `/historia/*`)

## Status

`done` (2026-08-04) — **recommendation only**; nothing goes live without Step 04 approval

**Online availability re-checked:** 2026-08-04 — full historical texts **are** publicly downloadable (see § Availability check).

---

## Tasks

- [x] Search and list candidate editions of Constitutions & Regulations of **1762**
- [x] Search and list candidate editions of Grand Constitutions of **1786**
- [x] Note language, license, source reliability for each candidate
- [x] Draft short public timelines for: R.E.A.A. · Supremos Conselhos · Confederação
- [x] Flag disputed / unsuitable material
- [x] Write recommendation: link-out vs host PDF vs summary-only

---

## Availability check (2026-08-04)

**Verdict:** Yes — the **full historical texts** of both 1762 and 1786 can be obtained online from public libraries. They are **not** a single “official CISCSR PDF”; they are 19th-century editions (often Pike / US Supreme Council tradition). Use only after Comité approval.

| Source | Contents | Access verified | Direct PDF / view |
|--------|----------|-----------------|-------------------|
| Internet Archive — Pike/Macoy 1859 | 1762 + 1786 (+ related statutes) | HTTP 200, ~12 MB PDF | https://archive.org/details/statutesregulati00free · [PDF](https://archive.org/download/statutesregulati00free/statutesregulati00free.pdf) |
| Internet Archive — NMJ short 1762 | Constitutions of 1762 (Rite of Perfection) | HTTP 200, ~2 MB PDF | https://archive.org/details/constitutionsreg00scot · [PDF](https://archive.org/download/constitutionsreg00scot/constitutionsreg00scot.pdf) |
| Internet Archive — NMJ 1885 | 1762 + 1786 + NMJ regulations | HTTP 200, ~5 MB PDF | https://archive.org/details/constitutionsgen00scot · [PDF](https://archive.org/download/constitutionsgen00scot/constitutionsgen00scot.pdf) |
| Gallica (BnF) | FR/EN Pike–Laffon edition incl. **Grandes Constitutions 1786** | IIIF manifest 200 | https://gallica.bnf.fr/ark:/12148/bpt6k329509h |
| LoC scan | Constitutions and regulations of 1762 (larger compilation) | Catalogue / viewer | https://archive.org/details/constitutionsreg00free · https://www.loc.gov/resource/gdcmassbookdig.constitutionsreg00free/ |

**License note:** LoC/Archive items above are treated as public-domain / no known US copyright restrictions on the scans. Still: **do not republish on CISCSR as “the” official text** without endorsement — versions differ; 1786 authenticity is debated historically while CISCSR **recognises** them institutionally (Regulamento Art. 2).

**Practical options for the site**

1. **Link-out** to Archive.org / Gallica (safest short term).  
2. **Host a CISCSR-approved PDF** copied from one of the above after written approval.  
3. Stay on **summary-only** placeholders until that approval.

---

1. **Institutional vs historical authenticity:** CISCSR Regulamento Art. 2 and the Declaração treat 1762 and 1786 as the Order’s fundamental laws. Historians often discuss the **1786** text as **apocryphal** (attribution to Frederick II of Prussia; no original MS produced). The public site should **not** pick a fight with either tradition. Prefer: “reconhecidas pela Confederação como leis fundamentais” + optional neutral note that several historical versions exist.
2. **Do not host a random US/Pike PDF as “the” CISCSR text** without Comité approval — editions differ (Latin tradition, FR translations, EN Pike/Macoy compilations, later Lausanne 1875 concordances).
3. **Avoid lineage polemics** between Supreme Councils on the History pages.
4. **Blogs / unofficial FR pages** may reproduce text; prefer **library archives** (Internet Archive, LoC, Gallica) for link-outs.

---

## Research log — 1762

| Candidate | Language | Source URL | License / access | Notes | Recommend? |
|-----------|----------|------------|------------------|-------|------------|
| *The constitutions and regulations of 1762* (LoC / Archive scan; often with later material) | EN (+ FR excerpts in some printings) | https://archive.org/details/constitutionsreg00free · https://www.loc.gov/resource/gdcmassbookdig.constitutionsreg00free/ | Public domain (LoC: unaware of copyright restrictions on item) | Classic 19th-c. compilation tied to SJ/Pike editorial tradition | **Link-out candidate** after approval |
| NMJ pamphlet: *Constitutions and regulations of 1762… Rite of Perfection (25 degrees)* | EN | https://archive.org/details/constitutionsreg00scot | Digitized historical | Shorter; frames 1762 as Rite of Perfection / Emperors of East & West | Secondary link |
| NMJ 1885 volume (includes 1762 + 1786) | EN | https://archive.org/details/constitutionsgen00scot | Digitized historical | Convenient single volume; US jurisdiction framing | Secondary |
| “Constitutions de Bordeaux – 1762” (FR institutional pages) | FR | e.g. SCNDF document lists | Varies | Useful FR naming (*Bordeaux 1762*) aligned with European usage | Prefer FR naming on PT/FR UI; verify which text they publish before linking |

---

## Research log — 1786

| Candidate | Language | Source URL | License / access | Notes | Recommend? |
|-----------|----------|------------|------------------|-------|------------|
| Pike/Macoy 1859: *Statutes… and grand constitutions* | EN | https://archive.org/details/statutesregulati00free | PD (LoC) | Widely cited EN compilation | Link-out only if approved |
| Gallica: *Grandes constitutions… 1786* (Laffon de Ladebat / Pike tradition) | FR / EN parallel | https://gallica.bnf.fr/ark:/12148/bpt6k329509h | BnF Gallica | Strong **FR** institutional library source | **Preferred FR link-out candidate** |
| NMJ 1885 volume (see above) | EN | https://archive.org/details/constitutionsgen00scot | Digitized | Bundled with 1762 | Secondary |
| *A historical inquiry… Grand Constitutions of 1786* (1872) | EN | https://archive.org/details/cu31924030335578 | PD scan | **Historiography**, not the constitution text itself — do not present as the law | Research only; not for Documentos download |
| Lausanne 1875 concordances (e.g. ES SC pages) | ES/FR variously | e.g. Spanish SC historical docs | Jurisdictional | Later revision/concordance — different document | Do **not** substitute for 1786 unless CISCSR says so |
| Unofficial FR web articles reproducing articles | FR | various | Unclear | Convenience copies; authenticity/version unknown | Avoid as primary |

---

## Recommendation for HTML phase (Documentos pages)

| Option | What it means | Verdict |
|--------|---------------|---------|
| **A. Summary-only** | Page explains what 1762/1786 are per CISCSR texts; no full text | **Default until Step 04** |
| **B. Link-out** | Summary + “Consultar edição histórica” → Archive.org / Gallica | **Preferred next step** after Comité picks URLs |
| **C. Host PDF on CISCSR site** | Upload chosen edition under `Docs/` | Only after explicit approval of **exact** file |
| **D. Full text in HTML** | Paste constitution into pages | Avoid (length, version risk, maintenance) |

**Proposed page formula (both `/documentos/1762/` and `/1786/`):**

1. Title matching Regulamento/Declaração language  
2. 2–4 sentences: role as fundamental laws of the Order (cite Art. 2 / Declaração)  
3. Status: Em preparação *or* link to approved external edition  
4. Short disclaimer: historical editions vary; CISCSR recognition is institutional  
5. Link back to Regulamento + Declaração  

**Languages:** UI in PT/EN/FR/AR. Full historical text: **FR and/or EN** link-outs first; PT/AR translation only if CISCSR commissions it.

---

## History outlines (draft — not published)

### R.E.A.A. (public-safe bullets)

| Draft bullets | Public OK? | Needs approval |
|---------------|------------|----------------|
| 18th c.: high-grade systems; **1762** Constitutions & Regulations (often “Bordeaux” / Rite of Perfection, historically 25°) | cautious yes | Yes — keep short |
| Tradition of **1786** Grand Constitutions structuring the **33°** Scottish system | cautious yes | Yes — avoid authenticity debate unless asked |
| **1801:** first Supreme Council of the AASR commonly dated at Charleston (as in CISCSR Declaração) | yes (already on site) | Confirm wording |
| 19th–20th c.: international spread of Supreme Councils and mutual relations | yes, vague | Yes |
| Do **not** claim a single worldwide hierarchy or settle rival obediences | n/a | Editorial rule |

### Supremos Conselhos (general)

| Draft bullets | Public OK? | Needs approval |
|---------------|------------|----------------|
| A Supreme Council governs the Scottish high degrees within its jurisdiction | yes | Align with Declaração |
| Sovereignty and territorial jurisdiction (Regulamento Art. 3) | yes | Already institutional |
| Per-country founding stories for BR / FR / PT / MA | **only** from each SC or CISCSR-approved bios | Yes — placeholders until then |

### Confederação (from our docs only)

| Draft bullets | Public OK? | Needs approval |
|---------------|------------|----------------|
| Tratado, Lyon, **12 Dec 2025** — BR, FR, PT, MA | yes | Already published |
| Regulamento Interno, Lisboa, **4 Jul 2026** | yes | Already published |
| Non-hierarchical concertation organ | yes | Already published |
| Presidency rotation PT → MA → BR → FR, 3 years | yes | From Regulamento |
| Admission rules for new members (Art. 4–5) — summary only | yes | Optional |

---

## Decisions needed (→ Step 04)

1. Summary-only vs link-out vs host PDF for 1762/1786? — **awaiting post-meeting** (Q8–Q9)  
2. If link-out: approve **which** URL(s) (suggest Gallica FR for 1786 + one Archive EN for 1762/1786 bundle)? — pending  
3. May History/R.E.A.A. mention Charleston 1801 and “several historical versions of 1786”? — stakeholder asked for a **meeting suggestion** (draft in Step 04); **do not publish expansion** until Comité OK  
4. Any CISCSR-owned translation to host later? — pending; languages of interest FR / EN / PT / ES

### Q10 meeting suggestion (not live on site)

- Charleston **1801** (already in Declaração)  
- Minimal chronology: 1762 · 1786 (recognised fundamental laws) · 1801 · international expansion · CISCSR treaty 2025  
- **No** authenticity debate on 1786

## Deliverables

- [x] This brief completed  
- [x] Findings reflected in section specs (`documentos`, `historia`)

## Acceptance criteria

- [x] Recommended path per constitution: **summary-only default; link-out after approval**  
- [x] No unverified claims marked ready for the site
