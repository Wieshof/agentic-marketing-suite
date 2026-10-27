# Branding in der Agentic Marketing Suite

Branding ist der zehnte optionale Fachbereich. Der direkte Einstieg bleibt [AGENT.md](../AGENT.md); [RULES.md](RULES.md) bindet bei vorhandener Suite deren Mindeststandards ein. Die [mitgelieferte Spezifikation](../Branding-Conceptual-Architecture-Organizational-Knowledge-Specification-v0.1.md) bleibt als ursprünglicher Entwurf erhalten; diese Integrationsnotiz beschreibt den konkreten Suite-Stand.

## Fachliche Zuständigkeit und Zugriff

Branding führt Markenentscheidungen, Marketing die Markt-/Kampagnenstrategie, Creative die Gestaltung, E-Commerce den Katalog/Feed und Analytics die gemessene Wahrnehmung. Unternehmensfakten brauchen belegbare Quellen; Business-DNA kann sie optional bereitstellen und muss nicht installiert sein. Ein Markenversprechen macht eine Produkteigenschaft nicht zum Fakt. Ein Branding-Review ist keine Messung und keine Rechte- oder Aktionsfreigabe.

Die Nachbarn fragen passende Markeninformationen per `brand-context-request` an: `request_id`, `requester`, `purpose`, `audience`, `topics`, optional `brand_ids`. Nur berechtigt zugängliche Dateien verwenden; die Kennzeichnung `public/shared/restricted` authentifiziert niemanden. Die Auswahlrechte und tatsächliche Weitergabe prüft der Harness.

Der vorhandene Offline-Builder exportiert ausschließlich formal freigegebene Profile und angeforderte Themen innerhalb der erlaubten Sichtbarkeit; Entwürfe und abgelöste Profile werden ausgeschlossen. Auch für `restricted` braucht der Empfänger eine reale Berechtigung. `source_refs`, Entscheidungsreferenzen und Einschränkungen vor Weitergabe prüfen; ein Pack ist kein automatischer öffentlicher Export. Beratung anhand von Entwürfen erfolgt ausdrücklich als Entwurf, außerhalb eines autoritativen Context Packs. Vor Verwendung den aktuellen Quellstatus, die Version, Marke, den Geltungsbereich und eventuelle Widerrufe kontrollieren; bereits erstellte Packs aktualisieren sich nicht automatisch.

## Lokale Werkzeuge

Vom Suite-Root aus, ausschließlich mit fiktiven Beispielen:

```sh
python3 branding/.branding/tools/test_contracts.py
python3 branding/.branding/tools/lint_records.py --kind brand-profile branding/.branding/beispiele/demo-brand-approved.json
python3 branding/.branding/tools/build_brand_context.py --request branding/.branding/beispiele/demo-request-public.json --profiles branding/.branding/beispiele/demo-brand-approved.json branding/.branding/beispiele/demo-brand-draft.json --out /tmp/branding-demo-context.json
```

Der Builder erzeugt nur eine lokale Datei und sendet nichts. Ausgabepfade bewusst wählen; vorhandene Dateien können überschrieben werden. Die Modulwerkzeuge sind als Python 3.10+ dokumentiert; die Suite prüft ihre Kompatibilität zusätzlich in ihren vorhandenen Python-3.9-/3.13-Jobs. Lokale Lints sind begrenzte Formprüfungen, keine vollständige JSON-Schema-, Identitäts-, Markenqualitäts- oder Rechtsprüfung.

## Suite-Verträge und Statusübersetzung

Die sechs lokalen Branding-Verträge bleiben unter [schemas/](schemas/); sie werden nicht als neue Suite-Kernverträge umbenannt. Für automatisierte Mehrmodulübergaben gelten zusätzlich die bestehenden [Suite-Verträge](../../.suite/INTERFACES.md):

