# Änderungen

## Unveröffentlicht – vorgesehen für v0.2.3

- Acht optionale technische Fähigkeiten: SFTP-Publishing, gemeinsamer IMAP-/SMTP-Mail-Adapter und sechs standalone Webmodule (Kontaktformular, Analytics Lite, Suche, Sitemap, Weiterleitungen, Newsletter mit Double-Opt-in).
- Capability-Register, maschinenlesbare Verträge, explizite Freigabebindung, private Ausführungsprotokolle und kontrollierte Recovery ohne blinde Wiederholung.
- Selektive Installation, private Host-Konfiguration, begrenzte Serviceaufträge, tägliche Aufbewahrungswartung und echte PHP-HTTP-/Browsermodultests. Keine automatische Konto-/Hosteraktivierung.

## v0.2.2 – 27. Oktober 2026

Additive Freigabe-/Audit-Fähigkeit mit einer rein lesenden Dashboard-Übersicht. Bestehende Kernverträge und Fachmodule bleiben kompatibel.

- Dashboard-Übersicht „Freigaben“: ausdrücklich konfigurierte, nur lesend ausgewertete Audit-Protokolle mit aktuellem Status, Version, Person, Zeit und Budget; automatische Aktualisierung und klare Leer-/Fehlerzustände.

- Optionale Human Approval & Audit Trail Capability: konkrete Anforderungen, menschliche Entscheidungen einschließlich Änderungswunsch und Widerruf, fortlaufende private JSONL-Ereignisse, read-only Statusprojektion und Regressionstests. Bestehende Aktionsfreigabeverträge bleiben kompatibel; keine Ausführungsprüfung im Dashboard.

## v0.2.1 – 27. Oktober 2026

Wartungs- und Sicherheitsupdate auf Basis von v0.2. Die neun Fachmodule bleiben eigenständig nutzbar; JSON-Verträge und Methoden-IDs bleiben kompatibel.

- Lokales Dashboard: Anfragen und Dateizugriffe serverseitig begrenzt; interne Dateifreigabe wird durchgesetzt, bekannte Zugangsdatenpfade bleiben gesperrt. Bestehende Server nach dem Update neu starten.
- Einheitliche Regeln für Begrüßung, konkrete Aufträge und Wiederaufnahme vorhandener Arbeitsstände in allen Fachmodulen.
- Selektive Analytics-Rückkopplung in PR, Social Media, Creative und noCRM; optionale E-Commerce-Quellen für Advertising und Analytics.
- Budgetvorschlag und Budgetprüfung klar von menschlicher Freigabe getrennt.
- Marketing-Quellenregister mit Zuordnung aller 45 Methoden; fehlende Eingangs-/Archivordner und TOPACA-Arbeitsauftrag ergänzt.
- Zusätzliche Regressionstests für den Social-Media-Validator und das Dashboard.

[Hinweise zur Aktualisierung](MIGRATION.md) · [Dashboard-Konfiguration](.suite/dashboard/README.md)

## v0.2 – 26. Oktober 2026

Gemeinsame Governance-, Qualitäts- und Vertragsregeln integriert, Modulübergaben präzisiert und E-Commerce als neuntes Fachmodul ergänzt. Details stehen in der [Entscheidungshistorie](.suite/HISTORY.md).
