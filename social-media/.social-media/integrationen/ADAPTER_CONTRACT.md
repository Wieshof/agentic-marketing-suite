# Publishing Adapter Contract v0.1

## Trennung der Zuständigkeiten
**Social-Media-Spezialist:** Strategie, Redaktion, Content-Varianten, Produktions- und QA-Status, Freigabeanfrage.

**Publisher Adapter:** deklarierte Capability für `channel+account+format` nachweisen, Medien-Upload, Scheduling, Veröffentlichung, Statusabfrage und Rückgabe externer IDs. Er entscheidet nicht selbst über Inhalt, Freigabe oder zusätzliche Plattformen.

**Mensch / Autorisierung:** Veröffentlichung und Kosten im konkret gewünschten Rahmen explizit genehmigen, Tokens sicher freigeben.

## Logischer Interface-Vertrag

```text
capabilities(account) -> supported_types, scopes, limits, verification_time
validate(job) -> warnings[], errors[], effective_format
prepare_assets(job) -> media_handles[] | blocked
schedule(job, approved_at) -> remote_schedule_id | not_supported | unknown
publish(job, approved_at) -> remote_post_id | unknown | rejected
status(job_id / remote_id) -> actual_external_state
metrics(remote_post_id) -> metrics + definitions + timestamp | not_supported
cancel(remote_schedule_id) -> confirmation | unknown | not_supported
```

Alle Methoden haben klare Auth- und Zeitgrenzen, strukturierte Fehlercodes und Event-Logs **ohne Secrets**. Implementierte Methoden dürfen `not_supported` zurückgeben, niemals simulierte Erfolgsmeldungen.

## Approval Boundary
`approved` ist an Content-Hash, Account, Zielkanal, geplanten Zeitpunkt/Zeitraum, Medien, Rechts- und Markenprüfung gebunden. Nach Änderung: Freigabe invalidieren. `publish` benötigt getrennte Ausführungsautorisierung (z. B. explizit erteilte Einzelfreigabe oder nachprüfbare Policy für einen engen Zeitraum).

## Exactly-once-Näherung
Kunde generiert stabile `job_id` und `idempotency_key`; Adapter schreibt `external_id` sobald bekannt. Bei Timeout/5xx zunächst Remote-Status nachprüfen. Wo Provider keine Idempotenz bietet, lokale Sperre+Reconciliation; kein automatischer Zweitversand bei `unknown`.

## Kalender und Retry
UTC-Zeit speichern plus Zielzeitzone und lokale Anzeige; DST-Übergänge validieren. Queue-Eintrag nicht mit Plattform-Scheduling verwechseln. Erfolgreicher Eintrag bei Scheduler hat eigenen `queue_id`; Plattformbeleg entsteht erst separat. Rate-Limits respektieren; Exponential Backoff nur für eindeutig nicht ausgeführte Operationen.

## Security
OAuth Least Privilege, Tokens im Secret Store, getrennte Account-Zuordnung und Revocation, isolierte Media-URLs mit begrenzter TTL wo Provider kompatibel, keine privaten Asset-Pfade öffentlich exponieren, keine Nutzung fremder Browser-Sessions ohne Erlaubnis.
