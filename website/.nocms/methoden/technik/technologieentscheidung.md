# Technologie- und Hostingberatung
**noCMS-Fachmethode · technik · v0.2**

## Ziel und fachlicher Nutzen
Die kleinste geeignete technische Lösung ohne unnötigen Lock-in wählen.

## Wann diese Methode wählen?
Fragen zu CMS, Hosting, Framework, statischer Site, Wartbarkeit.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Website-Funktionen, Inhaltsänderungen, Budget, technische Zuständigkeit.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Anforderungen nach rein statischen Inhalten, Formular-/Integrationsbedarf und echten serverseitigen Funktionen gruppieren.
2. Einfaches noCMS-HTML/CSS/JS mit CMS-/Framework-Alternativen vergleichen, wo relevant.
3. Kosten, Datenschutz, Performance, Migration, Sicherheit und Vendor-Lock-in abwägen.
4. Hosting-, Domain-, SSL- und Backupanlage mit Verantwortungen skizzieren.
5. Eine begründete Empfehlung aussprechen; nicht reflexhaft zusätzliche Runtime einführen.

## Konkrete Beratungsleistung / Ergebnis
Technikentscheidung mit Trade-offs und minimalem Betriebsmodell.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Kein static-only Versprechen bei echten Serverfunktionen.
- Keine nicht geprüften Hostingpreise oder garantierten SLAs.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
