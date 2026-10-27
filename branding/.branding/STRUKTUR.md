# Dateistruktur und dynamische Ergebnisse

`.branding/` enthält **alle** internen Regeln, Methoden, Schemas, Hilfsprogramme und Zustandsreferenzen. Operative Markendokumente gehören nicht hierher. `input/` ist temporär und `archiv/` erhält unveränderte Importe und ältere freigegebene Versionen.

Nur bei tatsächlich anfallender Arbeit geeignete Ordner anlegen, z. B. `strategie/`, `identitaet/`, `verbal/`, `visual/`, `portfolio/`, `guidelines/`, `research/`, `reports/`, `briefs/`. Keine leeren Pflichtordner für jedes Thema. Bei mehreren Marken Ergebnisse unter eindeutigem `brand_id`-Scope getrennt führen.

Das Setup erzeugt niemals ungefragt Ergebnisse, externe Veröffentlichungen oder Beispielkunden im Produktionsbestand. Fiktive Beispiele liegen ausschließlich unter `.branding/beispiele/`; lokale Vertragstests unter `.branding/tools/test_contracts.py`. Suite-Integrationstests liegen bei vorhandener Suite unter `.suite/tests/`.

Jede als verbindlich markierte Strategie benötigt Versionsnummer, Geltungsbereich, zugehörige Entscheidungsreferenz und menschlichen Freigabenachweis. Quell-Dateinamen allein sind kein Berechtigungsnachweis.
