# Step 07 — i18n and nav

## Goal

Make multipage navigation and locales consistent across PT/EN/FR/AR, including RTL and the El Fadhi spelling fix.

## Prerequisites

- [x] Step 06 structure done
- [x] Signatory spelling confirmed (Kamal El Fadhi)

## Inputs

- `locales/*.json`
- `js/i18n.js`
- Nav labels from Step 02
- Placeholder strings from Step 05

## Tasks

- [x] Add locale keys for new nav items and placeholder pages
- [x] Fix `Kamal El-Fehdi` → `Kamal El Fadhi` (Latin locales)
- [x] Align Arabic signatory to `كمال الفاضي` (from `الفهدي`)
- [x] Ensure language switcher keeps path + `?lang=` on every page (URL + link navigation)
- [x] Add `hreflang` / canonical / `x-default` per page (build script)
- [x] Verify Arabic RTL on nested routes (`/historia/reaa/?lang=ar`)
- [x] Mobile menu: primary (7) in header; secondary in footer; `aria-expanded` + close on Esc/outside/link

## Decisions

| Topic | Choice |
|-------|--------|
| Latin spelling | **Kamal El Fadhi** (space, no hyphen) |
| Arabic form | **كمال الفاضي** (aligned to Fadhi; confirm with stakeholders if a preferred Arabic spelling differs) |
| Lang persistence | `?lang=` in URL + `localStorage`; internal same-origin links keep `lang` |
| Secondary nav | Footer only (Comunicações · Declaração · Regulamento) — not in primary / mobile drawer |

## Deliverables

- Locale keys aligned (PT/EN/FR/AR)
- `hreflang` + canonical on generated pages
- Nav complete in four languages
- RTL usable on nested routes

## Acceptance criteria

- [x] No missing i18n keys on new pages
- [x] Spelling corrected site-wide (Latin + aligned AR)
- [x] AR layout usable on `/historia/reaa/` depth

## Status

`done` (2026-08-04)

## Next

→ Step 04 stakeholder replies (content) and/or Step 08 fill content  
→ Step 10 launch checklist when content freeze approaches