| Branding | Suite |
|---|---|
| fachlicher Markenauftrag | `work-order.lead_module: branding`, optional zuständige `supporting_modules` |
| Brand Profile, Guidelines, Decision oder Context Pack | `artifact.owner_module: branding`; eindeutige Artefakt-ID ergänzen, `path` ab Suite-Root, lokale `version` übernehmen, bei freigegebenen Artefakten tatsächlichen SHA-256 und geklärte Rechte ergänzen |
| `draft` | `artifact.status: draft` |
| `in_review` | `review` |
| `approved` | nur mit nachgewiesener menschlicher Entscheidung, gültigem Geltungsbereich, aktuellem Hash und geklärten Rechten `approved`; andernfalls `review` |
| `rejected`, `superseded`, `retired` | `archived`; lokale Unterscheidung/Begründung im Original erhalten; nicht als aktuelle Vorgabe nutzen |
| technisch veröffentlichte Datei | `published` erst mit eigener bestätigter Ausführung; nie allein aus einer Brand-Freigabe ableiten |

Ein Brand Review bindet sich mit `artifact_id` und `artifact_version` an das konkrete fremde Artefakt. Für einen Suite-Review `review_id` als `id` übernehmen, `dimension: consistency` (bzw. begründet `expert`), `reviewed_at`, Findings und belegbare `evidence_refs` ergänzen. `pass` nur ohne blockierende Findings; Für diese konservative Branding-Übersetzung `warning` nur ohne `major`/`critical` und mit menschlichem `risk_accepted_by`. `fail` oder blockierende Findings werden `blocked`; `inconclusive` wird `not_checked`. Der lokale Review bleibt unverändert erhalten. Das mitgelieferte Beispiel `demo-review.json` enthält eine `major`-Abweichung trotz lokalem `warning`: für diesen Handoff wird es deshalb als `blocked` übergeben, statt eine menschliche Risikoannahme zu unterstellen. Fehlende Nachweise oder Risikoannahme niemals erfinden.

## Menschliche Entscheidung und spätere Außenwirkung

Eine lokale `brand-decision` dokumentiert eine Markenrichtung, autorisiert aber weder Versand noch Deployment, Budget oder Markenanmeldung. Falls die [Freigabe-/Audit-Fähigkeit](../../.suite/APPROVALS.md) verwendet wird, die tatsächliche Anforderung mit Artefaktversion/Hash und Reviews erstellen; die authentifizierte menschliche Entscheidung bzw. der Widerruf wird dort als eigenes Ereignis erfasst. `decision_ref`/`approval_ref` referenzieren diesen Nachweis. Namen oder JSON-Felder sind keine Authentifizierung.

Für Außenwirkung erstellt das jeweils ausführende Modul eine gesonderte konkrete Aktionsfreigabe und prüft sie im Harness/Adapter unmittelbar vor der Ausführung. Branding fügt keine Dashboard-Schreib- oder Freigabefunktion hinzu. Änderungen an gültigen Markenregeln erhalten eine neue Version und einen Handoff an tatsächlich betroffene Artefakt-Owner; keine stillen Änderungen in fremden Modulen.

## Prüfstand

Die Repository-Prüfung führt die Branding-Vertragstests und Integrationstests mit echten lokalen Context-Exporten aus. Fachliche Harness-Fälle aus [TESTFAELLE.md](TESTFAELLE.md), etwa Beratungsqualität und Review eines echten fremden Artefakts, bleiben bei konkreter Nutzung auszuführen. Ein erfolgreicher Offline-Test behauptet keine reale Markenentscheidung oder externe Veröffentlichung.

## Übergabe aus Business-DNA

Bei installierter Suite ist Business-DNA als elfter Fachbereich vorhanden, bleibt aber optional. [Business-DNA-Requests und CLI](../../business-dna/.business-dna/SUITE.md) liefern quellenbezogene Claims. Deren `claim_id`, Status, Version, Geltung und Quellen als Referenzen erhalten; einen geplanten Produktnutzen nicht als erwiesenes Markenversprechen ausgeben. `brand-context-request.audience` und `context-request.visibility_max` sind unterschiedliche lokale Felder und keine gegenseitige Authentifizierung. Erst nach fachlicher Bewertung eine Markenentscheidung entwerfen; eine Unternehmensinformation erzeugt keine Markenfreigabe.
