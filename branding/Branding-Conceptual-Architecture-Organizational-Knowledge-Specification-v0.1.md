# Branding – Conceptual Architecture & Organizational Knowledge Specification v0.1

**Status:** Architektur- und Implementierungsentwurf  
**Version:** 0.1 · **Datum:** 27. Oktober 2026  
**Kontext:** Eigenständiger Fachbereich; optionale Integration in die Agentic Marketing Suite  
**Lizenz des mitgelieferten Codes und der eigenen Dokumentation:** MIT (vorbehaltlich Rechte Dritter)

## 0. Executive Summary

Branding ist ein eigenständiger, KI-gestützter Fachspezialist für strategische Markenbildung und operative Markenführung. Es handelt sich ausdrücklich **nicht** um ein bloßes Werkzeug zur Logoerstellung oder um eine starre Abfolge von Formularen. Der Spezialist analysiert, entwickelt fundierte, kreative Empfehlungen, erstellt nachvollziehbare Markenartefakte, beurteilt Umsetzungen anderer Module und sorgt für eine konsistente, aber veränderbare Markenidentität.

Im Zentrum stehen drei voneinander zu unterscheidende Ebenen: **Realität** (belegbare Unternehmensinformationen; Business-DNA), **Markenentscheidung** (beabsichtigte Bedeutung, Markenversprechen und Leitlinien; Branding) und **Wahrnehmung** (beobachtete Assoziationen und Wirkung; Analytics/Marktforschung). Keine dieser Ebenen darf unbemerkt mit einer anderen gleichgesetzt werden.

Das Modul funktioniert vollständig ohne Business-DNA, Marketing, Creative, Analytics, Datenbank, Dashboard oder speziellen KI-Harness. Sind geeignete Nachbarmodule vorhanden, nutzt es relevante Informationen und übergibt zweckbezogene Artefakte. Die Fachanweisungen liegen unter `.branding/`; Ergebnisse entstehen außerhalb dynamisch nach Bedarf. Interne Log- und Historiendateien dokumentieren tatsächliche Änderungen und Entscheidungen.

## 1. Ziele

1. Fachlich fundierte Beratung über Positionierung, Differenzierung und Markenführung liefern.
2. Markenkonzept und Brand Guidelines als **revisionsfähige, portable und nachvollziehbare** Artefakte erstellen.
3. Bestehende Marken analysieren und geeignete Verbesserungen vorschlagen.
4. Eine konsistente Markenidentität über Website, Werbung, PR, Social Media, noCRM, Print und weitere Kontaktpunkte fördern.
5. Unterschiede zwischen Vision, Beschluss, Umsetzung und empirischer Wahrnehmung konsequent sichtbar machen.
6. Markenänderungen versionieren und ihre Auswirkungen auf abhängige Artefakte nachvollziehen.
7. Portabel bleiben: Markdown und JSON als Standard; SVG, Bilder und weitere Medien nur soweit benötigt.
8. Dem Menschen Arbeit abnehmen: eigenständige Vorschläge vor Rückfragen, keine verpflichtende Interviewstrecke.

### 1.1 Nichtziele

- Keine eigene Agenten-Runtime, kein eigener Harness, kein zentraler Orchestrator.
- Kein generelles CRM, kein Medienbuchungssystem, kein CMS und keine Grafiksuite.
- Keine verpflichtende Kundendatenbank, kein Wissensgraph-Server und keine Modellbindung.
- Keine automatische Eintragung von Markenrechten oder rechtlich verbindliche Markenrecherche.
- Keine Gleichsetzung von Styleguide-Konformität mit Markt- oder Markenwirkung.
- Keine automatische externe Veröffentlichung oder Budgetfreigabe durch das Branding-Modul.

## 2. Fachliche Begriffe und Grenzen

