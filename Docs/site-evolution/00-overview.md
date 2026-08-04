# 00 — Overview

## Goals

Evolve the CISCSR website from a single-page institutional brochure into a **multi-page** site that matches the public information architecture in `Docs/new_specs.txt`, while preserving the classical institutional design (`Docs/design-concepts.md`).

Outcomes:

1. Clear public IA with stable URLs per area.
2. Honest **placeholders** for content not yet available (static HTML only).
3. Section specs complete **before** implementation.
4. Private / product areas (Chat, and any members-only tools) marked **future work** — out of this phase.

## Scope for this phase (HTML only)

**In scope:** multipage static HTML/CSS/JS on GitHub Pages — migrate existing copy, add public pages, add institutional placeholders.

| Area | This phase |
|------|------------|
| Confederação, Princípios, Membros, História, Documentos, Contactos | Migrate / expand (HTML) |
| Comunicações, Eventos | Placeholder pages (HTML) |
| Documentos 1762 / 1786 | Placeholder until approved text |
| Chat (3 níveis) | **Future work** — no route, no stub |
| Biblioteca (if members-only / auth) | **Future work** |
| Loja (commerce / catalogue) | **Future work** |

Optional later: a **public** Biblioteca that is only a list of PDFs/links is still HTML — decide in section spec if/when wanted; default is defer with Chat/Loja.

## IA summary

```
THIS PHASE (static HTML)
Confederação
  · Apresentação
  · Princípios e Valores
  · Comunicações (Discurso)     ← placeholder OK
  · Eventos (Anteriores / Agendadas) ← placeholder OK
  · Contactos
Membros · Fundadores / Membros
Documentos · Constituição CISCSR / 1762 / 1786
História · Confederação / Supremos Conselhos / R.E.A.A.

FUTURE WORK (not HTML-only)
Chat (3 níveis) — auth / messaging
Biblioteca — if private or CMS
Loja — if commerce
```

## Principles

- Expand docs in this folder **before** changing the live site.
- Prefer **placeholders** over invented events, speeches, or shop items.
- Stay on vanilla HTML/CSS/JS + GitHub Pages for this phase.
- Multilingual from day one: PT, EN, FR, AR (+ RTL).
- Do not build Chat, login, or shop in this phase.
- Align calendar/boletim ideas from `Docs/specs.txt` as **content** on public pages when available — not as private apps.

## Immediate factual note

Soberano Grande Comendador de Marrocos: **Kamal El Fadhi** (not Fedhi / El-Fehdi).  
Current locales still use `Kamal El-Fehdi` in declaration signatories — fix in Step 07 / section specs.

## What we already have on the site

| Area | Status |
|------|--------|
| Apresentação (Confederação) | Ready (copy in locales) |
| Princípios + Declaração | Ready |
| Membros (4 fundadores) | Ready (no Fundadores/Membros split yet) |
| História | Thin chronology only |
| Documentos | Declaração + Regulamento PDF; third card “em breve” |
| Contactos | Form placeholder |
| Comunicações / Eventos | Absent → HTML placeholders |
| Chat / Biblioteca / Loja | Future work |

## Out of scope (this phase)

- Chat authentication, messaging backend, or fake chat UI.
- Members-only / private areas.
- Loja catalogue, payments, or merch.
- Replacing the design system.
- Publishing ritual, private rolls, or non-approved historical editions.

## Suggested URL tree (this phase only) — frozen in Step 02

```
/
/confederacao/
/principios/            ← includes #declaracao
/membros/
/historia/
/historia/confederacao/
/historia/supremos-conselhos/
/historia/reaa/
/documentos/
/documentos/regulamento-interno/
/documentos/1762/
/documentos/1786/
/eventos/               ← placeholder (Anteriores / Agendadas on one page)
/comunicacoes/          ← footer only; placeholder
/contactos/
```

**Nav primary (7):** Confederação · Princípios · Membros · História · Documentos · Eventos · Contactos  
**Footer:** Comunicações · Declaração · Regulamento  

Homepage = **portal** (not full long-scroll clone).  
No `/chat/`, `/biblioteca/`, or `/loja/` in this phase.

**Inventory note (Step 01):** new_specs “Constituição da Confederação” maps to the **Regulamento Interno** PDF unless stakeholders publish separate Estatutos/Carta.

## Status

- [x] Folder created
- [x] Chat / private areas marked future work
- [x] Step 01 inventory done
- [x] Step 02 IA / routing frozen
- [x] Step 03 research brief (1762/1786 + history outlines)
- [x] Step 05 placeholder pattern + PT copy frozen
- [x] Step 06 multipage HTML migration
- [ ] Overview reviewed by project owner
- [ ] Step 07 i18n polish + GitHub Pages smoke-test
- [ ] Step 08 fill content from stakeholder replies
