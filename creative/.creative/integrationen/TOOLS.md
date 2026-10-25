# TOOLS – austauschbare Werkzeugklassen

| Klasse | Beispiele | Rolle | Verbindliche Grenzen |
|---|---|---|---|
| Ideen-/Bildmodelle | lokale Modelle, Cloud-Generatoren | Varianten, Motive, Referenzbilder | Rechte, Fakten, Qualitätsprüfung, keine exakten Texte im Pixelbild |
| Vektor-/SVG-Engine | Python, SVG-Werkzeuge, Inkscape | deterministisches 2D-Layout und editierbare Quellen | SVG nicht als PDF/X deklarieren |
| DTP | Scribus/Scripter; optional InDesign Server | präziser Satz, ICC, Druck-PDF, Templates | API/Version prüfen; Druckerei fordert konkreten Export |
| Preflight | callas pdfToolbox; gleichwertige GWG-/PDF/X-Validatoren | farb-/font-/box-/normgerechte PDF-Prüfung | unabhängiger Report + Produktionsfreigabe |
| Multimedia | FFmpeg, TTS, Bild-/Video-Generatoren | Video-/Audio-Erzeugung und Transcoding | Toolverfügbarkeit prüfen, Nutzungsrechte, Playback-QA |
| Perzeption | Vision-/Audiomodelle, menschliches Review | inhaltlicher und visueller Audit | keine uneingeschränkte Qualitätsgarantie |

**Installationsstatus:** keine externe Engine wird durch dieses Paket installiert oder verbunden. `tools/creative_preflight.py` validiert Jobdaten nur strukturell; `tools/svg_proof.py` erzeugt einen **RGB-SVG-Proof**, keine Druck-PDF.
