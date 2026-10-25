# Provider-unabhängige Integration

Die kanonische Handlung ist `draft`, `review`, `authorize`, `send`, `check_status`, `cancel` oder `import_inbound`. Fachmethoden kennen keine Zugangstokens oder Vendor-SDKs. Adapter legen Fähigkeiten per `capabilities` offen: erlaubte Zwecke, Medienformate, freigeschaltete Accounts, Templatepflicht, Limits, mögliche Sende-/Lesefunktionen, Zustellstatus und Kosten.

**Request für echtes Senden** (Konzept, nicht im Paket implementiert): `action_id`, `draft_id`, `contact_id`, `channel`, `purpose`, `content_hash`, `recipient_handle`, `authorization_ref`, `legal_basis_evidence_ref`, `idempotency_key`, `timeout`, `cost_limit`.

**Response:** `provider`, `account_id`, `provider_message_id`, `accepted_at`, `status`, `error`, `status_checked_at`; `accepted` ≠ `delivered`. Adapter speichern keine Tokens im Projektordner.

Aktuell ausgeliefert: lokale Schema-/Preflight-Validierung ohne Netzverkehr oder externen Versand. Später geeignet: Gmail, Microsoft Graph, WhatsApp Business Platform, Telegram Bot, eigener Website-Chat, Telefondienst. Signal nur nach besonderer Prüfung möglicher Integrationen, keinesfalls als offiziell unterstützte Bot-API ausgeben.

Priorität: Inbox-Import mit Autorisierung → individuelle Antwortentwürfe → menschliche Freigabe → gesicherter Sendeadapter → Status/Recovery → ggf. teilautomatische, eng begrenzte Routineantworten.
