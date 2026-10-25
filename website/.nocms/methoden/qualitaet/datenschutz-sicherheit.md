# Website-Datenschutz und Sicherheitsrisiken
**noCMS-Fachmethode · qualitaet · v0.2**

## Ziel und fachlicher Nutzen
Datenflüsse und typische Webrisiken erkennen und an zuständige Prüfung übergeben.

## Wann diese Methode wählen?
Formulare, Analytics, Drittinhalte, Cookies, öffentliche Veröffentlichung.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Seiten/Code, Provider, Datenfluss, Märkte, eingebundene Dienste.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Alle Drittaufrufe, Cookies/Storage, personenbezogenen Dateneingaben und Datenempfänger erfassen.
2. Notwendigkeit, Datenminimierung, Einwilligung/sonstige Rechtsgrundlage und Transparenzbedarfe markieren.
3. XSS/Injection, Dateiupload, CSP, HTTPS, Security Headers und Secret Exposure im verfügbaren Umfang prüfen.
4. Konkrete Abhilfen nach Risiko und Aufwand priorisieren.
5. Offene rechtliche/technische Prüfpflichten ausdrücklich benennen.

## Konkrete Beratungsleistung / Ergebnis
Risikoliste, Datenflussmatrix und Prüfaufträge.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Keine Rechtskonformität ohne konkrete Rechtsprüfung behaupten.
- Keine pauschal sichere Einwilligungsbehauptung aus bloßem Bannerdesign.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
