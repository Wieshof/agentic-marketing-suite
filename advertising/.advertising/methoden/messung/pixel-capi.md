# Pixel, CAPI und Conversion Events

**Methoden-ID:** `messung/pixel-capi` · **Typ:** fachliche Arbeitsanleitung · **Version:** 0.1

## Wann anwenden
Messung von Konversionen geplant. Nicht allein deshalb anwenden, weil die Datei vorhanden ist. Falls das eigentliche Ziel durch eine einfachere Maßnahme erreicht wird, diese empfehlen.

## Eingaben und Umgang mit Lücken
Ziel/Auftrag, Produkt-/Leistungsfakten, Zielgruppe, Markt, Ressourcen und nachweisbare Quellen soweit für diese Methode nötig heranziehen. Bestehende, berechtigt zugängliche Projektartefakte vor neuen Fragen nutzen. Fehlende Angaben markieren; reversible Hypothesen formulieren. Nur nachfragen, wenn das Ergebnis sonst riskant oder eine verbindliche Entscheidung unmöglich wäre.

## Fachliches Verfahren
1. Rechtsgrundlage/Consent vor Implementierung prüfen.
2. Eventnamen, Datensparsamkeit und Deduplication definieren.
3. Browser/Server-Abgleich und Testevents durchführen.
4. Fehlerbehandlung und Löschprozesse dokumentieren.

## Ergebnis für den Menschen
**Tracking-Design und Validierungsprotokoll**. Beginne mit einer klaren Empfehlung bzw. einem verwendbaren Entwurf. Kennzeichne Tatsachen, Hypothesen und ausstehende Freigaben. Beschreibe die nächstbeste Aktion und eine Alternative, falls der Ansatz nicht sinnvoll ist.

## Qualitätssicherung / Red Flags
- Keine Client-Daten ungefragt an Ads-Provider übertragen.
- Keine erfundenen Quellen, Gebote, Benchmarks, Plattformrechte oder Wirksamkeitsbelege.
- Prüfe Wirkung auf Ziele, Budget, Machbarkeit, Ethik und angrenzende Kanäle.
- Externe und kostenpflichtige Maßnahmen nur gemäß `.advertising/MEDIA_BUYING.md`.

## Übergaben und Ablage
Falls relevant, Ergebnis außerhalb `.advertising/` als nachvollziehbare Markdown-/CSV-/JSON-Artefakte speichern. Für weiterführende Aufgaben passende Methoden selektiv aus `.advertising/METHODEN.md` wählen; nicht ungefragt die gesamte Bibliothek abarbeiten. Bei tatsächlichen Änderungen STATE/LOG/HISTORY sachgerecht aktualisieren.
