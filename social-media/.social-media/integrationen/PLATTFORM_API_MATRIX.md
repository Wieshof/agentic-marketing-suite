# Veröffentlichungs-Matrix – keine Echtzeit-Garantie

**Recherche-Basis:** offizielle Quellen aus `.social-media/QUELLEN.md`, Stand 23.10.2026. Die folgenden Möglichkeiten sind **Grundpfade**, keine Prüfung eines vorhandenen Kontos. In einem konkreten Projekt gilt jede Capability standardmäßig als `unverified`, bis sie per verbundenem Konto, Scope und Test nachgewiesen ist.

| Kanal | Dokumentierter technischer Ausgangspfad | Besondere Grenze / Pflichtprüfung | Fallback |
|---|---|---|---|
| LinkedIn | Posts API für organischen Text, Bild, Video, Dokument und MultiImage | Unternehmensrollen und Scopes, Versionsheader, App-Freigaben. **Organische Carousels nicht gleich API-Dokumentpost** | LinkedIn-Webapp |
| Instagram | Instagram Platform API für Professional-Accounts: Feed, Reels, Carousel | Instagram API mit Facebook Login: kein Consumer Account, Stories nur Business; Media Container/Processing, öffentlich abrufbares Media ggf. nötig | Instagram-App |
| Facebook | Meta Graph / Pages-Kontext | API-Variante, Page-Rollen, Content-Typ, Feature-Freigaben und Berechtigungen aktuell verifizieren | Facebook Pages UI |
| Threads | Threads API: Text, Bild, Video, Carousel | App-/User-OAuth, Container/Publish, aktuelle Metadaten/Reply-Einstellungen | Threads-App |
| TikTok | Content Posting API für Video und Fotos | App-Audit, `video.publish`-Berechtigung, Creator-Consent; ungeprüfte Clients unterliegen privaten Sichtbarkeitslimits | TikTok-App |
| YouTube | YouTube Data API `videos.insert` für Video-Uploads | Upload-Scopes und Quota, API-Checks, tatsächliche Short-Einstufung erst Plattform-seitig; Polling auf Bearbeitung | YouTube Studio |
| Pinterest | Pinterest API v5 zur Pin-Erstellung und Medienverwaltung | OAuth scopes, Board-Zugriff, Sandbox/Standard, Videopins ggf. separates Handling | Pinterest-Webapp |
| Bluesky | AT Protocol Records, Media Blobs | Auth, Medienlimits/Typen, Record-Referenzen | Bluesky-App |
| Mastodon | `POST /api/v1/statuses`, Medien-Upload, planbare Status je Version | Instanzregeln, API-Version, Media Processing/Permissions | Mastodon-Webapp |
| X | Plattform-API grundsätzlich möglich | Aktuelle Preise, API-/Plan-Limits, Publikations-/Automationsregeln **nicht** fest annehmen | X-Webapp |
| Reddit | API / Community-Kontext | Zugangsfreigabe, aktuelle API-Policies, individuelle Subreddit-Regeln, Moderation | Reddit UI |
| Telegram | Offizielle Bot API für autorisierte Chats/Kanäle | Bot-Adminrechte und Einwilligung, Rate-Limits | Telegram UI |
| WhatsApp Channels | Nicht pauschal zugesagt | Keine Gleichsetzung mit WhatsApp Business Platform. Ohne nachgewiesene erlaubte Channel-API **nur manueller Weg** | WhatsApp-App |
| Discord | Bot API / Webhooks für erlaubte Serverkanäle | Bot-/Webhook-Rechte, Serverregeln, kein DM-Spam | Discord UI |

## Aktivierungsstatus je realem Konto
Mindestens speichern: `channel`, `account_identifier`, `account_type`, `adapter`, `connected`, `scopes_verified`, `can_publish_text`, `can_publish_image`, `can_publish_video`, `can_publish_story`, `can_schedule`, `can_read_insights`, `tested_at`, `source_checked_at`. Standard **false/unknown**, keine Annahme aus Produktmarketing.

## Technische Grundausstattung
- Optional self-hosted **Postiz** als fertiger Scheduler mit API/Workflow-Integrationen, aber mit eigenem Betriebsaufwand und **eigenen Plattform-App-Freigaben** bei Self-hosting. Lizenz: AGPL-3.0, Pflichten bei Anpassungen/Betrieb prüfen.
- Alternativ direkte offizielle Plattformadapter oder native manuelle Veröffentlichungswege.
- **FFmpeg / ffprobe** prüfen Export/Codecs; **ImageMagick/Pillow** Bildgrößen/Metadaten; **Python/CSV/JSON** für Jobs, Kalender und Reports; ein sicherer Vault für OAuth; ein echter Scheduler für terminierte Veröffentlichung.
- Keine Softwareinstallation oder authentifizierter Account ist in diesem Paket enthalten.
