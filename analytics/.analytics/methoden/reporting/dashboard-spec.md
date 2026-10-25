# Dashboard-Spezifikation
**Datei:** `.analytics/methoden/reporting/dashboard-spec.md`  
**Einsatz:** Eine dauerhafte Visualisierung gebaut werden soll  
**Ergebnis:** Produktneutraler Dashboard-Contract

## Beratungsauftrag
Übernimm die fachliche Arbeit selbst. Stelle keine methodischen Prüfungsfragen an den Nutzer. Wenn entscheidende Angaben fehlen, arbeite mit ausgewiesenen Hypothesen und klarer Unsicherheit, statt Fakten zu erfinden. Entscheide zuerst, ob diese Methode für den konkreten Auftrag überhaupt notwendig ist.

## Konkretes Vorgehen
1. Erstelle KPI-Wörterbuch und Nutzerentscheidungen.
2. Bestimme Filter, Segmente, Drilldown und Aktualität.
3. Definiere Datenqualitätsbanner und Zugriffsrechte.
4. Teste Lesbarkeit und Barrierefreiheit.

## Notwendige Nachweise
- Nenne Datenquelle, Erhebungs-/Extraktionszeit, Zeitfenster, Segmente, Zähler/Nenner sowie Vergleichsbedingungen, soweit für die Methode relevant.
- Kennzeichne Datenlücken, geringe Fallzahlen, Schätzwerte und Berechnungsschritte explizit.
- Liefere ein **verwendbares Ergebnis** und mindestens eine begründete Verbesserungsempfehlung oder explizit „keine Handlung begründbar“.

## Fachlicher Fallstrick und Gegenprüfung
**Achtung:** Dashboard darf stille Tracking-Ausfälle nicht als Performanceabsturz zeigen.
Prüfe mindestens eine plausible Gegenhypothese. Unterscheide statistische Beobachtung, Erklärung und kausalen Nachweis. Die Empfehlung muss eine konkrete messbare Nachprüfung enthalten.

## Qualität und Ablage
- Keine erfundenen Messwerte oder externen Aktionen.
- Für reproduzierbare Berichte Source-ID, Datenstand, Definitionen, Filter, Version und verwendete Methode referenzieren.
- Arbeitsergebnisse nur bei Bedarf außerhalb `.analytics/` erstellen; Zustand und Entscheidungen getrennt halten.
