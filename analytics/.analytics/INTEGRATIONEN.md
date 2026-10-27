# INTEGRATIONEN — Quellenadapter ohne Lock-in

- **Lokale Daten:** CSV/JSON/JSONL, SQL-Dumps, später DuckDB/PostgreSQL (wenn freigegeben); Dateiquellen bevorzugt für erste Tests.
- **Web/SEO:** GA4 Data API, Matomo Reporting API, Google Search Console; Metriken und Sampling/Thresholding prüfen.
- **Advertising:** Google Ads API, Meta Ads Insights, LinkedIn/TikTok Ads/weitere kontospezifische Exporte. Werbeplattformen berichten attribuierte, nicht zwangsläufig zusätzliche Wirkungen.
- **Social:** native Plattformanalyse und Exportdaten. Metriksemantik je Plattform und Format prüfen.
- **PR:** Erwähnungslisten, Medienresonanz, qualitative Bewertung, repräsentative oder methodisch deklarierte Befragungen.
- **noCRM:** nur rechtmäßig zugängliche, vorzugsweise aggregierte Beziehungs- und Antwortkennzahlen; keine ungebetenen personenbezogenen Joins.
- **Commerce:** Optional `../e-commerce/` (relativ zum Analytics-Modul) als Quelle für aggregierte Shop- und Funnel-Kennzahlen: Produkt-, Umsatz-, Retouren-, Deckungsbeitragsdaten und Funnel-Übergänge; Perioden, Nenner und Währungen harmonisieren. Nur passende, berechtigt zugängliche Exporte lesen; keine personenbezogenen Rohdaten voraussetzen. Ohne Nachbarmodul direkt bereitgestellte Daten verwenden, keine Pflichtabhängigkeit. Katalog und Feed bleiben beim Schreib-Owner E-Commerce.
- **Research/Experimente:** randomisierte Zuweisungen, Teilnahmequoten, Verblindung/Exposition soweit relevant, Nachbeobachtung und Ausschlussregeln.

Der Adaptervertrag liegt unter `integrationen/ADAPTER_CONTRACT.md`. Die technischen Schnittstellenprofile sind Hinweise, keine implementierten API-Verbindungen. Vor jeder echten Verbindung aktuelle Herstellerdokumentation und Kontoberechtigung prüfen. Tokens nie im Projekt ablegen.