**Marke:** Identifizierbares Versprechen und Summe der mit einer Organisation, einem Produkt oder Angebot verbundenen Wahrnehmungen und Erfahrungen.  
**Markenidentität:** Strategisch definierte Merkmale, Werte und die angestrebte Bedeutung.  
**Markenimage:** Tatsächlich bei Zielgruppen vorhandene Assoziationen; nur durch geeignete Beobachtung beurteilbar.  
**Positionierung:** Gewollte relative Bedeutung und Differenzierung in einem Wettbewerbs- und Nutzungskontext.  
**Markenarchitektur:** Geordnetes Verhältnis mehrerer Organisations-, Produkt-, Angebots- oder Submarken.  
**Corporate Design:** Visuelles Ausdruckssystem; Teil, nicht Gesamtheit der Markenführung.  
**Brand Governance:** Geltungsbereich, Verbindlichkeit, Änderungs- und Prüfprozess markenbezogener Vorgaben.

**Abgrenzung:** Business-DNA ist die bevorzugte Quelle für Unternehmensfakten, aber niemals die einzige mögliche Quelle; Branding verwaltet strategische Markenentscheidungen; Creative gestaltet Medien, Marketing bestimmt Marktbearbeitung, PR und Social Media verantworten ihre Kanäle, Analytics beurteilt empirische Wirkung.

## 3. Beraterrolle und menschliche Interaktion

Der Spezialist agiert als **Brand Strategist & Brand Management Advisor**. Er darf begründet gegen unpassende Designwünsche, nicht belegbare Versprechen oder inkonsistente Kampagnen empfehlen; er soll Alternativen anbieten, ohne Entscheidungen als getroffen auszugeben. Der Standard ist eine prägnante fachliche Diagnose mit nützlichem Entwurf und gekennzeichneten Annahmen.

**Sofortstart:** Wird nur `branding/AGENT.md` gelesen und liegt kein fachlicher Auftrag vor, lautet die erste Antwort genau: **„Wobei kann ich Ihnen rund um Ihre Marke helfen?“** Liegt ein Auftrag vor, soll direkt gearbeitet werden. Bei Fortsetzung soll der Spezialist relevante aktuelle Ergebnisse und `.branding/STATE.md` berücksichtigen. Dateiveränderung und externe Aktionen benötigen einen tatsächlichen Auftrag und verfügbare Berechtigung; das bloße Einlesen des Agent-Dokuments löst keine Änderung aus.

Keine Pflicht zur Vollerhebung. Fehlende Informationen werden aus vorhandenen Unterlagen extrahiert, mit Annahmen gekennzeichnet und nur gebündelt abgefragt, wenn sonst eine wesentliche Entscheidung riskant wäre.

## 4. Fachlicher Leistungsumfang

1. **Audit & Research:** Brand Audit, Markeninventar, Zielgruppensicht, Wettbewerber und Kategoriecodes.
2. **Markenstrategie:** Differenzierung, Positionierung, Versprechen, Markenwert, Mission-/Purpose-Bezug.
3. **Identität & Persönlichkeit:** Markenkern, Werte, Charakter, Archetypen als optionales Denkwerkzeug.
4. **Architektur & Portfolio:** Dachmarke, Produktmarke, Submarke, Naming-Hierarchie.
5. **Verbal Identity:** Naming, Claim, Markenstory, Tonalität, Terminologie, Sprachvarianten.
6. **Visual Identity Direction:** Designbriefing, gestalterische Prinzipien, Logo-/Schrift-/Farbkonzept; Ausführung durch Creative, sofern vorhanden.
7. **Brand Experience:** Kontaktpunkte, Customer/Brand Journey, Verhalten, Serviceversprechen.
8. **Governance:** Guidelines, Freigaben, Konsistenzprüfungen, Änderungsmanagement.
9. **Measurement:** Awareness, Salience, Associations, Consideration, Experience, Brand Lift und qualitative Insights.
10. **Integration:** Brand Briefs, Asset-Handoffs und selektive Context Packs für andere Fachbereiche.

## 5. Prinzipien der Methodenwahl

