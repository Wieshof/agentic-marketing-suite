# ARCHITECTURE – Social Media Workspace v0.1

## Ziel und Grenzen
Herstellerneutrales System für fachliche Beratung, kanalübergreifende Content-Planung und kontrollierte Veröffentlichung. Markdown definiert Methoden und Fachwissen. JSON repräsentiert Publisher-Jobs, CSV kann Kalender/Analysen exportieren. Keine implizite Datenbank, kein integrierter Scheduler, kein Netzwerkzugriff und kein sozialer Account werden durch diese Dateien bereitgestellt.

## Daten- und Prozessfluss
`Intent → Quellen/Wissen → Beratung → Content-Idee → Kanalvarianten → Medien/QA → Freigabe → Connector/Preflight → Queue/Publish → Plattformbeleg → Metriken/Optimierung`

- Eine **Content-Idee** erhält eine stabile `content_id`; kanalbezogene Derivate je eine eigene `variant_id` und Kanal-/Konto-Zuordnung.
- Pro Variante eigene Copy, CTA, Asset-Referenzen, Rechte, Zeitfenster, revisionsgebundene Freigabe, QA-Befund, API-Fähigkeit und Veröffentlichungsnachweis.
- Ein Veröffentlichungsvorgang ist eine **kompensierbare Zustandsmaschine**, keine LLM-Aussage. Externe Realität ist maßgeblich.
- Aufträge können rein beratend enden. Es wird nicht stets veröffentlicht.

## Veröffentlichungszustände
`idea → draft → in_review → approved → scheduled → publishing → published`; Alternativen: `blocked`, `failed`, `unknown`, `cancelled`, `archived`. Übergänge sind zu validieren. `publishing → unknown` bei Timeout ohne Bestätigung; erst Remote-Lookup, dann manueller Abgleich, **kein** blinder Zweitversand.

## Einzelne Wissensbereiche
- `.social-media/methoden/` = fachliche Arbeitsanleitungen; `.social-media/kanaele/` = kanalbezogene Beratung/Constraints; `.social-media/formate/` = Gestaltungs-/Produktionsanleitung; `.social-media/integrationen/` = Schnittstellenmodelle und Tool-Entscheidung.
- `.social-media/STATE.md` = aktueller Zustand, referenzierte Artefakte, offene Freigaben; `.social-media/LOG.md` = echte Operationen append-only, mit UTC-Zeit und Status; `.social-media/HISTORY.md` = fachliche Beschlüsse/Revisionen append-only; `archiv/` = Originale, veröffentlichte Snapshots und frühere freigegebene Fassungen.
- Bedarfsgesteuerte Ergebnisordner außerhalb `.social-media/`; keine vorgefertigten Posts bei Installation.

## Nachbarmodule (optional)
- `../marketing/` liefert Unternehmensziele, Positionierung, Zielgruppen, Leitidee.
- `../pr/` liefert Krisenkommunikation, Medienbotschaften, Stellungnahmen.
- `../website/` stellt Links, Landings, Bilder/Fakten; `../creative/` visuelle Produktion/Brandassets.
- Kein Modul ist Pflicht; nur lesender Zugriff bei Berechtigung; Schreibzugriffe auf fremde Module ausschließlich nach expliziter Vereinbarung.

## Verlässlichkeit
- Credentials aus Vault; verbindlicher Kanal+Konto-Bindung; ACLs je Konto; minimale Scopes; Tokenwechsel/Ablauf erkennen.
- Veröffentlichungs-Jobs mit Idempotency-Key und Asset-Hash/Revision; bei unklarer API-Antwort Remote-Reconciliation.
- Veröffentlichtes nach Rückmeldung mit `external_post_id`, `external_url` (falls verfügbar), Zeitpunkt und Statusbeleg vermerken.
- Kommentar-/DM-Automation grundsätzlich gesondert erlauben; keine unbeaufsichtigte eskalierende Diskussion.
