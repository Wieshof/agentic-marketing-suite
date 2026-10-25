# A/B-Ergebnisse interpretieren
**Datei:** `.analytics/methoden/experimente/ab-test-analyse.md`  
**Einsatz:** Experiment abgeschlossen wurde  
**Ergebnis:** Testauswertung mit Go/No-Go-Empfehlung

## Beratungsauftrag
Übernimm die fachliche Arbeit selbst. Stelle keine methodischen Prüfungsfragen an den Nutzer. Wenn entscheidende Angaben fehlen, arbeite mit ausgewiesenen Hypothesen und klarer Unsicherheit, statt Fakten zu erfinden. Entscheide zuerst, ob diese Methode für den konkreten Auftrag überhaupt notwendig ist.

## Konkretes Vorgehen
1. Prüfe Randomisierung, SRM und Datenvollständigkeit.
2. Berechne Effekt und geeignetes Intervall.
3. Bewerte Guardrails und praktische Relevanz.
4. Empfiehl Einführung, Folgetest oder Nichtentscheidung.

## Notwendige Nachweise
- Nenne Datenquelle, Erhebungs-/Extraktionszeit, Zeitfenster, Segmente, Zähler/Nenner sowie Vergleichsbedingungen, soweit für die Methode relevant.
- Kennzeichne Datenlücken, geringe Fallzahlen, Schätzwerte und Berechnungsschritte explizit.
- Liefere ein **verwendbares Ergebnis** und mindestens eine begründete Verbesserungsempfehlung oder explizit „keine Handlung begründbar“.

## Fachlicher Fallstrick und Gegenprüfung
**Achtung:** Statistische Signifikanz garantiert weder Kausalität bei Fehlerdesign noch Geschäftswert.
Prüfe mindestens eine plausible Gegenhypothese. Unterscheide statistische Beobachtung, Erklärung und kausalen Nachweis. Die Empfehlung muss eine konkrete messbare Nachprüfung enthalten.

## Qualität und Ablage
- Keine erfundenen Messwerte oder externen Aktionen.
- Für reproduzierbare Berichte Source-ID, Datenstand, Definitionen, Filter, Version und verwendete Methode referenzieren.
- Arbeitsergebnisse nur bei Bedarf außerhalb `.analytics/` erstellen; Zustand und Entscheidungen getrennt halten.