- **Problemorientiert:** Methode aufgrund des Auftrags wählen, nicht aufgrund eines starren Framework-Katalogs.
- **Minimal ausreichend:** Ein einzelner Claim-Check darf keine vollständige Markenarchitektur verlangen.
- **Belegorientiert:** Positionierungshypothesen gegen Markt- und Unternehmensinformationen prüfen.
- **Kreativ und kritisch:** Mehrere Optionen, erkennbare Auswahlkriterien, fachliche Empfehlung.
- **Einheitlich, nicht identisch:** Markenprinzipien stabil halten, Kanalgestaltung kontextbezogen anpassen.
- **Nachvollziehbar:** Aussage, Quellenbezug, Entscheidung, Version, Einschränkung dokumentieren.
- **Kontinuierlich:** Zwischen Projekten fortschreibbar, ohne durchgängige Runtime.

## 6. Logische Domänen und Zuständigkeiten

| Domäne | Kanonische Verantwortung | Wichtige Ausgaben |
|---|---|---|
| Brand Discovery | Relevante Markenausgangslage | Brand Audit, Quellregister |
| Brand Strategy | Strategische Markenentscheidungen | Positionierung, Brand Platform |
| Brand Identity | Gewünschte Selbstdarstellung | Markenpersönlichkeit, Kernwerte |
| Verbal Identity | Sprachlicher Ausdruck | Tone-of-Voice, Naming-Rules, Claims |
| Visual Direction | Gestaltungsprinzipien | Creative Brief, Designsystem-Vorgaben |
| Brand Architecture | Markenbeziehungen | Architekturkarte, Namenshierarchie |
| Brand Experience | Verhalten an Kontaktpunkten | Experience Principles, Touchpoint-Guidelines |
| Governance | Gültigkeit und Änderungswesen | Decision Record, Guidelines, Reviews |
| Brand Measurement | Evidenz über wahrgenommene Marke | Research Brief, Brand Health Assessment |
| Interoperability | Zweckbezogene Weitergabe | Brand Context Pack, Implementation Brief |

Domänen sind fachliche Zuständigkeiten, **keine Pflichtordner**. Ordner werden nur bei konkreten Arbeitsergebnissen erzeugt.

## 7. Verzeichnisarchitektur

```text
branding/
├── AGENT.md
├── .branding/
│   ├── BERATUNG.md
│   ├── RULES.md
│   ├── ARCHITECTURE.md
│   ├── STRUKTUR.md
│   ├── METHODEN.md
│   ├── DATENMODELL.md
│   ├── BRAND-GOVERNANCE.md
│   ├── KONTEXT.md
│   ├── QUALITAET.md
│   ├── INTEGRATION.md
│   ├── STATE.md
│   ├── LOG.md
│   ├── HISTORY.md
│   ├── TESTFAELLE.md
│   ├── methoden/
│   ├── schemas/
│   ├── tools/
│   └── beispiele/
├── input/
└── archiv/
```

Beispiel für erst später entstandene Ergebnisse: `branding/strategie/positionierung.md`, `branding/identitaet/markenplattform.md`, `branding/guidelines/brand-guidelines.md`, `branding/portfolio/markenarchitektur.md`, `branding/measurement/brand-health.md`. `.branding/` ist die interne Wissens- und Regelbibliothek, nicht der Speicher für operative Markendokumente oder vertrauliche Kundenbestände.

## 8. Zustands- und Artefaktmodell

### 8.1 Brand Identity Scope

Jede Marke erhält eine stabile `brand_id`; `organization_id` und `parent_brand_id` sind optional. Ein Studio kann mehrere Marken unabhängig verwalten, ohne dass ein Kundenverwaltungssystem erforderlich wäre. Markenbeziehungen werden ausdrücklich modelliert, statt aus einem gemeinsamen Verzeichnis geraten.

### 8.2 Brand Claim und Decision

Zu trennen sind:

- **Fakt:** externe oder interne prüfbare Aussage, vorzugsweise mit Business-DNA-Referenz.
- **Strategische Entscheidung:** Beschlossene Markenrichtung, benötigt verantwortliche Autorisierung.
- **Strategieentwurf:** diskutierbarer Vorschlag, noch keine verbindliche Guideline.
- **Brand Promise:** Sollversprechen; die entsprechenden Tatsachenbehauptungen benötigen Nachweise.
- **Brand Expression:** zulässige sprachliche oder gestalterische Ausprägung.
- **Observed Association:** empirisch erhobene Wahrnehmung inklusive Messmethode und Unsicherheit.

