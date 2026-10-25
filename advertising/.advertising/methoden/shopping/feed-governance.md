# Katalog-Governance

**Methoden-ID:** `shopping/feed-governance` · **Typ:** fachliche Arbeitsanleitung · **Version:** 0.1

## Wann anwenden
Mehrere Shopping-Kanäle und häufige Aktualisierungen. Nicht allein deshalb anwenden, weil die Datei vorhanden ist. Falls das eigentliche Ziel durch eine einfachere Maßnahme erreicht wird, diese empfehlen.

## Eingaben und Umgang mit Lücken
Ziel/Auftrag, Produkt-/Leistungsfakten, Zielgruppe, Markt, Ressourcen und nachweisbare Quellen soweit für diese Methode nötig heranziehen. Bestehende, berechtigt zugängliche Projektartefakte vor neuen Fragen nutzen. Fehlende Angaben markieren; reversible Hypothesen formulieren. Nur nachfragen, wenn das Ergebnis sonst riskant oder eine verbindliche Entscheidung unmöglich wäre.

## Fachliches Verfahren
1. Single Source of Truth für SKU und Stammdaten festlegen.
2. Plattform-Mappings und Qualitätschecks definieren.
3. Deltas, Ausfälle, Preisabweichungen und Lagerbestände überwachen.
4. Rollback und Konfliktbehandlung festlegen.

## Ergebnis für den Menschen
**Feed-Betriebsmodell**. Beginne mit einer klaren Empfehlung bzw. einem verwendbaren Entwurf. Kennzeichne Tatsachen, Hypothesen und ausstehende Freigaben. Beschreibe die nächstbeste Aktion und eine Alternative, falls der Ansatz nicht sinnvoll ist.

## Qualitätssicherung / Red Flags
- Veraltete Produktdaten nicht live belassen.
- Keine erfundenen Quellen, Gebote, Benchmarks, Plattformrechte oder Wirksamkeitsbelege.
- Prüfe Wirkung auf Ziele, Budget, Machbarkeit, Ethik und angrenzende Kanäle.
- Externe und kostenpflichtige Maßnahmen nur gemäß `.advertising/MEDIA_BUYING.md`.

## Übergaben und Ablage
Falls relevant, Ergebnis außerhalb `.advertising/` als nachvollziehbare Markdown-/CSV-/JSON-Artefakte speichern. Für weiterführende Aufgaben passende Methoden selektiv aus `.advertising/METHODEN.md` wählen; nicht ungefragt die gesamte Bibliothek abarbeiten. Bei tatsächlichen Änderungen STATE/LOG/HISTORY sachgerecht aktualisieren.
