# Tatsächliche Wissensquellen und Reifegrade v0.1

## Reihenfolge für Versions- und Funktionsauskünfte

1. **Beobachtbare aktuelle Installation:** Welche Pfade, Skripte, Konfigurationsdateien, Testberichte und Schnittstellen sind tatsächlich vorhanden?
2. **Beobachtete Test- und Verbindungsresultate:** Wurde die Funktion in dieser Umgebung ausgeführt? Sind Datum, Auftrag und Ergebnis feststellbar?
3. **Aktuelle Root-Dokumentation:** `../../README.md`, `../../CHANGELOG.md`, `../../MIGRATION.md`, `../../AGENT.md`.
4. **Suite-Verträge:** `../../.suite/ARCHITECTURE.md`, `../../.suite/WORKFLOW.md`, `../../.suite/QUALITY.md`, `../../.suite/GOVERNANCE.md`, `../../.suite/MODULES.md` (nur vorhandene Dateien).
5. **Fachquellen:** `../../<modul>/AGENT.md`, Methodenindex, konkrete Methoden, ggf. Adapterdokumentation.
6. **Öffentliche Herstellerdokumentation:** Nur mit aktuellem Quellenzugriff und Datum; kein aus Erinnerung geschätzter API-Support.
7. **Allgemeines Fachwissen:** Als Erklärung, nicht als Behauptung über vorhandene Software.

## Reifegrade – niemals vermischen

- `documented`: Ein Text beschreibt die Fähigkeit.
- `implemented`: Eine konkrete lokale Implementierung wurde gefunden; noch kein Funktionsnachweis.
- `configured`: Eine benötigte Konfiguration ist erkennbar; sagt nichts über die Erreichbarkeit aus.
- `tested`: Ein nachprüfbarer erfolgreicher Test belegt **diesen konkreten Umfang**.
- `unavailable`: Eine konkrete Voraussetzung fehlt oder der Test ist fehlgeschlagen.
- `unknown`: Der aktuelle Stand konnte nicht geprüft werden.

Die Stufen sind keine strenge Fortschrittsleiter; eine API kann dokumentiert und konfiguriert, aber aktuell unerreichbar sein. Ein altes Testergebnis belegt nicht die Funktion heute. Eine Datei namens `publisher.py` belegt noch keine erfolgreiche Veröffentlichung.

## Ausgangsstand für dieses Paket

Das öffentliche GitHub-README beschrieb am **27.10.2026** die Suite **v0.2.1**, neun integrierte Module (einschließlich `e-commerce/`) und 477 Methodendateien. **Dies ist eine datierte Referenz, keine permanente Versionsgarantie.** `branding/` und `business-dna/` existieren als getrennte Entwicklungspakete und werden nur genannt, wenn sie in der konkreten Installation gefunden werden.

Quelle: https://github.com/markus-ertel/agentic-marketing-suite und dortige `README.md`.

## Integration in diese Arbeitskopie

Der oben genannte v0.2.1-Ausgangsstand ist historisch. Suite v0.2.4 integriert Branding, Business-DNA und Help. Die ursprünglichen Paketangaben bleiben als historischer Kontext erhalten. Für aktuelle Modul-/Methodenzahlen das vorhandene Root-README und `scan_workspace.py` verwenden; keine Zahl als allgemeine Installationsvoraussetzung behandeln. Die Implementierungen und deren Konfiguration/Testumfang jeweils gesondert prüfen. Konkrete Verfahren: [SUITE.md](SUITE.md).
