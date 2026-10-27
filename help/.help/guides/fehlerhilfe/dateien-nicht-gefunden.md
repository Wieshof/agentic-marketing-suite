# Fehler: Dateien oder Fachbereich nicht gefunden

1. Stimmt das Arbeitsverzeichnis? `help/` muss neben den anderen Modulen liegen, falls integriert.
2. Kann das Agentensystem Dateien lesen und existiert der angegebene Pfad tatsächlich?
3. Werden versteckte `.help/`, `.suite/`, `.marketing/`-Ordner mitkopiert?
4. Ist das Modul vielleicht ein separat verfügbares, noch nicht integriertes Paket (z. B. Branding)?
5. Bei Terminalzugriff: `python3 help/.help/tools/scan_workspace.py --root .` listet **nur vorhandene Dateistrukturen**.

Wenn kein Dateizugriff besteht, die betreffende Datei bereitstellen; keine behaupteten Dateiinhalte aus einem Namen ableiten.
