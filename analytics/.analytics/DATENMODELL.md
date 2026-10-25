# DATENMODELL — Datenquelle, Metrik und Analyseobjekt

## Source Manifest
Jeder Datensatz bekommt `dataset_id`, `source_system`, `extracted_at`, `time_zone`, `grain`, `period_start`, `period_end`, `metric_definitions`, `filters`, `permissions`, `privacy_class`, `data_quality_notes`, optional `file_sha256`. Rohdateneinträge bleiben unangetastet. Datenstandsänderungen erzeugen neue Versionen.

## Metrikdefinition
`metric_id`, Anzeigename, Einheit, Zähler/Nenner, erlaubte Aggregationen, gültiges Populationsuniversum, Zähllogik, Berichtsfenster und Einschränkungen. Beispiel: CTR = Klicks/Impressionen für **dieselbe definierte Population**; nicht Durchschnitt einzelner CTR-Werte ohne Gewichtung.

## Vergleich
`analysis_id`, Zielentscheidung, Vergleichsfenster, Kontrollgruppe (falls vorhanden), Kanal/Segment, Filter, Störfaktoren, Berechnungen, Konfidenz/Evidenzgrad, Alternativerklärungen, Empfehlungen, Nachmessung.

## Privacy
Standard sind aggregierte Daten; Einzelkontakte, gerätebasierte Identitäten und vertrauliche Geschäftsmetriken nur bei geklärtem Zweck und Berechtigung. Keine automatische Identity Resolution. Event-Daten besitzen Datums-/Zeitzonen- und Consent-Kontext.

## Formate
CSV für einfache Zeitreihen/Tabellen; JSON für Manifest/Report; JSONL für Ereignisreihen; Parquet optional für große Datenbestände. Originale im Originalformat erhalten, wenn rechtlich und organisatorisch zulässig.
