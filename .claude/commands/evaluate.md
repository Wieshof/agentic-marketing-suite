---
description: Kennzahlen aus einer CSV mit Datensatzmanifest bewerten
argument-hint: <Pfad zur CSV> [Metrik] [Zeitraum A] [Zeitraum B]
---
Bewerte die Daten: $ARGUMENTS

1. `analytics/AGENT.md` befolgen. Zur CSV gehört ein Datensatzmanifest (`*.manifest.json`); fehlt es, zuerst nach Quelle, Zeitraum, Zeitzone und Filtern fragen.
2. Rechnen nur mit `analytics/.analytics/tools/evaluate_csv.py` (gewichtete Raten über `--denominator`, nicht Einzelquoten mitteln).
3. Bericht nach der passenden Methode unter `analytics/.analytics/methoden/reporting/`; Unsicherheit, fehlende Kausalität und Datenlücken offen benennen.
4. Keine Budgetänderung empfehlen, ohne sie als Vorschlag mit menschlicher Freigabe zu kennzeichnen.
