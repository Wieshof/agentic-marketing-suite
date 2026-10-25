# Barrierefreiheit und WCAG-Beratung
**noCMS-Fachmethode · qualitaet · v0.2**

## Ziel und fachlicher Nutzen
Zugänglichkeit fachlich prüfen und Verbesserungen priorisieren.

## Wann diese Methode wählen?
Neubau, Audit, besonders interaktive Seiten, E-Commerce.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Site/URL, Nutzerinteraktionen, Zielmarkt, gesetzlicher Anwendungsbereich.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Geltungsbereich rechtlicher Anforderungen ermitteln; für Österreich BaFG je Dienstleistungsart prüfen, nicht pauschal jede Website gleichsetzen.
2. Semantik, Kontrast, Tastatur, Fokus, Zoom/Reflow, Fehlerhinweise, Formularnamen, Alternativtexte und Medienalternativen prüfen.
3. Automatische Checks mit manueller Tastatur- und Screenreaderprüfung kombinieren, soweit Werkzeuge/Kompetenz vorhanden.
4. Befunde anhand konkreter WCAG-2.2-Erfolgskriterien zuordnen, Schwere und Nutzerwirkung nennen.
5. Nach Verbesserungen re-testen; nicht durch eine Checkliste volle Konformität bescheinigen.

## Konkrete Beratungsleistung / Ergebnis
Prüfmatrix mit WCAG-Bezug, Belegen, Prioritäten und bekannten Testgrenzen.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- BaFG gilt nicht automatisch für jede reine Infowebsite; maßgeblichen Fall prüfen.
- Ein Automated-Score reicht nicht als Konformitätsnachweis.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
