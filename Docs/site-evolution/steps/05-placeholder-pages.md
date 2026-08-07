# Step 05 — Placeholder pages

## Goal

Define the shared placeholder pattern and which routes ship as stubs vs real content in the first multipage release.

## Prerequisites

- [x] Step 02 routes frozen
- [x] Step 04 questionnaire ready (replies optional before HTML)

## Status

`done` (2026-08-04) — ready for Step 06 implementation

---

## Tasks

- [x] Agree PT placeholder strings; EN/FR/AR in Step 07
- [x] Classify each public route
- [x] Confirm Chat / Biblioteca / Loja omitted
- [x] Draft HTML wire structure (spec only)
- [x] Canonical PT copy below (+ section specs aligned)

---

## Decisions (frozen)

| Decision | Choice |
|----------|--------|
| Eventos: Lyon / Lisboa dates | **Not** on Eventos until Step 04 approves. Keep those facts on História / Confederação / Documentos only. |
| Empty “Membros” (non-founders) | Show **empty-state** block (not “Em preparação”) — honest “nenhum adicional publicado” |
| 1762 / 1786 | Summary + **Em preparação** (no external link until approved) |
| Status wording | Public gaps: **Em preparação** only (no “Acesso reservado” in this phase) |
| CSS | Reuse existing tokens; add minimal `.status-block` / `.page-hero` in Step 06 if needed |

---

## Classification (final)

| Route | Treatment | Notes |
|-------|-----------|-------|
| `/` | **portal** | Hero + area grid with status |
| `/confederacao/` | migrate | existing `confederation.*` |
| `/principios/` | migrate | pillars + declaração |
| `/membros/` | migrate + empty-state | Fundadores list; Membros empty-state |
| `/historia/` | migrate structure | index linking 3 threads |
| `/historia/confederacao/` | **seed** | from existing history + Regulamento facts |
| `/historia/supremos-conselhos/` | placeholder | |
| `/historia/reaa/` | placeholder | |
| `/documentos/` | migrate | cards (Declaração, Regulamento, 1762, 1786) |
| `/documentos/regulamento-interno/` | migrate thin | meta + PDF link |
| `/documentos/1762/` | placeholder | summary formula Step 03 |
| `/documentos/1786/` | placeholder | summary formula Step 03 |
| `/eventos/` | placeholder | Anteriores / Agendadas empty |
| `/comunicacoes/` | placeholder | |
| `/contactos/` | migrate | form; contacts when available |

Omit: `/chat/`, `/biblioteca/`, `/loja/`

---

## Shared placeholder pattern

### Visual / content blocks

1. **Page header** — `overline` + `h1` (section name)  
2. **Purpose** — one short paragraph  
3. **Status block** — bordered paper box: label **Em preparação** + optional “O que virá” bullets (no fake data)  
4. **Actions** — text links: parent index · Contactos · (optional) Documentos / Princípios  

### Suggested markup (Step 06)

```html
<main class="section section-light">
  <div class="section-title">
    <p class="overline" data-i18n="…">…</p>
    <h1 data-i18n="…">…</h1>
  </div>
  <p class="lead" data-i18n="…">…</p>
  <aside class="status-block" aria-live="polite">
    <p class="status-label" data-i18n="status.preparing">Em preparação</p>
    <p data-i18n="…">…</p>
    <!-- optional ul -->
  </aside>
  <p class="page-actions">
    <a href="../contactos/">…</a>
    ·
    <a href="../">…</a>
  </p>
</main>
```

Reuse: `page-frame`, `site-header`, `site-footer`, `section-light` / `section-warm`, `lead`, `button` where useful.  
New CSS (minimal): `.status-block` — paper background, gold-dark double border, burgundy status label (match declaration restraint).

---

## Canonical PT copy

### Shared chrome keys (Step 07)

| Key idea | PT |
|----------|-----|
| Status preparing | Em preparação |
| Status empty members | Nenhum membro adicional publicado |
| Portal ready | Disponível |
| Portal preparing | Em preparação |
| Back home | Página inicial |
| Contact link | Contactos |

---

### `/comunicacoes/`

**Overline:** Comunicações  
**Title:** Comunicações oficiais  
**Lead:** Espaço destinado às comunicações da Confederação, incluindo o Discurso do Presidente.  
**Status:** Em preparação  
**Will include (bullets):** Discurso do Presidente · Comunicados institucionais · (futuro) Boletim digital  
**Actions:** Contactos · Página inicial  

---

