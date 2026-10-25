# MEDIAPLAN — offenes Austauschformat und Fachlogik

Ein Mediaplan soll **ohne Werbeplattformkonto und ohne proprietäre Datei** nachvollziehbar bleiben. Lege `medienplan.csv` nur an, wenn ein konkreter Auftrag vorliegt.

## Spalten eines exportierbaren Plans
`campaign_id;market;language;channel;inventory;objective;audience;creative_ref;landing_ref;start_date;end_date;currency;budget_limit;estimate_type;estimated_cpm;estimated_cpc;estimated_impressions;expected_primary_kpi;assumptions;approval_status`

- Dateiformat: UTF-8 CSV mit `;` als Trennzeichen, Beträge als dezimale Zahlen in der angegebenen Währung (kein Tausenderpunkt). Datum nach ISO 8601.
- `estimate_type` ist `unknown`, `assumption`, `vendor_quote` oder `account_data`; keine Zahlen in unbestätigte Felder eintragen.
- Kosten für Kreation, Media-Handling, Tracking, Plattformzuschläge und Steuern **gesondert** aufführen. Ein Gesamtbudget muss mit sämtlichen Kostenrisiken abgestimmt werden.
- Ein CPA-/CPC-/CPM-Ziel ist weder garantiert noch aus einem allgemeinen Branchenmittel abzuleiten. Bei nur angenommener Datenlage transparent Szenarien und Sensitivität zeigen.
- `approval_status` ist `draft`, `reviewed`, `approved`, `booked`, `active` oder `completed`; `booked`/`active` nur mit tatsächlichem Nachweis.

## Kennzahlen und Einheiten
- `CPM = Spend / Impressions × 1.000` nur bei Impressions > 0.
- `CPC = Spend / Clicks` nur bei Clicks > 0.
- `CTR = Clicks / Impressions` nur bei Impressions > 0.
- `CPA = Spend / Conversions` nur bei Conversions > 0.
- `ROAS = zurechenbarer Umsatz / Spend` (≠ Marge/Profitabilität).
- `Frequency ≈ Impressions / Unique Reach`, nur wenn Reach-/Impression-Messungen vergleichbar sind.

Bei Markt-/Brandenaufbau ergänze Befragungen/Brand Lift, qualifizierte Kontakte und inkrementelle Nachfrage; CPM und Klicks allein beweisen keine Bekanntheit.

## Entscheidungshilfe
Empfehle in der Reihenfolge: 1) keine Werbung, falls ungeeignet; 2) einen sinnvoll eingegrenzten Pilotkanal; 3) mehrere Kanäle nur bei ausreichend Budget und Datenqualität.
