# ADAPTER_CONTRACT – Produktions- und Prüfintegrationen

## Adapterfähigkeiten
- `capabilities()`: unterstützte Medien, Formate, Version, Profile, lokale/Cloud-Verarbeitung, Lizenzstatus.
- `prepare(job_manifest)`: Eingangsprüfung, Spezifikation, Schätzung; **keine Aktion nach außen**.
- `render(job_manifest, source_assets)`: Versionsgeschützter Export inkl. Hash und Provenienz.
- `inspect(file, profile)`: maschinenlesbarer technischer Report (Regel-ID, Schweregrad, Fundstelle).
- `perceptual_review(file, references)`: visueller/auditiver Bericht mit Unsicherheiten, gern unabhängiger Prüfer.
- `release(artifact, approval)` nur bei **nachgewiesener, gültiger Freigabe** und separater Ausführungsberechtigung.

## Rückgabeformat
`{job_id, artifact_id, version, sha256, operation, status, timestamp, tool, tool_version, profile_id, findings, evidence_uri}`; Dateihashes und Profile sind verpflichtend für technische QA.

## Status & Fehler
`unavailable`, `not_authorized`, `unsupported`, `needs_specification`, `proof_only`, `qa_failed`, `approval_pending`, `approved`, `released`. Keine falsche Erfolgsmeldung aus einem HTTP-202 oder gestarteten Hintergrundjob.

## Sicherheit und Lock-in
Assets und Quellen bleiben im Arbeitsverzeichnis; externe Uploads sind opt-in. Zugangsdaten nur Secret-Store. Keine Verwendung eines einzigen Anbieters als Pflicht. Bei Adapterfehler bleibt verifizierter Zustand erhalten, Wiederaufnahme idempotent, keine Doppelbestellung.
