# INTEGRATIONEN — Quellenadapter ohne Lock-in

- **Lokale Daten:** CSV/JSON/JSONL, SQL-Dumps, später DuckDB/PostgreSQL (wenn freigegeben); Dateiquellen bevorzugt für erste Tests.
- **Web/SEO:** GA4 Data API, Matomo Reporting API, Google Search Console; Metriken und Sampling/Thresholding prüfen.
- **Advertising:** Google Ads API, Meta Ads Insights, LinkedIn/TikTok Ads/weitere kontospezifische Exporte. Werbeplattformen berichten attribuierte, nicht zwangsläufig zusätzliche Wirkungen.
- **Social:** native Plattformanalyse und Exportdaten. Metriksemantik je Plattform und Format prüfen.
- **PR:** Erwähnungslisten, Medienresonanz, qualitative Bewertung, repräsentative oder methodisch deklarierte Befragungen.
- **noCRM:** nur rechtmäßig zugängliche, vorzugsweise aggregierte Beziehungs- und Antwortkennzahlen; keine ungebetenen personenbezogenen Joins.
- **Commerce:** Produkt-, Umsatz-, Retouren-, Deckungsbeitragsdaten; Perioden und Währungen harmonisieren.
- **Research/Experimente:** randomisierte Zuweisungen, Teilnahmequoten, Verblindung/Exposition soweit relevant, Nachbeobachtung und Ausschlussregeln.

Der Adaptervertrag liegt unter `integrationen/ADAPTER_CONTRACT.md`. Die technischen Schnittstellenprofile sind Hinweise, keine implementierten API-Verbindungen. Vor jeder echten Verbindung aktuelle Herstellerdokumentation und Kontoberechtigung prüfen. Tokens nie im Projekt ablegen.
