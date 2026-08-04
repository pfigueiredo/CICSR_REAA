# Step 01 — Inventory

## Goal

Map everything we already have (site, locales, Docs) against the new IA, and list gaps.

## Prerequisites

- Read [`../00-overview.md`](../00-overview.md)
- Access to repo + `Docs/`

## Inputs

| Source | Use |
|--------|-----|
| `index.html` | Current sections / anchors |
| `locales/pt.json` (and en/fr/ar) | Existing copy |
| `Docs/new_specs.txt` | Target IA |
| `Docs/specs.txt` | Strategic programme overlap |
| `Docs/Regulamento-Interno-CISCSR.pdf` | Founding/regulatory text |
| `Docs/Confederação S.C. do REAA (V4).docx` | Source for Regulamento |
| `Docs/design-concepts.md` | Design constraints |

## Tasks

- [x] List every current `#section` and nav item
- [x] For each new IA item, mark: **ready / partial / missing / deferred**
- [x] Note which locale keys map to which section spec
- [x] Extract from Regulamento: official document name, organs, contacts clues, membership rules
- [x] Confirm “Constituição da Confederação” vs “Regulamento Interno” naming
- [x] List spelling/name issues (e.g. Kamal El Fadhi)
- [x] Update section specs’ “Sources we already have”

## Status

`done` (2026-08-04)

---

## 1. Current site map (single page)

**File:** `index.html`  
**Nav:** Confederação · Princípios · Declaração · Membros · História · Documentos · Contactos

| Anchor / block | Content |
|----------------|---------|
| `#inicio` / hero | Brand, CTAs |
| `#confederacao` | Apresentação |
| `#principios` | Four pillars |
| `#declaracao` | Full Declaração de Princípios |
| `#membros` | Map + 4 founders |
| `#historia` | 3 chronology items |
| `#documentos` | 3 cards (Declaração, Regulamento PDF, Comunicados “em breve”) |
| motto band | Quote |
| `#contactos` | Form (`type="button"` — no submit backend) |
| footer | Name + © 2026 |

---

## 2. Locale key → section map

| Locale root | Section spec | Notes |
|-------------|--------------|-------|
| `meta`, `brand`, `nav`, `hero`, `footer`, `motto` | homepage / chrome | |
| `confederation.*` | confederacao | ready |
| `pillars.*`, `declaration.*` | principios | ready; signatory spelling wrong |
| — | comunicacoes | no keys yet |
| — | eventos | no keys yet |
| `contact.*` | contactos | partial |
| `members.*` | membros | fundadores only; no Fundadores/Membros split keys |
| `documents.*` | documentos | 3 cards |
| `history.*` | historia | t1–t3 only |

All four files: `locales/pt.json`, `en.json`, `fr.json`, `ar.json`.

---

## 3. Gap table (completed)

| IA item | Current location | Status | Notes |
|---------|------------------|--------|-------|
| Apresentação | `#confederacao` | ready | `confederation.*` |
| Princípios e Valores | `#principios` + `#declaracao` | ready | Fix El Fadhi in Step 07 |
| Comunicações | — | missing | HTML placeholder in phase |
| Eventos anteriores | — | missing | Lyon 2025 + Lisboa 2026 known; need approval to list |
| Eventos agendadas | — | missing | placeholder |
| Contactos | `#contactos` | partial | UI only; no email/address in Regulamento |
| Fundadores | `#membros` | ready | BR, FR, PT, MA |
| Membros (non-founders) | — | missing | empty-state OK; admission rules in Regulamento Art. 4–5 |
| “Constituição da Confederação” | Regulamento PDF | **naming clarified** | See §4 — use **Regulamento Interno**; no separate Constituição file in repo |
| Constituição 1762 | Declaração + Regulamento Art. 2 | missing file | cited as Order founding law |
| Constituição 1786 | same | missing file | same |
| História Confederação | `history.t3` | partial | expand on dedicated page |
| História Supremos Conselhos | `history.t2` | partial | placeholder/enrich |
| História R.E.A.A. | `history.t1` | partial | placeholder/enrich |
| Chat | — | deferred | future work |
| Biblioteca | — | deferred | future work |
| Loja | — | deferred | future work |

