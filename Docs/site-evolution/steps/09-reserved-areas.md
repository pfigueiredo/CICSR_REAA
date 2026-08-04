# Step 09 — Future work (Chat, private areas, Loja)

## Status

`deferred` — **not part of the HTML multipage phase**

## Goal

Park product decisions for areas that need more than static HTML (auth, messaging, commerce, or private libraries). Revisit after the public multipage site ships.

## Explicitly out of this phase

| Area | Why not now |
|------|-------------|
| Chat (3 níveis) | Requires identity, access control, and a messaging stack |
| Private / members-only areas | Same — not GitHub Pages static alone |
| Loja | Catalogue, payments, fulfilment |
| Biblioteca (members-only) | Uploads + auth; public PDF list can be reconsidered later as plain HTML under Documentos |

## Decision record (fill when revisiting)

| Area | Choice | Rationale | Nav | Next tech step |
|------|--------|-----------|-----|----------------|
| Chat | deferred | Focus on public HTML site first | omit | TBD |
| Biblioteca | deferred | Scope TBD | omit | TBD — or fold public PDFs into Documentos |
| Loja | deferred | No commerce mandate | omit | TBD |

## Tasks (future — do not block Step 06)

- [ ] Choose Chat: external messenger only / in-site later / both
- [ ] Choose Biblioteca: public PDF archive (HTML) vs members-only vs defer
- [ ] Choose Loja: none / publications / merch
- [ ] Spec hosting + auth if anything leaves static Pages
- [ ] Only then add routes and nav

## Relationship to HTML phase

- No `/chat/`, `/biblioteca/`, `/loja/` routes in Step 02 / 05 / 06.
- Stakeholder questions about these can wait; public content questions stay in Step 04.
- External messenger group from `Docs/specs.txt` I (WhatsApp/Telegram/Signal) is an **organisational** channel, not a site feature in this phase.

## Acceptance criteria (for later)

- No fake chat UI or shop on the public site
- When resumed, update README status from `deferred` → `todo`
