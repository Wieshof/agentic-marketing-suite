# Nutzerführung und User Flows
**noCMS-Fachmethode · konzeption · v0.2**

## Ziel und fachlicher Nutzen
Kritische Aufgabenwege auf wenige verständliche Schritte reduzieren.

## Wann diese Methode wählen?
Anfrage/Buchung/Download/Kontakt soll funktionieren.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Nutzeraufgabe, Einstiegsseite, benötigte Daten und tatsächliche Site-Funktion.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Einstiegspunkte inklusive Direktaufruf und Suche benennen.
2. Idealen kürzesten Weg zur Zielhandlung skizzieren, inklusive Alternative ohne Formular.
3. Fehlerzustände, Barrieren, Mobilnutzung, Tastatur und Datenschutz berücksichtigen.
4. Unnötige Pflichtfelder und Verzweigungen entfernen.
5. Akzeptanzfälle für den Weg definieren (erfolgreich, Abbruch, Fehlermeldung).

## Konkrete Beratungsleistung / Ergebnis
Einfacher Ablaufdiagrammtext, Fehlerfälle und UX-Empfehlung.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Keine nicht vorhandenen Backend-Funktionen als vorhanden beschreiben.
- Kontaktmöglichkeiten sollen auf Wunsch niedrigschwellig bleiben.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
