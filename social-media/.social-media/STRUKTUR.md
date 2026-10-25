# STRUKTUR – System vs. Arbeitsergebnis

**Bei Installation**: `AGENT.md`, `.social-media/` (intern), `input/`, `archiv/`. Keine leeren Fach- oder Kanal-Ergebnisordner.

**Erst bei Auftrag, beispielhaft**:
```
social-media/
├── AGENT.md
├── .social-media/
├── input/
├── archiv/
├── strategie/
│   └── kanalstrategie.md
├── content/
│   └── cc-2026-0001/
│       ├── idee.md
│       ├── linkedin.md
│       ├── instagram.md
│       └── assets/
├── kalender/
│   └── 2026-11.csv
└── reports/
    └── 2026-11.md
```
- Das Datum/ID-Beispiel ist illustrative Struktur, kein echter Kundenauftrag.
- Methodenbeschreibung `.social-media/formate/reel.md` ist **kein** veröffentlichtes Reel und gehört nie in `content/`.
- Assets mit Quellnachweis, Lizenz- und Freigabestatus, Hash und Varianten dokumentieren. Nie benötigte Bild-/Video-Dateien bei Wechsel der Revision ungeprüft löschen.
- Kalender als CSV oder JSON, Daten UTF-8, ISO-8601 mit Zeitzone; keine parallelen divergierenden Kalenderwahrheiten. Kanäle können bei Bedarf Unterordner erhalten, müssen es aber nicht.
- Vor Änderung einer freigegebenen Fassung einen unveränderbaren Snapshot ins `archiv/`; Log- und History-Ereignis referenzieren dieselbe Revision.
- `input/` nur nach bestätigter Archivierung/Migration räumen; keine automatischen gefährlichen Bereinigungen.
