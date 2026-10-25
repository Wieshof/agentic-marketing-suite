# ARCHITECTURE – Creative Workspace

## Schichten
1. **Beratung**: Ziel, Konzept, kreative Kriterien, Empfehlung.
2. **Gestaltungswissen**: `.creative/methoden/`, Formatprofile, Designsystem-Referenzen.
3. **Job-Manifest**: versioniertes `creative-job.json` außerhalb `.creative/` für Ausgabespezifikation, Quellen, Bearbeitung und QS.
4. **Adapter**: Bild-/Video-/Audio-Generator, Vektor-, DTP-, Rendering-, Preflight-Engine; je Aufgabe austauschbar.
5. **Artefakte**: editierbare Quelle, gerendertes Prüfmedium, geprüfter Export, Berichte, Freigabevermerk.
6. **Persistenz**: `STATE.md` aktueller Stand, `LOG.md` tatsächliche Vorgänge, `HISTORY.md` Entscheidungen; Archiv kopiert Originale und ersetzte Freigabeversionen.

## Kerninvarianten
- Ein Job besitzt eindeutige ID und nachvollziehbare Version. Quellassets unverändert referenziert oder übernommen.
- Es existiert **keine** implizite Druck-/Upload-/Publikationsberechtigung.
- Statusmodell: `draft` → `concept_review` → `production` → `technical_qa` → `visual_qa` → `approval_pending` → `approved` → `released`; jeder Übergang protokolliert; fehlgeschlagene QA → `rework`.
- QA-Nachweis ist dateiversionsspezifisch; nach Renderänderung veraltete Prüfergebnisse nicht übernehmen.
- Arbeitsergebnisordner nur bei Bedarf. `.creative/` wird nicht mit Projektergebnissen vermischt.
- Andere Module sind optionale Wissensquellen und Auftraggeber; Dateien nur bei vorhandenem Zugriff und Berechtigung lesen. Keine überschreibenden Schreibzugriffe auf andere Fachmodule.
- Ein Designkonzept kann für mehrere Ausgaben instanziiert werden, aber **kanal-/formatangepasst** (Print ≠ Social ≠ Video).

## Empfohlener Datenfluss
Intent → selektive Marken-/Marketingdaten → Beratung/Creative Brief → Designkonzept → Medienproduktion → Preflight + visuelle Prüfung → Korrekturschleife → Freigabe → Paket/Archiv.

## Open-Source- und Provider-Grenzen
SVG/JSON sind reproduzierbar und editierbar; für professionelle Layouts können Scribus oder andere DTP-Engines genutzt werden. Generative Modelle, Cloudanbieter und kommerzielle Preflight-Engines sind **optionale Adapter**. Kein Font oder Asset wird ohne Lizenz weitergegeben.
