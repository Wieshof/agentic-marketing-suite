# Performance und Core Web Vitals
**noCMS-Fachmethode · qualitaet · v0.2**

## Ziel und fachlicher Nutzen
Spürbare Lade- und Interaktionsprobleme lokalisieren und pragmatisch beheben.

## Wann diese Methode wählen?
Langsame Site, Core Web Vitals, Launch-Audit.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Site, Bildformate, Fonts, Scripts, reale Feld-/Labordaten wenn vorhanden.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Page-Load- und Interaktionsszenarien auf Mobile/Desktop erfassen.
2. Bilder, Schriften, Rendering-Blocker, Skripte und Ressourcen priorisiert untersuchen.
3. Feld- und Labordaten sauber unterscheiden; konkrete Metrikquelle und Zeitpunkt notieren.
4. Größte technische Ursachen zuerst reduzieren: richtige Bildgrößen, Lazy-Loading, Caching, CSS-/JS-Umfang.
5. Nach Fixes erneut messen und Vorher-/Nachhervergleich mit Messbedingungen dokumentieren.

## Konkrete Beratungsleistung / Ergebnis
Priorisierte Performance-Maßnahmen mit Evidenz und Messplan.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Keine erfundenen Lighthouse- oder CWV-Werte.
- Keine generelle externe CDN-Pflicht für Geschwindigkeit.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
