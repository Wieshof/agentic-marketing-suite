# A/B-Test korrekt planen
**Datei:** `.analytics/methoden/experimente/ab-test-design.md`  
**Einsatz:** Zwei Varianten verglichen werden sollen  
**Ergebnis:** Vorregistrierter Testplan

## Beratungsauftrag
Übernimm die fachliche Arbeit selbst. Stelle keine methodischen Prüfungsfragen an den Nutzer. Wenn entscheidende Angaben fehlen, arbeite mit ausgewiesenen Hypothesen und klarer Unsicherheit, statt Fakten zu erfinden. Entscheide zuerst, ob diese Methode für den konkreten Auftrag überhaupt notwendig ist.

## Konkretes Vorgehen
1. Definiere eine primäre Metrik und Minimal Detectable Effect.
2. Randomisierungseinheit und Laufzeit prüfen.
3. Vermeide frühzeitiges optionales Stoppen.
4. Lege Ausschlüsse/Guardrails vor Testbeginn fest.

## Notwendige Nachweise
- Nenne Datenquelle, Erhebungs-/Extraktionszeit, Zeitfenster, Segmente, Zähler/Nenner sowie Vergleichsbedingungen, soweit für die Methode relevant.
- Kennzeichne Datenlücken, geringe Fallzahlen, Schätzwerte und Berechnungsschritte explizit.
- Liefere ein **verwendbares Ergebnis** und mindestens eine begründete Verbesserungsempfehlung oder explizit „keine Handlung begründbar“.

## Fachlicher Fallstrick und Gegenprüfung
**Achtung:** Ungeplantes tägliches Testen erhöht Fehlalarmrisiko.
Prüfe mindestens eine plausible Gegenhypothese. Unterscheide statistische Beobachtung, Erklärung und kausalen Nachweis. Die Empfehlung muss eine konkrete messbare Nachprüfung enthalten.

## Qualität und Ablage
- Keine erfundenen Messwerte oder externen Aktionen.
- Für reproduzierbare Berichte Source-ID, Datenstand, Definitionen, Filter, Version und verwendete Methode referenzieren.
- Arbeitsergebnisse nur bei Bedarf außerhalb `.analytics/` erstellen; Zustand und Entscheidungen getrennt halten.
