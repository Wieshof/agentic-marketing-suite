# PRODUKTION – verbindlicher Erstellen/Prüfen/Korrigieren-Kreislauf

## 1. Auftrag und Zieldefinition
- Originalbriefing verdichten; Key Message, Zielgruppe, Anwendungsumfeld, gestalterische Anforderungen.
- Eindeutige Ausgabeanforderungen: Maße, Seiten, Format, Beschnitt, Sprachvariante, Kanal, Deadline, Druckverfahren oder Videocodec.
- Akzeptanzkriterien vor Erstellung notieren: 1 klare Botschaft, CD-Konformität, Lesbarkeit im Zielkontext, verwendbare Dateien.

## 2. Creative Direction
- Zwei bis drei echte Richtungen explorieren, differenzieren, eine begründet empfehlen.
- Leitidee, Layout-Hierarchie, Bildsprache, Tonalität, Typografie, Farben, Komposition, CTA, Barrierefreiheit.
- Entwurfsalternativen differenzieren; keine pseudo-unterschiedlichen Varianten.

## 3. Produktion
- Generative Quellen als Assets; **Text, Logos und rechtlich/faktisch wichtige Elemente deterministisch setzen**.
- Quelle/Parameter/Modell/Seed soweit verfügbar im Job dokumentieren. Editierbares Quellformat und gerenderte Version getrennt sichern.
- Für Druck: Seitengeometrie und Farbmanagement kontrolliert im DTP-/PDF-Workflow; für Video: Timeline, Audio, Untertitel, Exportprofile.

## 4. Zwei unabhängige Prüfungen
- **Visual Review:** Hierarchie, räumliche Beziehungen, Lesbarkeit in realer Größe, Barrierefreiheit, Markenwirkung, Artefakte, Textkorrektheit. Bei Video zusätzlich Rhythmus und Story; bei Audio Sprachverständlichkeit und Geräusche.
- **Technical QA:** Quelle und exportierte Datei messen: pixel/mm, Format, Dateiintegrität, Font-Lizenzen/Einbettung, Rasterauflösung, PDF-Boxen, Beschnitt, ICC und PDF/X, Video-/Audioformat, rechtliche Assets.
- Jede Prüfung protokolliert Profil, Ergebnis, Prüfer/Tool, Datei-Hash, offene Mängel.

## 5. Korrektur und Freigabe
- Mängel nach Kritikalität priorisieren (BLOCKER/MAJOR/MINOR); ändern, rendern, betroffene Prüfungen wiederholen.
- Kein „fertig“ bei Blockern. Bei ungelösten Punkten `proof_only`/`approval_pending` melden.
- Freigabe dokumentieren; externer Upload oder Druckauftrag benötigt zusätzliche explizite Ausführungsfreigabe.

## 6. Abschluss
- Übergabe: editierbare Quelle, benötigte Assets/Lizenzliste, finaler Export, QA-Report, Einschränkungen, Versionshistorie. State/Log/History auf Basis **tatsächlicher Aktionen** aktualisieren.
