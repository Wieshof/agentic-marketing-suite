# Toolkatalog und Auswahlentscheidung

## Minimale Arbeitsfähigkeit ohne Drittanbieter
- Fachberatung und Entwürfe: LLM mit Dateizugriff; Markdown, JSON, CSV, vorhandene Medien; keine Social-Anmeldung erforderlich.
- Bild/Text: lokaler Editor/Renderer und Bildprüfung. Nicht vorhandene Generationstools nur als mögliche Option nennen.
- Video: `ffmpeg`/`ffprobe` für Transcode/Inspektion, Untertitel als SRT/VTT, Vorschau am tatsächlichen Export. Für semantische Videosichtung ein Vision-Modell oder eine menschliche Freigabe, sonst keine Vollprüfung vortäuschen.
- Fallback-Publishing: Freigabepaket für manuelle Plattform-App mit Caption, Hashtags nur wenn relevant, Bildtext, Cover, Alttext und Prüfcheckliste.

## Direkte Kanalanbindung
Official APIs nach Account- und App-Review (siehe Matrix). Eigene Adapter nur entwickeln, wenn Zugang, Wartbarkeit und Plattformregeln es rechtfertigen. API-Endpunkte, Medienlimits, Quoten und Preise vor Implementierung abrufen.

## Scheduler-/Hub-Auswahl
**Postiz self-hosted:** AGPL-3.0, breites Kanalportfolio und API. Prüfen: Betrieb (DB/Redis/Storage), OAuth-App-Freigaben, Datenschutz, Updates, konkrete Formate/Insights, Rechte in Drittplattformen. Self-hosted ist nicht „0 Aufwand“ und nicht gleich automatisch zugelassenen API-Konten.

**n8n:** Workflow-Orchestrierung, kein universeller Social-Publishing-Provider. Braucht passende offizielle Nodes oder authentifizierte HTTP/API-Verbindungen, Scheduler und die gleiche Rechteprüfung.

**SaaS-Scheduler:** nur austauschbar anbinden, niemals als Datenmaster. Preise, AGB, Export, DSGVO, Datenaufbewahrung, API-Funktionen und Medienunterstützung vor Auswahl vergleichen.

## Tool-Entscheidungsmatrix
1. Benötigte Plattform+Format+Accounttyp nachweislich unterstützt?
2. Offizielle und erlaubte Veröffentlichung, inklusive App-Zulassung?
3. Kann jede veröffentlichte Variante inklusive Asset/Copy/ID exportiert werden?
4. Gibt es Freigabe, Audit, idempotente Recovery und echte Statuskontrolle?
5. Betreibbar im verfügbaren Technikstack ohne versteckte Cloud-/Audio-Lizenzkosten?

Bei einem Nein: Kanal manuell bedienen oder anderes Tool wählen. **Keinen Hersteller zum Kern der fachlichen Inhalte machen.**
