# XML-Sitemap · Capability v0.1

## Zweck / Voraussetzungen

Sitemap für öffentliche statische HTML-Seiten erstellen. Python 3.9+ nur beim Build, kein Laufzeitdienst auf der Website.

## Konfiguration / Ein- und Ausgaben

```sh
python3 website/.nocms/tools/webmodules.py --site /projekt/site sitemap --origin https://example.com
```

Erzeugt/aktualisiert `sitemap.xml` im gewählten Website-Root. Origin muss HTTPS ohne Zugangsdaten, Query oder zusätzlichen Pfad sein; Beispiele beziehen sich auf Webroot-Hosting. Private/versteckte Pfade, `noindex` und Symlinks werden wie bei der lokalen Suche ausgeschlossen. Nur tatsächlich öffentliche Seiten einbeziehen; Hosting-Zugriffsschutz wird nicht automatisch interpretiert. Dynamische PHP-Routen und fremde Origins werden nicht automatisch erfunden. Keine vermeintlich aktuellen `lastmod`-Werte aus einem Git-Checkout ableiten.

## Prüfung / Status

URL-Encoding und XML-Escaping, valide lokale HTML-Pfade und Root-Bindung. `local_files_created` heißt nur lokal erzeugt; Veröffentlichung und etwaige Suchmaschinenübermittlung sind eigene autorisierte Schritte. XML-/Pfadtests vorhanden; nach Bereitstellung tatsächliche URL-Erreichbarkeit und Canonicals prüfen.
