# Quellenadapter — minimaler Vertrag v0.1

## Interface
- `discover()`: verfügbare Quellen und Berechtigungen melden; keine stillen Datenimporte.
- `describe(source)`: Grain, Metriken, Zeitzone, Historie, Limitierungen und Datenschutzklasse melden.
- `extract(query, read_only=true)`: Daten per autorisiertem Zugriff in CSV/JSON liefern, Zeitfenster/Filter/Account eindeutig vermerken; keine Ressourcen ändern.
- `validate(export)`: Schema, Zeiträume, Zeilenzahl, leere Werte, Pagination/Limitierung, Sampling/Thresholding, Version, Einheiten prüfen.
- `provenance()`: extrahiert_am, Account-/Quellen-ID, Abfrageparameter, Version, Datei-Hash, Fehlermeldungen.
- `revoke()`: Berechtigung entziehen ohne Daten zu löschen (Löschung ist eigener geregelter Vorgang).

## Sicherheits- und Qualitätsinvarianten
Read-only Default, OAuth/Tokens aus Secret Store, minimale Scopes, Retry/Rate-limit, Pagination, Quotenverwaltung, Datenzugriff nur für definierte Aufgabe. Kein Server-seitiger code execution via CSV-Felder. Abweichende CSV-Zeilen, Plattform-Updates, fehlende Tage und Messlücken nicht verschweigen.

## Nicht enthalten
Keine fertigen OAuth-Flows, keine Live-Konten, keine garantierte historische Datenverfügbarkeit, keine Produktivdatenbank und keine autonome Änderungsberechtigung in anderen Modulen.
