# Step 02 — IA and routing

## Goal

Freeze the **public** URL tree and navigation for the HTML phase. Chat / Biblioteca / Loja are future work — omit from routes and nav.

## Prerequisites

- [x] Step 01 inventory done
- [`../00-overview.md`](../00-overview.md) draft URL tree reviewed

## Inputs

- Gap table from Step 01
- Section specs in `../sections/`
- Design concepts (institutional tone; avoid nav overload)

## Tasks

- [x] Finalize routes (folders with `index.html` for GitHub Pages)
- [x] Define primary nav labels (≤ 7–8 items)
- [x] Define secondary / footer links (Comunicações)
- [x] Confirm Chat / Biblioteca / Loja **omitted** (future work)
- [x] Decide homepage: portal (short) vs keep long scroll + deep links
- [x] Map each route → section spec file
- [x] Plan redirects/anchors from old `#ids` if needed

## Status

`done` (2026-08-04) — frozen for HTML phase unless owner overrides

---

## Decisions (frozen)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Homepage | **Portal** — hero + short links to areas | Fits multipage IA; avoids duplicating long scroll |
| Declaração in nav | **No** separate top item — under `/principios/#declaracao` | Keeps primary nav to 7 |
| História | **One continuous page** with 3 in-page threads (`#confederacao`, `#supremos-conselhos`, `#reaa`) | Narrative brochure; avoids thin hub → empty subpages |
| Eventos | **One page**, two blocks (Anteriores / Agendadas) | Enough for v1; no extra folders |
| Documentos 1762/1786 | **Subpages** with placeholders | Stable URLs when editions arrive |
| Regulamento | Card on index → thin page **or** direct PDF; prefer **thin page** + download | Institutional framing |
| Comunicações | **Footer / secondary** only | Hub + speech subroute; not primary (nav already full) |
| Chat/Biblioteca/Loja | **Omit** | Future work (Step 09) |

---

## Primary navigation (7)

Order:

1. Confederação → `confederacao/`
2. Princípios → `principios/`
3. Membros → `membros/`
4. História → `historia/`
5. Documentos → `documentos/`
6. Eventos → `eventos/`
7. Contactos → `contactos/`

Labels via i18n (`nav.*` — add `nav.events`, drop relying on `nav.declaration` in primary bar; keep key for in-page jump).

## Secondary / footer

| Link | Route |
|------|-------|
| Comunicações | `comunicacoes/` |
| Declaração de Princípios | `principios/#declaracao` |
| Regulamento Interno | `documentos/regulamento-interno/` (or PDF) |

No “Área reservada” in this phase.

---

## Final route table

Paths are **site-root relative** (GitHub Pages project site: base `/CICSR_REAA/`). Each folder has `index.html`.

| Route | Section spec | Nav | Treatment |
|-------|--------------|-----|-----------|
| `/` (`index.html`) | — portal | — | New: hero + area grid (ready / em preparação) |
| `/confederacao/` | confederacao | primary | Migrate existing copy |
| `/principios/` | principios | primary | Pillars + Declaração (`#declaracao`) |
| `/membros/` | membros | primary | Fundadores + empty Membros |
| `/historia/` | historia | primary | Continuous brochure: 3 threads as sections + anchors |
| `/historia/confederacao/` | historia | redirect | → `/historia/#confederacao` |
| `/historia/supremos-conselhos/` | historia | redirect | → `/historia/#supremos-conselhos` |
| `/historia/reaa/` | historia | redirect | → `/historia/#reaa` |
| `/documentos/` | documentos | primary | Cards index |
| `/documentos/regulamento-interno/` | documentos | via documentos | Meta + PDF download |
| `/documentos/1762/` | documentos | via documentos | Placeholder |
| `/documentos/1786/` | documentos | via documentos | Placeholder |
| `/eventos/` | eventos | primary | Placeholder (+ optional approved dates) |
| `/comunicacoes/` | comunicacoes | footer | Hub (discursos) |
| `/comunicacoes/discurso-lisboa-2026/` | comunicacoes | via hub | Discurso de posse (HTML PT/EN/FR; PDF + ES; AR note) |
| `/contactos/` | contactos | primary | Migrate form |

**Out of tree:** `/chat/`, `/biblioteca/`, `/loja/`

---

## Repo folder map (for Step 06)

```
CICSR_REAA/
  index.html                 # portal
  confederacao/index.html
  principios/index.html
  membros/index.html
  historia/index.html          # continuous page (3 sections + anchors)
  historia/confederacao/       # redirect → /historia/#confederacao
  historia/supremos-conselhos/ # redirect → /historia/#supremos-conselhos
  historia/reaa/               # redirect → /historia/#reaa
  documentos/index.html
  documentos/regulamento-interno/index.html
  documentos/1762/index.html
  documentos/1786/index.html
  eventos/index.html
  comunicacoes/index.html
  comunicacoes/discurso-lisboa-2026/index.html
  contactos/index.html
  css/ …  js/ …  locales/ …  assets/ …  Docs/ …
```

Asset paths from depth-1 pages: `../css/`, `../js/`, `../locales/`, `../assets/`  
From depth-2 (`historia/reaa/`, `documentos/1762/`, `comunicacoes/discurso-lisboa-2026/`): `../../…`

---

## Old single-page anchors

| Old | New |
|-----|-----|
| `#inicio` | `/` |
| `#confederacao` | `/confederacao/` |
| `#principios` | `/principios/` |
| `#declaracao` | `/principios/#declaracao` |
| `#membros` | `/membros/` |
| `#historia` | `/historia/` |
| `#documentos` | `/documentos/` |
| `#contactos` | `/contactos/` |

**Migration note:** After cutover, bare `#…` on the new portal will not restore old sections. Optional later: tiny redirect map on `index.html` if `location.hash` is set — not required for v1.

---

## Homepage portal content (spec)

1. Existing ceremonial hero (shortened CTAs: Confederação + Membros, or Documentos)
2. Grid / list of areas with status:
   - Ready: Confederação, Princípios, Membros, Documentos, Contactos, História (partial)
   - Em preparação: Eventos, Comunicações; História sub-threads as needed
3. Motto band + footer (with Comunicações link)

Do **not** paste full Declaração on the homepage.

---

## Acceptance criteria

- [x] Route table marked final for HTML phase
- [x] Every public route has a section spec
- [x] No Chat / private / Loja routes
- [x] Primary nav = 7 items
