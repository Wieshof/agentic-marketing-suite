# MEDIA_BUYING — Aktivierung, Kontrolle und Belege
**Nur lesen bei intendierter kostenpflichtiger Aktion oder Werbekonto-Vorbereitung.** Dieses Paket implementiert standardmäßig **keinen aktiven Connector**.

## Freigabe-Gates
1. **Strategisches Gate:** Ziel, Angebot, Zielgruppe, kreative Aussagen, Zielseite und Alternativen geprüft.
2. **Compliance Gate:** Rechts-/Plattformrichtlinien, Claims, Rechte, Datenschutz, Identität, ggf. politische/regulierte Werbung geprüft; Unsicherheiten als Blocker.
3. **Budget Gate:** Betrag, Währung, Zeitraum, Laufzeit, Tages-/Gesamtdeckel, Billing-Account, Risiko-/Stop-Loss-Regeln; klar, ob Betrag inklusive Nebenkosten ist.
4. **Asset Gate:** finaler Text/Medien/Varianten, Produktpreise und URLs geprüft, Werbekennzeichnung.
5. **Consent & Authority:** explizite Freigabe für *genau die* Kampagne, den Betrag und das gewählte Konto; separate Ausführungsberechtigung des ausführenden Tools.
6. **Preflight:** Kontozugang, API-/Format-/Länderfreigabe, Tracking-Consent, Produktfeed, URL-Status, optional Testupload. Keine realen Änderungen ohne legitimen Auftrag.
7. **Staging:** wenn autorisiert im pausierten Zustand vorbereiten. Staging im Werbekonto ist bereits eine externe Aktion und braucht Auftrag; nicht automatisch „aktiv“ schalten.
8. **Activation:** aktivieren nur nach passender Livefreigabe; Plattformantwort, IDs und tatsächlichen Status dokumentieren.
9. **Verification:** Kampagnenstatus und erste Auslieferung später gesondert abrufen. API-Erfolg beim Create bedeutet nicht Live-Auslieferung.
10. **Recovery:** vor Retries idempotente IDs/Schlüssel; bei Timeout erst Plattformzustand prüfen, keine Duplikate. Budgetüberschreitung → pausieren nur nach vereinbarter Autorität/Eskalationsregel.

## Achtung bei KI-Ads
OpenAI ChatGPT Ads besitzt Ads Manager und Advertiser API, *aber Account-Zulassung, Review und Produktfeed-Rechte sind kontoabhängig*. Werbung beeinflusst ChatGPT-Antworten nicht; Sponsored Agents und neue visuelle Formate können regional, kontobezogen oder nur Pilot sein. Andere KI-Anbieter niemals aufgrund ihres Namens als buchbaren Paid-Kanal darstellen.

## Status-Lebenszyklus
`draft → ready_for_review → approved → staged → active → paused/completed`, zusätzlich `rejected`, `error` mit begründetem Nachweis. Keine Status-Sprünge von `draft` nach `active`. Budgets in Micros nur im spezifischen Plattformadapter umrechnen; das kanonische Format speichert **Dezimalbetrag + ISO-Währung**.
