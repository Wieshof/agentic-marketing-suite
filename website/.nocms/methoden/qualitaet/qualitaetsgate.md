# Website-Abnahme und Release-Qualität
**noCMS-Fachmethode · qualitaet · v0.2**

## Ziel und fachlicher Nutzen
Für Website-Änderungen prüfbare Akzeptanzkriterien erstellen.

## Wann diese Methode wählen?
Neue Website, Relaunch, größerer Änderungsauftrag.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Bestätigtes Briefing, Seiteninventar, Testwerkzeuge, Releaseziel.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Akzeptanzkriterien an Businessziel, Seitenfunktion und bekannte Risiken binden.
2. Funktion, mobile Darstellung, Zugänglichkeit, Links, Performance, Datenschutz und Inhaltsfreigabe systematisch ordnen.
3. Tatsächliche Testabdeckung dokumentieren und ungeprüfte Bereiche sichtbar machen.
4. Blockierende Probleme und Freigaben getrennt behandeln.
5. Release-Paket aus `site/` erst nach Berechtigung und Prüfungen erstellen; Veröffentlichung gesondert verifizieren.

## Konkrete Beratungsleistung / Ergebnis
Abnahmeprotokoll mit bestanden/nicht bestanden/nicht geprüft.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Kein „alles geprüft“ ohne Nachweis.
- Kein Deployment durch eine bloße Empfehlung.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
