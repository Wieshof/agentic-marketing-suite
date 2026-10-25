# PUBLISHING – Veröffentlichungsmodell und Toolwahl

**Wichtig:** Die vorhandenen Dateien veröffentlichen NICHT selbst. Benötigt werden zugängliche offizielle Plattform-APIs oder ein genehmigter Scheduler, aktive verknüpfte Konten, OAuth/Scopes, bei einigen Plattformen App-Prüfung sowie eine dauerhaft laufende Queue/Scheduler-Infrastruktur. Vor jedem Posting Echtzeit-Preflight, da Plattformregeln wechseln.

## Wahl des Weges (in dieser Reihenfolge prüfen)
1. **Nativ:** Offizielle Web-/Mobil-App für manuelles Publishing; gute Fallback-Lösung und oft breitester Funktionsumfang.
2. **Direkte API:** Wenn Konto/Medientyp/Scopes/Review passen. Auslieferung mit Auth, Resumable Upload bei Video, Statuspolling, Rate-Limits, idempotenter Fehlerbehandlung.
3. **Austauschbarer Scheduler-Adapter:** z. B. self-hosted Postiz oder zugelassener anderer Dienst; keine Verwechslung zwischen Produktliste und tatsächlich freigeschaltetem Account-/Feature-Support.
4. **Assistierte Übergabe:** finaler Export aus Workspace mit Copy, Medien, Captions, Alt-Text und manueller Checkliste, falls API nicht unterstützt/zugelassen.

## Verpflichtender Preflight
`account_owner`, Berechtigung, konkrete `channel`, erlaubter Content-Typ, aktualisierte API-Feature-Matrix, Einwilligungen/Rechte, Medienlänge/Codec/Aspect/Dateigröße, Alttext/Caption, verbindliche Uhrzeit inkl. Zeitzone, revidierte Freigabe, Ausführungscredential aus Vault, Policy-Compliance, Kosten und Dublettencheck prüfen. Wenn etwas fehlt: `blocked`, nicht erraten.

## Ausführungsvertrag
Siehe `integrationen/PUBLISH_JOB_SCHEMA.json` und `integrationen/ADAPTER_CONTRACT.md`. Status/Planung/Zielplattform unabhängig dokumentieren. Adapter müssen `validate`, `upload`, `schedule_or_publish`, `status`, `cancel` soweit API es unterstützt, `read_metrics` soweit autorisiert implementieren oder explizit als nicht verfügbar deklarieren.

## Zustandsnachweis
`queued/scheduled` nur mit echter Queue-/Plattformbestätigung. `published` nur mit bestätigter Remote-ID bzw. überprüfbarem externen Nachweis. API-Timeout: `unknown` und Remote-Abgleich vor Retry. Keine automatische Wiederholung anhand eines LLM-Vorschlags. Löschung/Änderung live nur mit eigener Berechtigung.

## Formate
- Reels, Shorts und TikTok-Videos unterscheiden sich nicht nur in Größe, sondern auch Produkt-/Uploadlogik, Audio-/Musikrechten, Cover- und UI-Metadaten.
- Story, Livestream, Duett, kollaborativer Post, Sticker, Trend-Audio oder Poll können manuelle native App-Funktionen sein. Nie universelle API-Verfügbarkeit annehmen.
- Feeds/Carousels, Stories und Ads sind separate Capability-Klassen; Connected-Account-Typ kann den Unterschied machen.

## Tools (Kategorien)
- **Grundlage:** FFmpeg/ffprobe für technische Video-/Audio-Prüfung, ImageMagick/Pillow für Bildprüfung, JSON/CSV für Export, git oder versioniertes Archiv für Revisionen.
- **Content-Erzeugung:** beliebiger Text-/Vision-LLM-Service, Bild-/Video-/TTS-Werkzeuge, Editor und Untertitel-Generator – niemals Voraussetzung für reinen Beratungseinsatz.
- **Orchestrierung:** lokale Queue/Cron/Workflow-Engine (z. B. n8n) oder Scheduler wie Postiz; nur verwenden, falls installiert/konfiguriert.
- **Publishing:** offizielle APIs, erlaubte Partner oder native Plattform-App. Kein Browserbot, der Captchas/Plattformregeln umgeht.
- **Analytik:** offizielle Insights/Exports, datensparsame Tracking-URLs mit klaren Einwilligungsvorgaben; plattformübergreifende Metriken fachlich nicht blind addieren.

Siehe `integrationen/PLATTFORM_API_MATRIX.md` für die dokumentierte Ausgangslage und offizielle Quelllinks. Stand: 23. Oktober 2026; Werte vor jeder Live-Nutzung neu prüfen.
