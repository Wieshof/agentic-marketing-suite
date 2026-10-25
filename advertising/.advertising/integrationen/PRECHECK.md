# Validierung und Grenzen
`python3 advertising/.advertising/tools/validate_manifest.py path/to/manifest.json`

Der **lokale Validator** kontrolliert Format und grundlegende Risikogates. Ein `PASS` ist *keine* Freigabe, *kein* geprüfter Kontozugang und *keine* Zusage einer ausführbaren API-Aktion. Es werden **nie Netzwerkanfragen** ausgeführt.

Der [DRAFT_MANIFEST_DEMO.json-Datensatz](../beispiele/DRAFT_MANIFEST_DEMO.json) ist ausdrücklich fiktiv und dient nur zur Veranschaulichung; `https://example.org/not-a-real-site` ist kein echtes Kampagnenziel. `account_ref: NOT_CONNECTED` verbietet echte Aktionen.
