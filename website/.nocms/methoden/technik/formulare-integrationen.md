# Formulare und Schnittstellen
**noCMS-Fachmethode · technik · v0.2**

## Ziel und fachlicher Nutzen
Kontakt- und Interaktionsfunktionen sinnvoll, zugänglich und datensparsam konzipieren.

## Wann diese Methode wählen?
Kontakt, Newsletter, Terminbuchung, CRM-Anbindung oder API.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Gewünschte Nutzeraktion, Datenbedarf, Drittanbieter, Rechte/Freigaben.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Prüfen, ob eine einfache E-Mail-Verknüpfung statt Formular genügt.
2. Felder minimieren, Validierung, Fehlertexte, Sicherheitsmaßnahmen und Tastaturbedienung spezifizieren.
3. Datenfluss, Speicherung, Rechtsgrundlage und Anbieterzugriffe darstellen.
4. Fallback bei Ausfall und Spam-/Missbrauchsschutz planen.
5. Erst nach Autorisierung Integration entwickeln und tatsächlich testen.

## Konkrete Beratungsleistung / Ergebnis
Interaktionsspezifikation mit Datenfluss und Testfällen.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Keine Tokens in HTML oder Dokumentation ablegen.
- Keine externe Übermittlung durch bloße Konzeptarbeit.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
