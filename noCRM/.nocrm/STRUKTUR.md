# Strukturregeln

Die einzige zwingende Eintrittsdatei ist `AGENT.md`; systeminterne Unterlagen liegen unter `.nocrm/`. Bestehende Nutzerinhalte werden niemals beim Upgrade überschrieben.

`input/` ist nur Übergabeort. Erfolgreich integrierte Materialien nach Prüfung mit Herkunft und Datum unter `archiv/inputs/` unverändert ablegen; bei Importfehlern im Input belassen. Keine unbegrenzte Kopie sämtlicher Nachrichten aufbewahren.

Außerhalb von `.nocrm/` entstehen Ergebnisordner erst wenn nötig: etwa `kontakte/`, `kommunikation/`, `beziehungen/`, `service/`, `angebote/` oder `analysen/`. Ordnernamen im selben Unternehmen variieren nach Bedarf; Verweise nutzen relative Pfade. Kein Ordner pro Empfänger als Pflicht; Ereignisprotokoll + Kennung genügen zunächst.

Vor neuen Dateien: existierende Struktur und aktuellen Stand lesen. Dateinamen, Datenformate, Pfade und Privacy-Level in einem kleinen Manifest vermerken. Änderung versionsfähig und atomar durchführen; keine parallelen unsicheren CSV-Schreibprozesse. Keine Passwörter oder Token in Archiven.

Archivierung ist kein Freibrief zur ewigen Datenhaltung. Personenbezogene Backups werden in definierten Fristen gelöscht oder entsprechend behandelt. Widersprüche zwischen Löschpflicht und Archivierung werden anhand konkret geltender Pflichten gelöst.
