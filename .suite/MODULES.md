# Modulregister v0.2

| Modul | Zuständigkeit | Geeignete eingehende Aufgaben | Möglicher Ausgabevertrag |
|---|---|---|---|
| marketing/ | Unternehmens-, Marketing- und Kommunikationsstrategie | Ziele, Positionierung, Marketingkonzept | Strategie, Zielgruppe, Leitplanken |
| pr/ | Medien, Öffentlichkeiten, Reputation | Presse, Journalist:innen, Krisen | Pitch, Q&A, Statement, Medienplan |
| social-media/ | Social-Strategie, Community, organischer Content | Redaktion, Kanalwahl, Posts, Reels | kanaladaptierte Pakete, Publishing-Manifest |
| website/ | Webberatung und noCMS | Audit, IA, Landingpage, Website | Sitemap, HTML/CSS/JS, Release |
| advertising/ | Bezahlte Werbung, Media und Kampagnen | Creative Brief, Anzeigen, Shopping | Mediaplan, Anzeigenset, Budgetvorschlag und Budgetprüfung |
| creative/ | Design, Corporate Design, Medienproduktion | Key Visual, Print, Bild, Video, Audio | Quellen, Medien, Export und QA |
| noCRM/ | Individuelle 1:1-Kommunikation | Rückfrage, Begleitung, Antwortentwurf | Nachricht, rechtmäßiger Versandnachweis |
| analytics/ | Evidenz, Messung, unabhängige Wirkungsevaluation | Ergebnisse, Qualitätslücken, KPIs | Analyse, Hypothesen, Verbesserungsauftrag |
| e-commerce/ | Online-Shop-Beratung, Produktdaten, Feeds, Checkout und Angebote; kein Shop-Betrieb | Shop-System, Katalog, Merchant-Center-Feed, Checkout, Order Bump, Upsell, Preisaktion | Katalog (CSV/JSON), Feed (XML/TSV), Funnel-Spezifikation, Preis-/Feed-Prüfung und Freigabevorlage |
| business-dna/ | Organisationswissen, Quellen, Erkenntnisstatus und zweckbezogener Kontext | Firmenprofil, Produktreife, Quellen-/Konfliktprüfung, Wissenspflege | Claims, Quellenregister, Context Pack, Änderungsvorschlag |
| help/ | Hilfe, Lernen und Orientierung ohne Ausführungsrolle | Einstieg, Begriffe, Dokumentverständnis, Fachbereichswahl, Funktionsgrenzen | Erklärung, Guide, Dateiinventar, kopierbarer Fachauftrag |
| branding/ | Markenstrategie, Identität, Markenarchitektur und Brand Governance | Positionierung, Naming, Tonalität, Guidelines, Markenreview | Brand Profile, Decision, Context Pack, versionsgebundener Brand Review |

**Zuständigkeit Produktfeed:** Schreib-Owner von Katalog und Feed ist `e-commerce/`; `advertising/` nutzt den Feed für Shopping-Kampagnen und meldet Befunde zurück.

**Regel:** Nur benötigte Module aktivieren. Benachbarte Verzeichnisse sind optionale Quellen, keine Ausführungsermächtigung. Direkter Fachauftrag bleibt beim Fachspezialisten, ein fachübergreifender Auftrag verwendet `.suite/WORKFLOW.md`.

**Freigaben:** Die Module erstellen Vorschläge, Prüfungen und Freigabevorlagen. Die menschliche Budgetfreigabe erteilt ausschließlich eine handlungsberechtigte Person mit Konto, Budgetlimit, Zeitraum und konkreter Aktion; eine KI-Prüfung ersetzt diese Autorisierung nicht. Dasselbe gilt für Preis- und Feed-Freigaben. Bestehende Gates und Ausführungsrechte bleiben unverändert.

**Zuständigkeit Marke:** `branding/` ist Schreib-Owner strategischer Markenentscheidungen. Marketing verantwortet Marktbearbeitung und Kampagnenstrategie, Creative die Gestaltung, die Kanäle ihre Umsetzung, Analytics die empirische Wirkung. Bestehende Module bleiben ohne Branding arbeitsfähig. Business-DNA ist als elfter optionaler Fachbereich integriert; auch externe Installationen bleiben als berechtigte Quelle verwendbar. [Übergaben und Status](../branding/.branding/SUITE.md).

**Zuständigkeit Unternehmenswissen:** `business-dna/` pflegt quellenbezogenes Organisationswissen. Es definiert weder die gewünschte Marke noch Shop-Katalog/Preise oder empirische Wirkung. Faktenkorrekturen als referenzierte Vorschläge an den zuständigen Owner zurückgeben. `verified` ist kein Veröffentlichungsstatus; [Kontext und Suite-Mapping](../business-dna/.business-dna/SUITE.md).

**Zuständigkeit Hilfe:** `help/` unterstützt Verständnis und Einstieg; Produktion bleibt beim zuständigen Fachbereich. Vorgeschlagene Aufträge sind noch keine tatsächlich weitergeleiteten Aufgaben. Module nur nach beobachteter Verfügbarkeit empfehlen; Konfiguration und erfolgreiche Tests getrennt prüfen. [Kontext und Übergaben](../help/.help/SUITE.md).
