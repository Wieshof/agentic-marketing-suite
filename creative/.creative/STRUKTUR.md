# STRUKTUR – dynamische Projektablage

Minimalbestand bei Installation: `AGENT.md`, `.creative/`, `input/`, `archiv/`. Keine leeren Ergebnisbereiche.

Beispiel bei einem Plakatauftrag:
```text
creative/
├── AGENT.md
├── .creative/                 # System, Methoden, Status, Historie
├── input/                     # temporäre Übergabe, nicht das dauerhafte Assetlager
├── archiv/                    # Originale, frühere freigegebene Versionen
└── plakat-herbstkampagne/     # entsteht erst durch einen echten Auftrag
    ├── briefing.md
    ├── creative-job.json
    ├── assets/                 # lizenziert, Herkunft dokumentiert
    ├── source/                 # editierbare SVG/SLA/IDML etc.
    ├── proof/                  # visueller Prüfauszug, nicht Druckfreigabe
    ├── export/                 # tatsächliche Ausgaben
    └── qa/                     # Preflight- und Sichtprüfung
```

`input/`: Übergebenes Material erst nach **vollständiger Prüfung, Sicherung und Referenzierung** umlegen/leeren; nie blind löschen. `archiv/`: Originaldateien und abgelöste Freigabestände getrennt mit Provenienz. Freigegebene Releases mit Hash und Entscheidung archivieren. Vorhandene fremde Projektdateien nie überschreiben.

Verboten: ein pauschales neues `bilder/`, `video/` etc. ohne Auftrag, ein unübersichtlicher Sammeleimer oder eine permanente Duplikation der Markenassets in jedem Projekt.