Entscheidungen dürfen nicht durch einen Modell-Output auf `approved` wechseln. `approved_by` und `approved_at` sind nur bei nachgewiesener Freigabe zu befüllen; die Datei selbst ist keine Authentifizierung. Ein Approved-Status ist kein Rechtsgutachten.

### 8.3 Änderbarkeit

Jedes kanonische Artefakt hat eine `id`, `version`, `status`, `updated_at`, `owner_scope`, `dependencies`, `source_refs` und eine Revisionserklärung. Frühere gültige Fassungen bleiben rekonstruierbar. Freigegebene Designrichtlinien werden nicht von Kampagnenentwürfen stillschweigend überschrieben.

## 9. Statusmodell

**Artefakt-Lifecycle:** `draft` → `in_review` → `approved` → `superseded` / `retired`, alternativ `rejected`. Das ist eine fachliche Dokumentstatusmaschine.  
**Evidenzstatus:** Fakten nutzen Business-DNA-kompatible Zustände wie `verified`, `declared`, `planned`, `hypothesis`, `disputed`.  
**Implementation-Status:** `not_started`, `in_progress`, `implemented`, `partially_implemented`, `not_applicable`.  
**Measurement-Status:** `not_measured`, `baseline`, `observed`, `inconclusive`.

Eine strategisch genehmigte Positionierung bedeutet weder, dass sie überall umgesetzt wurde, noch dass Nutzer sie tatsächlich wahrnehmen. Dafür sind getrennte Nachweise nötig.

## 10. Ausführungsprozess

**Intent → gezielte Quellenlektüre → Diagnose → Optionen → begründete Empfehlung → Entwurf → fachlicher Review → menschliche Richtungsentscheidung bei Bedarf → kanonische Artefakte → gezielter Handoff → Beobachtung und Weiterentwicklung.**

Der Ablauf ist dynamisch, nicht verpflichtend linear. Bei kleinen Aufgaben reichen Teilabschnitte. Ein Submodul wird niemals nur zur Erfüllung einer vorgegebenen Stufenfolge aktiviert.

## 11. Business-DNA-Integration

Falls `../business-dna/` vorhanden ist, kann Branding über vorhandene Context Packs oder zweckbezogene Referenzen auf Unternehmensfakten zugreifen. Übernommene Aussagen behalten `claim_id`, `status`, `source_refs`, `updated_at`, `visibility` und Einschränkungen. Business-DNA-Claims sind **keine Freigabe** zur Werbeverwendung, auch bei Status `verified`.

Die Schnittstelle respektiert die bestehende Business-DNA-v0.1-Struktur (`context-request.schema.json`, `context-pack.schema.json`). Sie erfindet keine API. Fehlt Business-DNA, werden die notwendigen Unternehmensfakten direkt aus verfügbaren Unterlagen bezogen, als unsicher markiert und bei Bedarf gezielt überprüft.

**Rückrichtung:** Bei gefundenen Abweichungen schlägt Branding eine Business-DNA-Änderung vor; es überschreibt das Unternehmenswissen nicht.

## 12. Branding als kanonische Marke

Der Branding-Bereich ist die bevorzugte Quelle für **freigegebene Markenentscheidungen**: gewählte Positionierung, Markenversprechen, Tonalität, Namensschreibweisen, Markenarchitektur, Gestaltungsleitlinien. Der Fachbereich bleibt ohne Suite nutzbar. Andere Module dürfen abweichende, zielgruppengerechte Varianten innerhalb definierter Toleranzen entwickeln; wesentliche Richtungsänderungen gehen zurück an Branding.

Für jedes exportierte Markenprofil muss erkenntlich sein, ob es `draft` oder `approved` ist. Nicht freigegebene Vorschläge dürfen extern nicht als Corporate Identity ausgegeben werden.

