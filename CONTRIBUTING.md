# Beiträge zur Agentic Marketing Suite

Fehlerberichte, fachliche Korrekturen und Erweiterungen sind willkommen. Bitte zuerst die [README](README.md) und die Regeln des betroffenen Moduls lesen. Für Sicherheitslücken gilt [SECURITY.md](SECURITY.md).

## Änderungen vorschlagen

1. Ein Issue mit dem konkreten Problem und einem reproduzierbaren Beispiel eröffnen oder ein bestehendes Issue verwenden. Keine echten Kontakt-, Kunden- oder Zugangsdaten anhängen.
2. Das Repository forken, einen eigenen Branch anlegen und Änderungen auf ein nachvollziehbares Thema begrenzen.
3. Neue Methoden im jeweiligen `METHODEN.md` registrieren. Zuständigkeiten, Quellen, Grenzen und positive wie negative Anwendungsfälle beschreiben.
4. Betroffene Dokumentation, Beispiele und Tests aktualisieren. Öffentliche Vertragsänderungen und Upgrade-Schritte in [MIGRATION.md](MIGRATION.md) erläutern.
5. Lokal prüfen und einen Pull Request mit Problem, Änderung und Prüfergebnis erstellen.

## Lokale Prüfung

Python 3.9 oder neuer genügt; die enthaltenen Hilfswerkzeuge und Tests benötigen keine zusätzlichen Python-Pakete.

```sh
python3 .suite/tools/check_repository.py
```

Die Prüfung kontrolliert erforderliche Dateien, lokale Markdown-Linkziele, JSON-Syntax, automatisierte Tests und ausgewählte Demo-Preflights. Sie stellt keine Verbindung zu Marketingplattformen her und bescheinigt keine fachliche oder rechtliche Produktionsreife.

## Daten und Rechte

Nur eigene oder zur Veröffentlichung berechtigte Inhalte beitragen. Beispiele müssen fiktiv oder ausdrücklich für die Veröffentlichung freigegeben sein. Externe Quellen verlinken und Herkunft sowie abweichende Nutzungsbedingungen kenntlich machen. Beiträge werden unter der bestehenden [MIT-Lizenz](LICENSE.md) eingereicht; fremde Rechte bleiben zu beachten.

Methodenbibliothek und produktive Arbeitsdaten getrennt halten. `STATE.md`, `LOG.md` und `HISTORY.md` können im Betrieb vertrauliche Informationen enthalten und müssen vor einem öffentlichen Commit kontrolliert werden. Die `.gitignore` deckt typische lokale Dateien ab, ersetzt aber keine Sichtprüfung.