---

## 4. Regulamento extract (from V4 docx → PDF)

**Official title:**  
`REGULAMENTO INTERNO DA CONFEDERAÇÃO INTERNACIONAL DOS SUPREMOS CONSELHOS SOBERANOS E REGULARES DO R.E.A.A.`

### Naming decision (recommended for site)

| new_specs label | What exists | Site recommendation |
|-----------------|-------------|---------------------|
| “Constituição da Confederação” | **Regulamento Interno** (full document) | Label the download **Regulamento Interno**. Título I is headed “Da constituição e dos princípios gerais” (chapter title, not a separate act). |
| Carta / estatutos | Preâmbulo cites tratado (Lyon 2025); Art. 9 says “Nos termos dos estatutos…” for presidency order | Ask stakeholders (Step 04) if a separate **estatutos/carta** is public; not in repo today |
| 1762 / 1786 | Art. 2: recognized as unique fundamental laws of the Order | Separate Documentos entries; need approved public edition |

**Open question remains only for:** whether a public “Carta constitutiva / Estatutos” exists besides the Regulamento. Default for HTML phase: publish Regulamento as the Confederation’s institutional document.

### Organs (for copy / future Eventos)

- **Assembleia Confederal** — SGCs or delegates; ≥1×/year; admissions, exclusions, opinions
- **Presidência rotativa** — 3 years; order of first presidencies: **Portugal → Marrocos → Brasil → França**
- Vice-presidência open to any member
- Conflict: mediação → Conselho de Sábios (founders)

### Membership

- Art. 4–5: admission criteria and 2/3 + no negative vote procedure
- Distinction **membros fundadores** vs **novos membros** is explicit (Art. 9)

### Contacts

- **None** in Regulamento (no sede, email, phone)

### Dates

- Tratado: **12 December 2025**, Lyon (preâmbulo)
- Regulamento entry into force: **Lisboa, 3 July 2026** (Art. 15)

---

## 5. Spelling / name issues

| Item | Current | Target | Where |
|------|---------|--------|-------|
| Morocco SGC | `Kamal El-Fehdi` | `Kamal El Fadhi` (per `new_specs.txt`) | `declaration.signatories` in **pt, en, fr** (check ar) |
| Acronym | CISCSR used in docs/design | Confirm on-site usage | brand strings |

AR locale: verify signatory line in Step 07.

---

## 6. Overlap with `Docs/specs.txt` (strategic → HTML phase)

| Strategic item | HTML phase handling |
|----------------|---------------------|
| Messaging group (WhatsApp etc.) | Future / organisational — not site |
| Presidency rotation | Already in Regulamento + history; can show on Confederação/Eventos |
| Calendário anual | Eventos page (placeholder → fill) |
| Boletim digital | Comunicações later |
| Vitrine excelência | Out of IA for now / later |

---

## Decisions needed

| Decision | Recommendation from inventory | Needs stakeholder? |
|----------|-------------------------------|--------------------|
| Constituição vs Regulamento on site | Call it **Regulamento Interno**; map new_specs “Constituição da Confederação” → this PDF | Confirm if separate Estatutos/Carta is public |
| List Lyon/Lisboa on Eventos before full calendar | Yes as “anteriores” if approved | Yes (Step 04) |
| El Fadhi spelling | Fix in locales | Confirm exact form (space vs hyphen) |

## Deliverables

- [x] Completed gap table
- [x] Notes for section specs (see updates in `../sections/`)

## Acceptance criteria

- [x] Gap table filled
- [x] Naming of Constituição vs Regulamento recorded
- [x] No section left without a status
