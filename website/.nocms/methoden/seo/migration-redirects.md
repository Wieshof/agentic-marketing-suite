# SEO-sichere Migration und Weiterleitungen
**noCMS-Fachmethode · seo · v0.2**

## Ziel und fachlicher Nutzen
Verlust von URLs und Inhalten bei Relaunch/Migration minimieren.

## Wann diese Methode wählen?
Domainwechsel, Seitenzusammenlegung, Relaunch.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Alte URL-Liste, neue Seitenstruktur, Analytics/Search Console soweit verfügbar.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Alle bekannten alten URLs und wichtige interne Verlinkungen inventarisieren.
2. Jeder alten relevanten URL eine inhaltlich passende Ziel-URL oder eine begründete Ausnahme zuordnen.
3. Permanente/temporäre Weiterleitungen passend zur tatsächlichen Migration planen.
4. Canonical, Sitemap, interne Links und hreflang auf neuen Zustand abstimmen.
5. Nach Veröffentlichung Stichproben und Fehlerlisten mit tatsächlichem Zugriff prüfen.

## Konkrete Beratungsleistung / Ergebnis
Redirect-Tabelle, Checkliste Vor-/Nach-Release, bekannte Risiken.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Keine pauschalen Weiterleitungen aller URLs auf die Homepage.
- Nicht als durchgetestet markieren, wenn Serverzugriff fehlt.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
