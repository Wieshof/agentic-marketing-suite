# Lokale Website-Suche · Capability v0.1

## Zweck / Voraussetzungen

Statische HTML-Seiten mit JavaScript und einem generierten JSON-Index durchsuchen. Kein Suchdienst, keine Datenbank und keine Übermittlung von Suchbegriffen. Python 3.9+ wird nur zum Erzeugen des Index gebraucht; die veröffentlichte Website benötigt ausschließlich einen Browser mit JavaScript.

## Konfiguration / Ein- und Ausgaben

```sh
python3 website/.nocms/tools/webmodules.py --site /projekt/site install site-search
python3 website/.nocms/tools/webmodules.py --site /projekt/site search-index
```

Danach stehen `search.html`, `js/site-search.js` und `search-index.json` zur Verfügung. Für Unterverzeichnis-Hosting Script-/Indexpfad und Links entsprechend anpassen. Nach Änderungen an HTML-Seiten den Index neu bauen; vorhandene generierte Indexdaten werden ersetzt, manuell abweichende Laufzeitvorlagen nicht.

Der Build verarbeitet öffentliche UTF-8-HTML-Dateien, überspringt versteckte/Archiv-/Input-Pfade und `noindex`, extrahiert keine Script-/Style-/Template-Inhalte und weist Symlinks ab. Bis zu 1000 Seiten und 5 MiB Index, pro Seite bis zu 1 MiB HTML. **Der veröffentlichte Index enthält öffentliche Textinhalte**; nicht für geschützte/personenbezogene Bereiche verwenden. `noindex` ist kein Zugriffsschutz. Vor dem Build prüfen, ob Server-Zugriffsschutz oder vertrauliche Inhalte im gewählten Root liegen.

## Prüfung / Status

Suchbegriffe bleiben in der Seite; es wird nur der gleichursprüngliche Index geladen. Treffer werden mit `textContent` gebaut, nicht als fremdes HTML. Tastaturfähiges Formular, lesbare Ergebnismeldung, mindestens zwei Zeichen und maximal 50 Treffer. Fehler ergeben „Suche derzeit nicht verfügbar“, keine vorgetäuschten Treffer. Build-/Escaping-/noindex-Tests sind enthalten; echte Browser-/Barrierefreiheitsprüfung im konkreten Design bleibt Teil der Website-Abnahme.