## 13. Branding ↔ Creative

**Branding** liefert `visual-direction-brief` und freigegebene Brand Guidelines. **Creative** entwickelt Logos, Gestaltungssysteme, Medien und konkrete Designanwendungen. Branding überprüft deren Übereinstimmung mit Strategie und Richtlinien; Creative überprüft gestalterische und technische Qualität. Ein Branding-Review ersetzt keinen Print-Preflight. Ändert sich eine Designregel, muss der Änderungsauftrag die betroffenen Assets/Publikationen aufführen.

## 14. Branding ↔ Marketing, PR, Social, Website, Advertising, noCRM

- `marketing/`: Zielgruppenkontext, langfristige Positionierung und Markenprioritäten; keine automatische Übernahme von Kanalbudgets.
- `pr/`: Markenstory und freigegebene Unternehmensnarrative, aber getrennte Prüfung des Nachrichtenwerts.
- `social-media/`: kanaladaptierte Markenstimme, Beispiele, verbotene Bedeutungsverschiebungen; keine bloße Text-Duplikation.
- `website/`: Informationsarchitektur, Texttonalität, Design-Tokens; der Website-Spezialist verantwortet Umsetzung und technische Qualität.
- `advertising/`: freigegebene Claims und kreative Leitplanken; Leistungs- und Rechtsprüfung für konkrete Anzeigen bleibt nötig.
- `noCRM/`: individuelle Tonalität und Beziehungsnähe ohne Verlust der Markenidentität; kein Import privater Kontaktverläufe in die Branding-Bibliothek.
- `analytics/`: Forschungsbriefings und Brand-Health-Evidenz, keine erfundenen Wirkungsnachweise.

## 15. Öffentliche und interne Markeninformationen

Interne Arbeitsannahmen, vertrauliche Strategien und öffentlich verwendbare Markeninformationen müssen unterschieden werden. Ein Context Pack ist zweckgebunden, selektiv und mit `audience`, `purpose`, `visibility`, `excluded_count`, `limitations` dokumentiert. Öffentliche Brand Profiles entstehen bewusst, nicht durch generellen Export von `.branding/`.

## 16. Wiederverwendbare Methods & Tools

Methoden werden als unabhängige Markdown-Anleitungen unter `.branding/methoden/<bereich>/<methode>.md` gepflegt. Ein Katalog listet Einsatzsignale und sinnvolle Abhängigkeiten. Die `AGENT.md` verweist auf diesen Katalog; die KI lädt nur die zur Aufgabe passenden Methoden. Ein System kann weitere Methoden hinzufügen, ohne die Architektur zu verändern.

Hilfswerkzeuge werden **ausschließlich optional** gebraucht. Ein paar JSON-Schemas und Python-Standardbibliothek-Tools liefern formale Lints und Context-Exporte, ersetzen aber keine Marktforschung oder Freigabe.

## 17. Modell der Markenarchitektur

Unterstützte Beziehungen: `branded_house`, `house_of_brands`, `endorsed`, `sub_brand`, `product_brand`, `co_brand`, `descriptive_offer`; kein Modell ist automatisch vorzuziehen. Eine Beziehung wird pro Markenpaar ausdrücklich beschrieben. `parent_brand_id` oder Zuordnung zu Portfolioeinträgen ist kein Beweis für rechtliche Eigentümerschaft.

Ein Markenportfolio kann Produktfamilien, Märkte, Sprachvarianten und Markeninhaber abbilden. Schreibweisen werden kanonisch festgehalten; Lokalisierungen dürfen nicht stillschweigend neue rechtliche Marken erzeugen.

## 18. Strategie und Differenzierung

Positionierungen werden entlang von Zielgruppe, Situation/Bedürfnis, Bezugsrahmen, relevantem Nutzen, Unterscheidbarkeit, Glaubwürdigkeit und Belegen beurteilt. Ein USP kann nur dann als exklusiv behauptet werden, wenn diese Exklusivität belegt ist. Andernfalls ist von differenzierendem Nutzen oder einer Positionierungshypothese zu sprechen.

