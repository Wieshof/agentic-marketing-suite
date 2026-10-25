# Adapter Contract — offene Schnittstelle für Media-Buying
## Zweck
Der Fachspezialist plant kanalgenerisch; ein **separat installierter** Adapter kann Werbekonten lesen, schreibend im pausierten Zustand vorbereiten, mit zusätzlicher Freigabe aktivieren, kontrolliert optimieren, deaktivieren und tatsächliche Kennzahlen berichten. Dieses Paket enthält **keine Zugangsdaten, authentifizierten Clients oder reale Veröffentlichungsfunktionen**.

## Minimale Adapteroperationen (konzeptionelle Schnittstelle)
- `capabilities(account, market)` → account/permissions/eligible campaign types/formats/limits/verified_at.
- `get_status(resource_id)` und `get_insights(resource_id, date_range)` → API-Rohdaten + Zeit/Währung/Attributionsmetadaten.
- `stage(manifest, idempotency_key)` → *pausierten* Entwurf anlegen, nur mit dafür gültigem Mandat; gibt IDs zurück.
- `activate(resource_id, approval_token_reference, idempotency_key)` → gesondertes Budget- und Aktionsmandat; bestätigt Status.
- `pause(resource_id, authorization_reference)` → ausschließlich im erlaubten Schutz-/Betriebskorridor.
- `update(resource_id, diff, approval_reference)` → nur innerhalb genehmigten Änderungsumfangs.

## Sicherheitskonzept
**Human approval wird außerhalb des JSON-Manifests von einem vertrauenswürdigen Ausführungssystem geprüft.** Das Feld `approval.ref` kann nur als Verweis dienen und ist allein kein Beweis. Auch ein lokaler JSON-Validator ersetzt weder Berechtigung noch Live-Preflight.

- Credentials nur Secret Store; Scopes und Kontobindung minimal; OAuth-Refresh sicher verwalten.
- API-Version, Land, Account-/Produkt-Rechte, Identity/Policy Review, Zahlungsmethode und Creative-Regeln prüfen.
- `draft` wird niemals automatisch zu `active`.
- Bei Timeout: zuerst Query anhand der Idempotency-Key/IDs; niemals blind neu anlegen.
- Budget-Mikroeinheiten, Währungsumrechnung und Rundung im Adapter, im Manifest Betrag als Decimal-String.
- Zielgruppen-Uploads und Konversionserfassung erfordern getrennte Datenschutz-Freigabe.
- Rückgabebeleg: timestamp, Plattform, Account, Resource IDs, current_status, budget/targeting in read-back; keine geheimen Werte.
- Keine Werbeplattform über Browser-Scraping oder heimliche Click-Bots bedienen.

## Besondere OpenAI-/Google-Grenzen
- OpenAI Advertiser API dokumentiert `campaigns`, `ad_groups`, `ads`, Insights und Produktfeeds; tatsächlichen Zugang und neue Formate pro Konto prüfen.
- Google Ads API unterstützt die Erstellung klassischer Video-Campaigns nicht umfassend, obwohl bestehende Daten lesbar sind; alternative unterstützte Kampagnentypen und Ads UI unterscheiden.
- Retail-Datenhaltung und Media-Buying sind unterschiedliche Aufgaben: Google Merchant API ≠ Google Ads API; OpenAI Product Feeds können besondere Zugangsrechte voraussetzen.