### `/eventos/`

**Overline:** Agenda  
**Title:** Eventos e reuniões  
**Lead:** Calendário das Assembleias Confederais, encontros institucionais e reuniões relevantes da Confederação.  
**Status:** Em preparação  

**Block Anteriores:**  
> Os eventos públicos anteriores serão publicados aqui após validação.  

**Block Agendadas:**  
> As datas futuras confirmadas serão anunciadas nesta secção.  

**Actions:** Contactos · História · Página inicial  

*(Do not list Lyon/Lisboa here until approved.)*

---

### `/historia/supremos-conselhos/`

**Overline:** História  
**Title:** Supremos Conselhos  
**Lead:** Enquadramento histórico geral da instituição dos Supremos Conselhos no R.E.A.A.  
**Status:** Em preparação  
**Note:** Apenas conteúdos validados pela Confederação serão publicados.  
**Actions:** História · Membros · Página inicial  

---

### `/historia/reaa/`

**Overline:** História  
**Title:** Rito Escocês Antigo e Aceite  
**Lead:** Percurso histórico do R.E.A.A. e das leis fundamentais de 1762 e 1786, no respeito pela tradição regular.  
**Status:** Em preparação  
**Note:** Texto de enquadramento em preparação; ver também Documentos e a Declaração de Princípios.  
**Actions:** História · Documentos · Princípios  

---

### `/documentos/1762/`

**Overline:** Documentos fundadores  
**Title:** Constituições e Regulamentos de 1762  
**Lead:** Textos fundamentais da Ordem referidos no Regulamento Interno (Art. 2.º) e na Declaração de Princípios.  
**Status:** Em preparação  
**Note:** A edição pública a disponibilizar (ou a ligação oficial) será publicada após validação da Confederação. Existem várias edições históricas.  
**Actions:** Documentos · Princípios  

---

### `/documentos/1786/`

**Overline:** Documentos fundadores  
**Title:** Grandes Constituições de 1786  
**Lead:** Textos fundamentais da Ordem referidos no Regulamento Interno (Art. 2.º) e na Declaração de Princípios.  
**Status:** Em preparação  
**Note:** A edição pública a disponibilizar (ou a ligação oficial) será publicada após validação da Confederação. Existem várias edições históricas.  
**Actions:** Documentos · Princípios  

---

### `/membros/` — empty state (not status “Em preparação”)

**Heading:** Membros  
**Text:** Além dos Supremos Conselhos fundadores, futuros membros admitidos conforme o Regulamento Interno serão apresentados nesta secção.  
**Status line:** Nenhum membro adicional publicado.  

---

### `/historia/confederacao/` — seed (not placeholder)

**Overline:** História  
**Title:** A Confederação  
**Body (PT seed):**  
A Confederação Internacional dos Supremos Conselhos Soberanos e Regulares do R.E.A.A. foi criada por tratado assinado em Lyon a 12 de dezembro de 2025 entre o Supremo Conselho Português, o Supremo Conselho de Marrocos, o Supremo Conselho do Brasil e o Supremo Conselho para a França. O Regulamento Interno foi adotado em Lisboa a 4 de julho de 2026. A presidência é rotativa por períodos de três anos entre os membros fundadores, pela ordem: Portugal, Marrocos, Brasil, França.  

---

### Portal `/` — area grid (PT labels)

| Area | Href | Badge |
|------|------|-------|
| Confederação | confederacao/ | Disponível |
| Princípios | principios/ | Disponível |
| Membros | membros/ | Disponível |
| História | historia/ | Disponível |
| Documentos | documentos/ | Disponível |
| Eventos | eventos/ | Em preparação |
| Comunicações | comunicacoes/ | Em preparação |
| Contactos | contactos/ | Disponível |

---

## Documentos index cards (target)

| Card | Link | Meta |
|------|------|------|
| Declaração de Princípios | ../principios/#declaracao | Texto · Disponível |
| Regulamento Interno | regulamento-interno/ | PDF · Disponível |
| Constituições de 1762 | 1762/ | Em preparação |
| Grandes Constituições de 1786 | 1786/ | Em preparação |

(Replace old “Comunicados · Em breve” card with Comunicações in footer, not a fake docs card.)

---

## Acceptance criteria

- [x] Every first-release route has a treatment  
- [x] Canonical PT copy defined  
- [x] No lorem / fake events / fake shop  
- [x] Wire structure specified for Step 06  

## Next

→ [`06-multipage-migration.md`](06-multipage-migration.md)