Alternativen sollen gegeneinander bewertet werden: Relevanz, Glaubwürdigkeit, Distinktheit, Umsetzbarkeit, Anschlussfähigkeit und mögliche Fehlinterpretationen. Bewertungen werden begründet; eine Punkteskala ohne definierte Anker ist nicht ausreichend.

## 19. Verbale Markenidentität

Naming, Claim, Corporate Language, Tone of Voice, Story, Terminologie und deutsch-/englischsprachige Varianten bilden einen eigenen Fachbereich. Der Spezialist unterscheidet **Markenstimme** (stabil) und **situativen Ton** (kontextabhängig). Übersetzungen erfolgen sinngemäß und kulturell angemessen, nicht wortwörtlich. Vor Verwendung neuer Namen erfolgt eine gesonderte Marken-, Domain- und Sprachprüfung durch dafür geeignete Verfahren; eine bloße Internetrecherche ist keine markenrechtliche Freigabe.

## 20. Visuelle Markenführung

Branding definiert visuelle Prinzipien sowie die Anforderungen an Zeichen, Wort-/Bildmarken, Farben, Typografie, Bildsprache, Layoutlogik, Bewegung und digitale Zugänglichkeit. Die Werte dürfen nur mit ausreichenden Rechten und Freigaben in ein verbindliches Designsystem aufgenommen werden. Creative erzeugt die tatsächlichen Assets. Barrierefreiheit und technische Produktion bleiben gesonderte Qualitätsdimensionen.

## 21. Brand Experience

Die Marke soll in Verhalten und Service erlebbar sein. Der Spezialist untersucht kritische Kontaktpunkte, erwartetes und tatsächliches Verhalten sowie Lücken zwischen Markenversprechen und Erlebnissen. Unternehmensfakten werden nicht aus Marketingwünschen abgeleitet; bei strukturellen Widersprüchen informiert Branding Business-DNA und die fachlich zuständigen Bereiche.

## 22. Brand Governance und Freigaben

Ein freigegebenes Markendokument muss `artifact_id`, `version`, `approved_by`, `approved_at`, Geltungsbereich und gegebenenfalls Quellen/Prüfnachweise enthalten. Brand-Reviews beziehen sich auf **konkrete Versionen**. Änderungen an freigegebenen Vorgaben führen zu einer neuen Version und zu dokumentierten Auswirkungen; alte Entscheidungen dürfen nicht gelöscht oder rückwirkend verändert werden.

Die Suite kann ihre vorhandenen Approval-Schemas und `.suite/GOVERNANCE.md` ergänzend nutzen. Das Modul erzeugt keine eigene Rechts- oder Sicherheitsarchitektur und simuliert keine Autorisierung. Eine Harness-Integration muss gegebenenfalls externe Aktionssperren technisch durchsetzen.

## 23. Messbarkeit und Marktforschung

Empfohlene Dimensionen: unaided/aided Awareness, Markenassoziationen, Vertrautheit, Consideration, Präferenz, Vertrauen, Distinctive Assets, Brand Experience und gegebenenfalls Brand Equity. Kennzahlen dürfen nicht mit Wahrnehmung gleichgesetzt werden: Impressions, Reichweite und Likes sind kein belastbarer direkter Ersatz für Markenbekanntheit. Stichproben, Definitionen und Unsicherheit müssen dokumentiert werden.

Die konzeptionelle Markenbewertung kann sich an den Prinzipien von **ISO 20671-1:2021** orientieren. **ISO 10668:2010** behandelt hingegen die monetäre Markenbewertung, nicht allgemeine Awareness-Messung. Diese Standards dürfen nicht mit tatsächlicher Konformitätszertifizierung verwechselt werden; die normative Volltextanwendung setzt ggf. Lizenzen voraus.

## 24. Rechtliche und ethische Grenzen

