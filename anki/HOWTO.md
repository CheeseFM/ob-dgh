# Anki-kaartjes & oefenpagina bijwerken

Alle kaartjes staan in deze map als Python-scripts. Eén keer bouwen geeft zowel de Anki-decks als de oefenpagina op de site.

## Eenmalig

```bash
pip install --user genanki pillow
```

## Bouwen

Altijd **vanuit deze map** draaien (de scripts gebruiken relatieve paden):

```bash
cd anki
python3 combine.py     # alle decks samen  → ../content/Source/Anki/DGH_Alle_hoofdstukken.apkg
python3 webexport.py   # oefenpagina       → ../content/Source/Oefenen/kaartjes.json + media/
```

Eén los deck opnieuw bouwen: `python3 h4.py`, `python3 so.py`, `python3 proc.py` of `python3 nato.py` → `../content/Source/Anki/DGH_<…>.apkg`.

## Wat staat waar

| Bestand | Inhoud |
|---|---|
| `h1.py` … `h12.py` | Kaartjes per hoofdstuk; foto's in `h<N>media/` |
| `so.py` | Staande orders: leest `content/Wiki/Staande Orders/O*.md` + extra kaartjes in de dict `X` |
| `proc.py` | Procedures: leest `content/Wiki/Procedures/P*.md` + kernstappen in de dict `K` |
| `nato.py` | NATO-alfabet |
| `dgh_common.py` | Note types (DGH Basic / DGH Cloze), CSS, `build()` |
| `mdparse.py` | Hulpfuncties om de Obsidian-markdown te lezen |
| `combine.py` | Alles in één `.apkg` |
| `webexport.py` | Zet alle kaartjes om naar JSON voor `oefenkaartjes.htm` |

## Een kaartje aanpassen of toevoegen

In `h<N>.py` is elk kaartje een tuple:

```python
("b", "sleutel", "Vraag?", "Antwoord", "Extra", ["H4", "H4::rea"])   # Basic
("c", "sleutel", "REA: {{c1::30}} compressies, {{c2::2}} beademingen.", "Extra", ["H4"])  # Cloze
```

- De **sleutel** moet uniek zijn per hoofdstuk en **nooit veranderen**: daarop is de vaste ID gebaseerd. Zo werkt Anki bij herimporteren het bestaande kaartje bij en blijft je voortgang behouden.
- Een foto: zet het bestand in `h<N>media/` en gebruik `<img src="dgh_h<N>_…png">` in de tekst. Voeg het bestand ook toe aan de `media`-lijst van dat script.
- Tags `examen` (of `H<N>::…::examen`) zorgen dat het kaartje verschijnt bij "enkel examenvragen" op de oefenpagina.

## Na het bouwen

- **Anki**: `DGH_Alle_hoofdstukken.apkg` gewoon opnieuw importeren (niet eerst verwijderen, anders ben je je voortgang kwijt).
- **Site**: de nieuwe `kaartjes.json` en `media/` gaan mee met de volgende Quartz sync.

## Oefenpagina

- `content/Oefenkaartjes.md` is een gewone Quartz-pagina met een `<iframe>` naar `content/Source/Oefenen/oefenkaartjes.htm`.
- Die pagina laadt `kaartjes.json`, neemt de kleuren, lettertypes en licht/donker-modus van de site over en past de hoogte van de iframe aan haar inhoud aan. Los geopend werkt ze ook.
- Linken naar één hoofdstuk: `[[Oefenkaartjes#H4|Online oefenkaartjes]]`, `[[Oefenkaartjes#staande-orders|…]]`, `[[Oefenkaartjes#procedures|…]]` (meerdere: `#H4,H5`).
- Extensie **`.htm`** is bewust: Quartz stript `.html` uit de naam van losse bestanden.
