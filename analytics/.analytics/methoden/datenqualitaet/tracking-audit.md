# Tracking- und Instrumentierungsprüfung
**Datei:** `.analytics/methoden/datenqualitaet/tracking-audit.md`  
**Einsatz:** Ein starker Trend durch Trackingänderung entstanden sein könnte  
**Ergebnis:** Tracking-Audit mit Bruchstellen und Nachmessung

## Beratungsauftrag
Übernimm die fachliche Arbeit selbst. Stelle keine methodischen Prüfungsfragen an den Nutzer. Wenn entscheidende Angaben fehlen, arbeite mit ausgewiesenen Hypothesen und klarer Unsicherheit, statt Fakten zu erfinden. Entscheide zuerst, ob diese Methode für den konkreten Auftrag überhaupt notwendig ist.

## Konkretes Vorgehen
1. Vergleiche Tag-/Event-Versionen und Zeitpunkte.
2. Prüfe Consent-Banner, Adblocker und Hoständerungen.
3. Validiere Events gegen serverseitige Referenzzahlen.
4. Markiere Vergleichsbrüche explizit.

## Notwendige Nachweise
- Nenne Datenquelle, Erhebungs-/Extraktionszeit, Zeitfenster, Segmente, Zähler/Nenner sowie Vergleichsbedingungen, soweit für die Methode relevant.
- Kennzeichne Datenlücken, geringe Fallzahlen, Schätzwerte und Berechnungsschritte explizit.
- Liefere ein **verwendbares Ergebnis** und mindestens eine begründete Verbesserungsempfehlung oder explizit „keine Handlung begründbar“.

## Fachlicher Fallstrick und Gegenprüfung
**Achtung:** Mehr erfasste Conversions kann nur bessere Instrumentierung bedeuten.
Prüfe mindestens eine plausible Gegenhypothese. Unterscheide statistische Beobachtung, Erklärung und kausalen Nachweis. Die Empfehlung muss eine konkrete messbare Nachprüfung enthalten.

## Qualität und Ablage
- Keine erfundenen Messwerte oder externen Aktionen.
- Für reproduzierbare Berichte Source-ID, Datenstand, Definitionen, Filter, Version und verwendete Methode referenzieren.
- Arbeitsergebnisse nur bei Bedarf außerhalb `.analytics/` erstellen; Zustand und Entscheidungen getrennt halten.
