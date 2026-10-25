# Quellenprofil: SQL / DuckDB / PostgreSQL
**Datenweg:** Optional read-only SQL adaptor with scoped role.

## Importprinzip
1. Lesezugriff/Scope, Zweck, Berichtszeitraum und relevante Konten ermitteln.
2. Offene Exportrepräsentation CSV/JSON bevorzugen und Datenstand, Zeitzone, Schema, Filter sowie Query festhalten.
3. Grain, Metrikdefinitionen, Quoten/Pagination und eindeutige Schlüssel validieren; keine implizite Quellenfusion.
4. Nur für eine konkrete fachliche Entscheidungsfrage analysieren. Dokumentiere Einschränkungen, bevor du Ergebnisse deutest.

## Kritische Prüfung
SQL injection, Cartesian joins, personally identifying rows, query performance.

## Betrieb
Dies ist ein fachliches Profil, **kein funktionierender API-Connector**. Vor echter Anbindung aktuelle Hersteller-Dokumentation, Berechtigungen, Datenschutz und Rate-Limits prüfen. Standardmäßig **read-only**.
