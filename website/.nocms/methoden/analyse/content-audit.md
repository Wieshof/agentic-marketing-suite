# Content-Audit und Bestandsübernahme
**noCMS-Fachmethode · analyse · v0.2**

## Ziel und fachlicher Nutzen
Bestehende Inhalte klassifizieren und migrationsfähig machen.

## Wann diese Methode wählen?
Redesign, Migration, große Überarbeitung.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Site-Dateien, URLs, Contentinventar, Nutzungsrechte, Metriken soweit verfügbar.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Seiten, Medien, Texte und Downloads inventarisieren inklusive URLs und Sprache.
2. Inhalte nach Zielbeitrag, Aktualität, Quellenlage, Autorisierung und Redundanz markieren.
3. Entscheidung je Inhalt treffen: behalten, verbessern, zusammenführen, entfernen, prüfen.
4. Abhängigkeiten zu Navigation, Suchmaschinen-URLs, Weiterleitungen und Linkstruktur erfassen.
5. Kritische Originale und Quellen dokumentieren; Ausgabeversionen von Originalen trennen.

## Konkrete Beratungsleistung / Ergebnis
Content-Matrix mit Behaltens-/Änderungsentscheidungen und Risiken.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Alte URLs/Downloads nicht ohne Redirect-Plan löschen.
- Unklare Bild-/Schriftrechte nicht als geklärt markieren.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
