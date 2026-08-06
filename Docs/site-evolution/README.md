# CISCSR site evolution — planning pack

This folder holds the **planning docs** for evolving the website from a single-page brochure to a multi-page institutional site, based on `Docs/new_specs.txt` and aligned with `Docs/specs.txt` / `Docs/design-concepts.md`.

**Rule:** expand and approve content here **before** changing the live site.

**This phase:** static **HTML only** (migrate + public placeholders).  
**Future work:** Chat, private/members areas, Loja, and any auth-backed Biblioteca — see Step 09.

**Live site today:** https://pfigueiredo.github.io/CICSR_REAA/  
**Stack today:** vanilla HTML/CSS/JS, GitHub Pages, PT/EN/FR/AR + RTL.

---

## How to use

1. Read [`00-overview.md`](00-overview.md).
2. Work through [`steps/`](steps/) in order; mark checkboxes as you go.
3. Fill each **in-scope** [`sections/`](sections/) spec until ready or explicit placeholder.
4. Skip Chat / Biblioteca / Loja for implementation (future work).
5. Only then execute multipage HTML work (Step 06).

---

## Status board

| Item | Status |
|------|--------|
| Overview | drafting |
| Step 01 — Inventory | done |
| Step 02 — IA and routing | done |
| Step 03 — Content research | done |
| Step 04 — Stakeholder pack | ready to send (PT/EN/FR/AR) |
| Step 05 — Placeholder pages | done |
| Step 06 — Multipage migration (HTML) | done |
| Step 07 — i18n and nav | done |
| Step 08 — Fill content | todo |
| Step 09 — Future work (Chat / private / Loja) | deferred |
| Step 10 — Launch checklist | todo |
| Section: Confederação | drafting |
| Section: Princípios | drafting |
| Section: Comunicações | todo |
| Section: Eventos | todo |
| Section: Contactos | drafting |
| Section: Membros | drafting |
| Section: Documentos | drafting |
| Section: História | drafting |
| Section: Chat | deferred (future) |
| Section: Biblioteca | deferred (future) |
| Section: Loja | deferred (future) |

Status values: `todo` · `drafting` · `ready` · `done` · `deferred`

---

## Index — steps

| # | File | Goal |
|---|------|------|
| 00 | [00-overview.md](00-overview.md) | Goals, HTML-phase scope, out of scope |
| 01 | [steps/01-inventory.md](steps/01-inventory.md) | Map current site + docs vs new IA |
| 02 | [steps/02-ia-and-routing.md](steps/02-ia-and-routing.md) | Final URL tree and navigation (public only) |
| 03 | [steps/03-content-research.md](steps/03-content-research.md) | Research brief (1762/1786, REAA history) |
| 04 | [steps/04-stakeholder-pack.md](steps/04-stakeholder-pack.md) | Questionnaire for public content ([PT/EN/FR/AR](stakeholder-questionnaire/)) |
| 05 | [steps/05-placeholder-pages.md](steps/05-placeholder-pages.md) | Placeholder pattern (HTML pages) |
| 06 | [steps/06-multipage-migration.md](steps/06-multipage-migration.md) | Split into static pages |
| 07 | [steps/07-i18n-and-nav.md](steps/07-i18n-and-nav.md) | Locales, spelling fix, hreflang |
| 08 | [steps/08-fill-content.md](steps/08-fill-content.md) | Replace placeholders as content arrives |
| 09 | [steps/09-reserved-areas.md](steps/09-reserved-areas.md) | **Future work** — Chat / private / Loja |
| 10 | [steps/10-launch-checklist.md](steps/10-launch-checklist.md) | QA and deploy (HTML phase) |

---

## Index — section specs

### This phase (HTML)

| Section | File | Nav |
|---------|------|-----|
| Confederação | [sections/confederacao.md](sections/confederacao.md) | primary |
| Princípios e Valores | [sections/principios.md](sections/principios.md) | primary |
| Comunicações | [sections/comunicacoes.md](sections/comunicacoes.md) | secondary |
| Eventos e reuniões | [sections/eventos.md](sections/eventos.md) | primary |
| Contactos | [sections/contactos.md](sections/contactos.md) | primary |
| Membros | [sections/membros.md](sections/membros.md) | primary |
| Documentos fundadores | [sections/documentos.md](sections/documentos.md) | primary |
| História | [sections/historia.md](sections/historia.md) | primary |

### Future work (do not implement now)

| Section | File | Why deferred |
|---------|------|--------------|
| Chat | [sections/chat.md](sections/chat.md) | Needs auth / messaging — not static HTML |
| Biblioteca | [sections/biblioteca.md](sections/biblioteca.md) | Scope TBD; private library needs more than HTML |
| Loja | [sections/loja.md](sections/loja.md) | Commerce / catalogue — not this phase |

---

## Related source documents

- [`Docs/new_specs.txt`](../new_specs.txt) — IA outline (source)
- [`Docs/specs.txt`](../specs.txt) — strategic programme (calendar, boletim, messaging)
- [`Docs/design-concepts.md`](../design-concepts.md) — visual/tech constraints
- [`Docs/Regulamento-Interno-CISCSR.pdf`](../Regulamento-Interno-CISCSR.pdf) — internal regulation
- [`Docs/Confederação S.C. do REAA (V4).docx`](../Confedera%C3%A7%C3%A3o%20S.C.%20do%20REAA%20(V4).docx) — source for Regulamento
