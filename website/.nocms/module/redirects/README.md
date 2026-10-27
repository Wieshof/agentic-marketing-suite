# Weiterleitungen · Capability v0.1

## Zweck / Voraussetzungen

Exakte lokale URL-Umzüge als reviewbare Apache-`RedirectMatch`-Regeln erzeugen. Python 3.9+ beim Build; Apache `mod_alias` und passende `AllowOverride`-/Hostingrechte bei Auslieferung. Andere Hostingformate sind nicht als implementierte Adapter ausgegeben.

## Konfiguration / Ein- und Ausgaben

[mappings.example.json](mappings.example.json) enthält `from`, `to`, `status` (301 oder 302). Beide Pfade sind einfache lokale ASCII-Pfade ohne Prozentkodierung, fremden Host, Query oder Header-/Konfigurationszeichen. Komplexe/Unicode-Mappings am konkreten Hoster gesondert prüfen statt ungeprüft generieren.

```sh
python3 website/.nocms/tools/webmodules.py --site /projekt/site redirects --input /projekt/redirects.json
```

Erzeugt `.htaccess` nur, wenn keine vorhanden ist. Bestehende Hostingregeln manuell vergleichen/zusammenführen; keine automatische Überschreibung, kein automatisches Deployment und keine Cache-Invalidierung. Die SFTP-Prüfung erlaubt diese gezielt reviewbare Hostingdatei als Ausnahme zu privaten Punktdateien.

## Prüfung / Status

Exakte Regex-Verankerung, keine fremden Ziele, doppelten Quellen, Selbstumleitungen oder Schleifen. `local_files_created` bedeutet keine aktive Serverkonfiguration. Vor Veröffentlichung echte Apache-/Host-Konfiguration prüfen, danach Statuscodes und Zielseiten testen. 301 kann von Clients dauerhaft zwischengespeichert werden; Mapping bewusst freigeben. Es wird keine echte Hosting-Abnahme durch die lokalen Generator-Tests behauptet.