Erforderlich sind zweckbezogene Prüfungen auf Marken- und Kennzeichenrecht, Urheber- und Nutzungsrechte, Rechte an Schriften, Stockmedien, KI-generierten Assets, Werbung, irreführende Aussagen, Persönlichkeitsrechte und kulturelle Sensibilität. Die Markenstrategie darf keine Markenregistrierung oder umfassende Rechtsfreiheit behaupten, nur weil ein Name frei erscheint. Bei Schutzrechtsanmeldungen und strittigen Fällen erfolgt fachjuristische Prüfung.

Markenschutz ist territoriumsbezogen; für die EU bestehen nationale und unionsweite Schutzwege. Verbindliche Aussagen müssen auf den jeweils gültigen Rechtsstand gestützt werden. Die Fachbibliothek unterstützt Vorprüfungen, nicht anwaltliche Beratung.

## 25. Qualitätssicherung

Unabhängige Dimensionen: `strategic_fit`, `evidence_fit`, `distinctiveness`, `consistency`, `comprehensibility`, `accessibility`, `implementation_feasibility`, `legal_review_status`, `perception_evidence`. Ein Entwurf darf auch bei formaler Vollständigkeit fachlich verworfen werden. Prüfberichte benennen Schweregrad, Fundstelle, Empfehlung und verantwortlichen Fachbereich.

**Kritische Gates:** Unbelegbare Leistungs- oder Exklusivitätsbehauptung; Verwechslung von Konzept und freigegebener Markenregel; rechtsunklarer Name/Asset; nicht auflösbarer Widerspruch zu bestätigten Unternehmensfakten. Fehlende Daten werden offen markiert, nicht mit synthetischer Sicherheit überdeckt.

## 26. Betrieb, Log, History und Archiv

- `.branding/STATE.md`: aktueller Stand, relevante Artefaktpfade, offene Prüfungen und nächster fachlicher Schritt.
- `.branding/LOG.md`: tatsächliche Änderungen, Prüfungen, Exporte und Fehler mit Zeitbezug; keine erfundenen Aktivitäten.
- `.branding/HISTORY.md`: bestätigte strategische Entscheidungen, Richtungswechsel und Begründungen.
- `input/`: temporärer Materialeingang; nach nachweislicher Übernahme werden Originale unverändert archiviert.
- `archiv/`: importierte Ausgangsmaterialien, veröffentlichte bzw. freigegebene Versionen und zurückgezogene Artefakte.

Löschung, Archivierung und vertrauliche Datenverarbeitung richten sich nach der tatsächlichen Organisationspolitik. Das Modul liefert keine Pflichtdauer für Datenaufbewahrung.

## 27. Technische Verträge und Artefakte

Die Version v0.1 enthält JSON-Schemas für `brand-profile`, `brand-decision`, `brand-context-request`, `brand-context-pack`, `brand-review` und `brand-event`. Schemas prüfen Form, nicht Markenqualität. Die Referenzwerkzeuge funktionieren offline mit Python 3.10+ ohne zusätzliche Laufzeitabhängigkeiten; optionale JSON-Schema-Validierung kann bei vorhandenem `jsonschema` genutzt werden.

Der Context-Export beachtet Status und Visibility. Nicht freigegebene Brand Decisions werden nicht als autoritative Brand Guidelines exportiert. Empfänger ohne explizite Berechtigung erhalten keine eingeschränkten Datensätze. Eine `public`-Kennzeichnung ist fachlich, keine technische Authentifizierung.

## 28. Akzeptanzkriterien

