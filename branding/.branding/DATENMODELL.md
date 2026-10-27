# Canonical Brand Data Model v0.1

## Artefakte

- `brand-profile` – benannte Marke mit strategischen Feldern und sichtbarem Status.
- `brand-decision` – Vorschlag / Beschluss zu Positionierung, Naming, Voice, Identity oder Architektur.
- `brand-context-request` – Zweck, Empfänger und benötigte Aspekte eines Exports.
- `brand-context-pack` – selektiver Transfer bestehender gültiger Markeninformation.
- `brand-review` – konkrete Prüfung einer Artefaktversion.
- `brand-event` – tatsächlich stattgefundenes Status-/Änderungsereignis.

## Trennung von vier Zuständen

- `lifecycle_status`: draft / in_review / approved / rejected / superseded / retired.
- `evidence_status`: verified / declared / planned / hypothesis / disputed / unknown.
- `implementation_status`: not_started / in_progress / implemented / partially_implemented / not_applicable.
- `measurement_status`: not_measured / baseline / observed / inconclusive.

Achtung: Freigegebenes strategisches Artefakt ist **keine Aussage** über Markenrecht, tatsächliche Implementierung oder Außenwirkung. Versionsreferenz plus menschliche Freigabe sind notwendig, bevor `approved` öffentlich als beschlossene Guideline bezeichnet wird.

## Technischer Mindestkontrakt

Stable ID, Version, Zeitbezug, Geltungsbereich, Quell- und Abhängigkeitsreferenzen, Freigabenachweis (falls approved), Visibility sowie limitations. JSON-Schemas liegen unter `schemas/`. Es existiert keine Pflichtdatenbank.
