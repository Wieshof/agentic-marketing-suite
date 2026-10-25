# STRUKTUR – Installation und dynamische Ergebnisse

**Version:** 0.4

## Minimalstruktur

```text
marketing/
├── AGENT.md                 # sichtbarer Einstiegspunkt
├── .marketing/              # interne Anweisungen, Methoden, Status
│   ├── BERATUNG.md
│   ├── RULES.md
│   ├── ARCHITECTURE.md
│   ├── STRUKTUR.md
│   ├── METHODEN.md
│   ├── methoden/             # statische fachliche Anleitungen
│   ├── STATE.md             # aktueller Zustand
│   ├── LOG.md               # operative Ereignisse
│   └── HISTORY.md           # fachliche Entscheidungen
├── input/                   # temporärer Eingang, regulär leer
└── archiv/                  # Originale/Freigaben, Unterordner bei Bedarf
```

Unterhalb von `marketing/` werden **keine Fach-Ergebnisordner vorab angelegt**. Der interne Methodenbaum ist die einzige feste fachliche Ordnerstruktur. `input/` und `archiv/` dienen dem Materialfluss; sie sind keine Projektergebnisbereiche.

## Beispiel (erst nach echtem Arbeitsauftrag!)

```text
marketing/
├── AGENT.md
├── .marketing/
├── input/
├── archiv/
├── strategie/
│   └── positionierung.md   # ausgearbeitete Positionierung eines Unternehmens
├── ziele/
│   └── markenbekanntheit.md
└── kampagnen/
    └── produktstart/
        └── konzept.md
```

`.marketing/methoden/strategie/positionierung.md` erklärt dagegen **wie** eine Positionierung entwickelt wird. `marketing/strategie/positionierung.md` enthält **das Ergebnis**. Diese Dateien sind absichtlich getrennt.

## Ablageregeln

- Pfade möglichst kurz, sprechend und ohne personenbezogene Details; einheitliche lowercase Dateinamen.
- Neue Artefakte als Markdown oder ein fachlich besser geeignetes offenes Format ablegen.
- Kein leerer Ordner allein als Beleg einer geplanten Aktivität.
- Relevante neue Ergebnisdateien in `STATE.md` verlinken. Fachliche Freigaben/Versionen nach `HISTORY.md` und erforderlichenfalls `archiv/` dokumentieren.
- Rohmaterial nicht stillschweigend überschreiben; unsicheres Material isoliert prüfen.
- Nach Abschluss von Projekten Ordner nicht automatisch löschen; Freigaben und referenzierte Ergebnisse müssen erhalten bleiben.
- Geschwistermodule (`../website/`, `../social-media/`) bleiben unabhängige Arbeitsbereiche; nur explizit zugängliche Informationen referenzieren.

## Eingangsablauf

1. Datei in `input/` erkennen, als Quelle behandeln und prüfen.
2. Import/Zuordnung in eine sinnvolle Ergebnisakte vornehmen (falls erforderlich).
3. Original unter `archiv/` unverändert sichern und Sicherung überprüfen.
4. Erst danach importiertes Material aus `input/` entfernen, wenn ausdrücklich/regelbasiert berechtigt.
5. Relevanten Vorgang dokumentieren; bei Fehler Material behalten und Fehler melden.

Weitere Ergebnisordner dürfen frei entstehen – die Liste der Beispiele ist keine starre Taxonomie.
