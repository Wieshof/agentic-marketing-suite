# Schlankes Web-Designsystem
**noCMS-Fachmethode · design · v0.2**

## Ziel und fachlicher Nutzen
Konsistente Styles und Komponenten ohne unnötiges Framework schaffen.

## Wann diese Methode wählen?
Mehrere Seiten, wiederholte Bausteine, Gestaltungsdrift.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Corporate Design, bestehende CSS/HTML-Dateien, gemeinsame Komponenten.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Design-Tokens für Farben, Schrift, Abstände, Radien und Zustände definieren.
2. Wiederkehrende Bausteine wie Navigation, Buttons, Karten, Formulare inventarisieren.
3. HTML-Semantik, Fokuszustände, responsive Verhalten und Varianten pro Komponente beschreiben.
4. Bausteine auf bestehende `shared/`- und CSS-Konventionen abstimmen.
5. Eine Dokumentation erstellen, mit der neue Seiten ohne Stilbruch gebaut werden.

## Konkrete Beratungsleistung / Ergebnis
Token-/Komponentenregister und konkrete Style-Regeln.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Nicht bei kleiner Website komplexe Komponentenbibliothek erzwingen.
- In `site/` keine Build- oder Runtime-Pflicht einführen.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