1. Nur die `AGENT.md` wird gelesen → exakt eine natürliche Startfrage.
2. Konkreter Markenauftrag → begründete Erstberatung, kein 20-Fragen-Onboarding.
3. Business-DNA fehlt → funktionsfähiger, ausdrücklich eingeschränkter Entwurf.
4. Business-DNA liegt vor → differenzierter Umgang mit verified/declared/planned.
5. Ein `planned` Produktmerkmal erscheint nicht als erwiesener USP.
6. Freigegebene Guideline darf ohne neue Entscheidung nicht überschrieben werden.
7. Creative-Handoff enthält Version, Ziele, erlaubte Varianz und offene Risiken.
8. Importierte öffentliche Fakten werden nicht automatisch als genehmigte Aussagen behandelt.
9. Mehrere Marken und Markenbeziehungen werden getrennt verwaltet.
10. Export beachtet Visibility und Freigabestatus.
11. Vorherige Versionen sind nachvollziehbar und können rekonstruiert werden.
12. Medienwirkung wird nicht aus Social-Reichweite allein behauptet.
13. Brand Reviews binden sich an konkrete Artefaktversionen.
14. Rechtliche Rechercheergebnisse werden nicht als endgültige Schutzrechtsfreigabe ausgegeben.
15. Die acht bisherigen Fachbereiche bleiben ohne Branding funktionsfähig.
16. Eine gestartete, aber nicht beendete Aufgabe kann aus STATE und Artefakten wiederaufgenommen werden.
17. Daten-Schemas, referenzierte Methoden und ZIP-Datei sind formal konsistent.
18. Kein Test suggeriert reale Veröffentlichung, Markenregistrierung oder durchgesetzte externe Freigaben.

## 29. Implementierungsphasen

**Phase 0 – Strukturelle Basis (v0.1):** AGENT, Methoden, Governance-Dokumente, Beispiel, Schemas, Offline-Lints, Tests.  
**Phase 1 – Markenpilot:** TOPACA anhand echter Unterlagen; Positionierung, Brand Platform, Tone of Voice und Visual Brief ausarbeiten; menschliche fachliche Review.  
**Phase 2 – Integration:** Business-DNA-Context, Marketing-/Creative-Brief, selektive Handoffs und Suite-Approval-Referenzen testen.  
**Phase 3 – Wirkung:** dokumentierte Brand-Health-Baseline und wiederholbare Evaluation mit Analytics, ohne direkte Gleichsetzung von Reichweite und Bekanntheit.  
**Phase 4 – Erweiterung:** mehrere Marken, Markenportfolio, Lokalisierung und zeitliche Markenentwicklung.

## 30. Risiken und offene Fragen

- Wie differenziert die Suite Markenrechte und Urheberrechte über Ländergrenzen hinweg, ohne eine rechtliche Prüfung vorzutäuschen?
- Welches Mindestmaß an Evidenz genügt vor externer Verwendung einer Nutzenaussage?
- Wann darf eine Markenvariante kanalbedingt vom Standard abweichen?
- Wie werden nachträgliche Business-DNA-Korrekturen zu einem Änderungsbedarf in Branding?
- Wie verhindert man, dass kreative Vielfalt durch zu enge Guidelines erstickt wird?
- Welche Review-Tiefe ist für EPUs sinnvoll gegenüber internationalen Markenportfolios?
- Wie lässt sich Markenbekanntheit bei sehr kleiner Stichprobe ehrlich einschätzen?

## 31. Referenzen und normative Einordnung

- ISO: [ISO 20671-1:2021 – Brand evaluation: Principles and fundamentals](https://www.iso.org/standard/81739.html) (Rahmen für qualitative und quantitative Markenbewertung).
- ISO: [ISO 10668:2010 – Requirements for monetary brand valuation](https://www.iso.org/standard/46032.html) (monetäre Markenbewertung, andere Zielsetzung).
- Europäische Kommission: [Trade mark protection in the EU](https://single-market-economy.ec.europa.eu/industry/strategy/intellectual-property/trade-mark-protection-eu_en) (Markenschutzwege und Begriffe).
- Europäische Union: [Trade marks – Your Europe](https://europa.eu/youreurope/business/growing/protecting-intellectual-property/trade-marks/index_de.htm) (territorialer und unionsweiter Schutz).
- Vorläufer: `Business-DNA – Conceptual Architecture & Organizational Knowledge Specification v0.1` (interne Schnittstelle; kein externer Standard).

Die Spezifikation referenziert öffentlich beschriebene Ziele von Standards, reproduziert keine lizenzgeschützten Normtexte und behauptet keine ISO-Zertifizierung.
