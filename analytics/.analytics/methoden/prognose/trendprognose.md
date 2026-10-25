# Zeitreihenprognose und Unsicherheit
**Datei:** `.analytics/methoden/prognose/trendprognose.md`  
**Einsatz:** Künftige Nachfrage oder Reichweite geschätzt wird  
**Ergebnis:** Prognose samt Benchmark und Ausfallgrenzen

## Beratungsauftrag
Übernimm die fachliche Arbeit selbst. Stelle keine methodischen Prüfungsfragen an den Nutzer. Wenn entscheidende Angaben fehlen, arbeite mit ausgewiesenen Hypothesen und klarer Unsicherheit, statt Fakten zu erfinden. Entscheide zuerst, ob diese Methode für den konkreten Auftrag überhaupt notwendig ist.

## Konkretes Vorgehen
1. Prüfe Datenlänge, Saison, strukturelle Brüche und Missingness.
2. Vergleiche naive Baseline mit komplexerem Modell.
3. Backteste rollierend ohne Leakage.
4. Berichte Intervalle und Szenarien.

## Notwendige Nachweise
- Nenne Datenquelle, Erhebungs-/Extraktionszeit, Zeitfenster, Segmente, Zähler/Nenner sowie Vergleichsbedingungen, soweit für die Methode relevant.
- Kennzeichne Datenlücken, geringe Fallzahlen, Schätzwerte und Berechnungsschritte explizit.
- Liefere ein **verwendbares Ergebnis** und mindestens eine begründete Verbesserungsempfehlung oder explizit „keine Handlung begründbar“.

## Fachlicher Fallstrick und Gegenprüfung
**Achtung:** Prognose ist keine durch Marketing verursachte Wirkung.
Prüfe mindestens eine plausible Gegenhypothese. Unterscheide statistische Beobachtung, Erklärung und kausalen Nachweis. Die Empfehlung muss eine konkrete messbare Nachprüfung enthalten.

## Qualität und Ablage
- Keine erfundenen Messwerte oder externen Aktionen.
- Für reproduzierbare Berichte Source-ID, Datenstand, Definitionen, Filter, Version und verwendete Methode referenzieren.
- Arbeitsergebnisse nur bei Bedarf außerhalb `.analytics/` erstellen; Zustand und Entscheidungen getrennt halten.
