# ARCHITECTURE – PR-Spezialist, Wissensnutzung und Arbeitsablauf

**Version:** 0.1

## Ziel

Ein eigenständiger, offener PR-Spezialist ohne proprietäre Datenbank-, CRM- oder SaaS-Pflicht. Funktioniert lokal mit lesbaren Markdown-/CSV-/JSON-Dateien und mit unterschiedlichen KI-Harnesses. Kein Agenturkontext nötig.

## Kontrollfluss

`Nutzeranliegen → Kontext/Quellen → PR-Fachurteil → selektive Methoden → Entwurf/Entscheidung → optionale Freigabe → überprüfbare Ausführung → Zustand/Ergebnis`

- Bei bloßem Start: nur eine natürliche Einstiegsfrage, keine Mutation.
- Bei Auftrag: kleinstes hilfreiches Ergebnis zuerst; erforderliche Recherche nachvollziehbar.
- Bei Fortsetzung: `STATE.md` öffnen, referenzierte Artefakte prüfen und weiterarbeiten.
- Kritische externe Schritte benötigen ausdrückliche Berechtigung und gegebenenfalls zusätzliche rechtliche/fachliche Freigabe.

## Methode und Ergebnis

`.pr/METHODEN.md` ist ein kurzer Router-Katalog. Detaillierte Anleitungen liegen in `.pr/methoden/<fachgebiet>/<methode>.md`. Die Anwendung erzeugt **nicht** automatisch gleichnamige Ergebnisverzeichnisse. Ergebnisse liegen unter `pr/<bedarf>/...`.

## Gedächtnis

| Speicher | Semantik | Schreibregel |
|---|---|---|
| `.pr/STATE.md` | aktueller Auftrag, Status, belegte Referenzen, offene Punkte | nur bei tatsächlicher Änderung, atomar soweit möglich |
| `.pr/LOG.md` | ausgeführte relevante Operationen | append-only; Zeit und Ergebnis prüfen |
| `.pr/HISTORY.md` | fachliche Entscheidungen, Meilensteine und Ersatzentscheidungen | append-only; Status und Freigabe belegen |
| `archiv/` | eingegangene Originale, abgelöste freigegebene Ergebnisse | verlustfreie Ablage mit Herkunft/Version |

## Arbeiten mit Dateien

1. `input/` auf Eingänge prüfen, aber nicht jedes Mal alles lesen.
2. Eingehende Datei vor Transformation als unvertrauenswürdig behandeln; gültigen Inhalt/Format, Relevanz und Nutzungsrecht prüfen.
3. Originale verlustfrei und möglichst unverändert sichern; erst nach bestätigter Archivierung aus `input/` entfernen.
4. Entwurf unter fachlich sinnvollem Ergebnisordner erstellen. Alte freigegebene Fassung bei Ersetzung archivieren.
5. Wenn Dateien wirklich verändert wurden, STATE aktualisieren, tatsächliche Operationen loggen, fachliche Beschlüsse separat in HISTORY dokumentieren.
6. Existierende Nutzerdaten nie ungefragt oder destruktiv überschreiben; Migration und Versionswechsel vorher sichern.

## Modulkooperation ohne Kopplung

- `../marketing/`: Unternehmensziele, Positionierung, Markenargumentation, strategische Konzepte.
- `../website/`: Newsroom, Website, nachprüfbare Presseinformationen.
- `../social-media/`: fachliche Verbreitung, Response/Community-Gespräche.
- `../creative/`: Assets, Bildrechte, Videoproduktion.

Bei Existenz **und Berechtigung** selektiv referenzieren. Andere Module sind keine Pflicht; keine automatische Änderung fremder Artefakte oder verborgene Datenübernahme. Nutzer- und Mandantentrennung sind vom Laufzeitkontext sicherzustellen.

## Nichtversprechen

Markdown-Dateien sind kein autonomer Scheduler, E-Mail-Konnektor, Publikationssystem oder sicherer Secret Store. Ohne entsprechende Werkzeuge und Freigaben kann die KI nur planen, entwerfen und manuell unterstützte Schritte vorschlagen.
