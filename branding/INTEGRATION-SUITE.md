# Integration in die Agentic Marketing Suite

Dieses Paket ist **additiv**. `branding/` als eigenständigen Ordner auf oberster Suite-Ebene hinzufügen. Die vorhandenen `marketing/`, `creative/`, `business-dna/` und `.suite/` bleiben unverändert.

1. `branding/AGENT.md` ist direkter Einstieg. Die Root-`AGENT.md` und `.suite/MODULES.md` können bei Bedarf einen Verweis `branding/AGENT.md` aufnehmen.
2. `../business-dna/` ist optional und liefert geprüfte bzw. deklarierte Organisationsinformationen. Branding ist nur kanonisch für **Markenentscheidungen**, nicht für Unternehmensfakten.
3. `../creative/`, `../marketing/`, `../pr/`, `../website/`, `../social-media/`, `../advertising/`, `../noCRM/` und `../analytics/` können zweckgebunden Brand Context Packs lesen.
4. `.suite/LEGAL.md`, `.suite/QUALITY.md` und `.suite/GOVERNANCE.md` bleiben die übergreifenden Standards, sofern die Suite installiert ist. Das Branding-Modul erzeugt keine zusätzliche Runtime oder zentrale Sicherheitsarchitektur.
5. Keine echten Marken-/Produktdaten im Methodenordner einchecken; `input/`, `archiv/` und dynamische Kundenergebnisse nach Projektpolitik behandeln.
6. Nach Integration Tests durchführen: natürliche Startfrage, Positionierung aus grobem Briefing, Fakt-/Strategie-Trennung, Review eines fremden Artefakts und Context Pack nach `visibility`.

**Abgrenzung:** Das Paket installiert weder Designsoftware noch externen Markenrechtsdienst, noch ist es ein Publishing-Adapter. Das vorhandene Harness kann Dateien lesen und die beigelegten Offline-Prüfwerkzeuge aufrufen.
