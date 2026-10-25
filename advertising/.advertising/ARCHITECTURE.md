# ARCHITECTURE — werbliches Denken und Ausführungsarchitektur
## Grenzen
`advertising/AGENT.md` = Einstieg; `.advertising/` = statische Fachmethoden, Kanal-/Formatwissen, Quellen, Schnittstellenverträge sowie Laufzeitmetadaten STATE/LOG/HISTORY. Ergebnisse außerhalb der versteckten Systemstruktur.

## Entscheidungslaufzeit
`Intent → Kontext & Evidenz → Diagnose → Methodenwahl → Empfehlung/Strategie → kreative Leitidee → Mediaplan → Qualitätsprüfung → freizugebende Artefakte → ggf. verbindlicher Media-Auftrag → Ausführungsadapter → Plattformbeleg → Bericht → Optimierung`.

## Teilprozesse
- **Beratung:** unabhängig und ohne Werbekonto möglich.
- **Kreativproduktion:** Text, Design-Briefings, Storyboards, Varianten; Produktrender nur mit verfügbaren Tools.
- **Mediaplanung:** Zielmarkt, Kanalrollen, Budget-Szenarien, Kontaktqualität, Frequenz, Testdesign, Laufzeit; niemals fehlende Benchmarks als Fakten behandeln.
- **Aktivierung:** hermetisch über Adapter, mit Genehmigung, Rechteprüfung, Idempotenz, Dry-run/paused-first, Bestätigung.
- **Optimierung:** nur mit ausreichendem Messfenster, Konfidenz/Unsicherheit, konkretem Änderungsauftrag; Stop-Loss- und Rückfallregel.

## Kooperation ohne Zwang
- `../marketing/`: Unternehmensziele/Strategie/Positionierung
- `../pr/`: Reputations-/Medienkontext
- `../social-media/`: organische Kanäle, Content-Material, Freigaben (nicht automatisch Ads-Budget)
- `../website/`: Zielseiten, technische Conversion, Design
- `../creative/`: Asset-Erzeugung
- `../analytics/`: Messung/Attribution
Fehlen diese Verzeichnisse, arbeitet Advertising vollständig eigenständig. Verweise nur auf tatsächlich vorhandene, berechtigt zugängliche Dateien. Keine Übertragung persönlicher Daten ohne Erlaubnis.

## Persistenz
`.advertising/STATE.md` = aktuellen Stand und Artefaktpfade; `.advertising/LOG.md` = überprüfbare Aktionen + Fehler mit IDs; `.advertising/HISTORY.md` = bestätigte strategische Entscheidungen, Abweichungen und Versionen. Keine erfundenen Einträge. Bei fehlender Dateischreibfunktion Arbeit im Dialog ausgeben und den fehlenden Speicherzustand benennen.

## Wiederaufnahme
Zuerst STATE lesen; Referenzen auf konkrete Artefakte prüfen; nur benötigtes Wissen laden; bei offenen Genehmigungen in review, niemals ungefragt aktivieren.
