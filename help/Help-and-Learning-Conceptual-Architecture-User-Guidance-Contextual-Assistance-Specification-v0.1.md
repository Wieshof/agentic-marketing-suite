# Help & Learning – Conceptual Architecture, User Guidance & Contextual Assistance Specification v0.1

**Status:** Architektur- und Referenzspezifikation · **Datum:** 27. Oktober 2026  
**Zweck:** Eigenständig nutzbares, optional in die Agentic Marketing Suite integrierbares Hilfesystem für Menschen ohne Marketing- oder IT-Fachkenntnisse  
**Normative Sprache:** *MUSS*, *SOLL*, *DARF* beziehen sich auf den hier definierten Fachbereich und nicht automatisch auf bereits nachgewiesene Eigenschaften eines Harnesses.

## 1. Zusammenfassung

`help/` ist ein beratender, didaktischer und erklärender KI-Fachbereich. Er erklärt die Agentic Marketing Suite, hilft Menschen beim Einstieg und Verstehen von Ergebnissen, übersetzt Fachbegriffe, prüft die behauptete Verfügbarkeit technischer Funktionen und unterstützt bei konkreten Bedienungsproblemen. Er verfügt **über keinen eigenen Agenten-Harness, keine Workflow-Engine, keinen zentralen Aufgabenrouter und keine Ausführungsbefugnis für andere Fachmodule**.

Die wesentliche Leistung ist nicht eine Sammlung häufiger Fragen, sondern **kontextbezogene Hilfe zur tatsächlichen Arbeit**. Eine Person soll ein Problem in natürlicher Sprache schildern können und sofort eine verständliche Antwort oder eine passende erste Arbeitsanweisung erhalten. Dokumentation und didaktische Hilfen werden nur insoweit konsultiert, wie sie die konkrete Frage beantworten.

## 2. Ausgangslage und Abgrenzung

Die öffentliche Suite-README beschrieb am 27.10.2026 den integrierten Stand v0.2.1 mit neun Modulen inklusive E-Commerce, 477 Methodendateien und einer gemeinsamen `.suite/`-Ebene. Weitere separat entwickelte Bereiche wie Business-DNA und Branding sind keine vorausgesetzten, stets installierten Module. Die Beschreibung ist ein Versionsschnappschuss; tatsächliche Installation hat Vorrang. Referenz: https://github.com/markus-ertel/agentic-marketing-suite.

Das System ist bewusst dateibasiert und ohne Pflichtdatenbank. Daraus ergeben sich Chancen (Offenheit, Portabilität, Nachvollziehbarkeit) und Einstiegshürden (versteckte Verzeichnisse, mehrere Fach-`AGENT.md`, Methodendichte, ungleiche technische Reife von Integrationen). Help beseitigt die Hürden **ohne** die Suite in ein Menü-getriebenes Softwareprodukt umzubauen.

## 3. Ziele

1. Natürlicher Gesprächsstart mit genau einer kurzen offenen Frage, wenn kein Auftrag vorliegt.
2. Sofort nützliche Antworten bei vorhandener konkreter Frage.
3. Beratung zu Möglichkeiten, Grenzen, Stärken, Schwächen, Einstieg und Arbeitspraxis.
4. Erklärung der bestehenden Fachbereiche, ohne selbst deren Fachaufgaben zu übernehmen.
5. Unterstützung von Fehlerdiagnose und realitätsnaher Funktionsklärung.
6. Verständliche Deutung vorhandener Dateien und Arbeitsergebnisse mit gezieltem Dokumentkontext.
7. Transparenz darüber, was nur dokumentiert, implementiert, konfiguriert, getestet oder unbekannt ist.
8. Unabhängige Nutzbarkeit außerhalb der Suite, optionale Integration in Dashboard und beliebige geeignete Harnesses.
9. Lernförderung aus tatsächlicher Aufgabe; keine erzwungenen Kurse oder Onboarding-Bögen.

## 4. Nicht-Ziele

Keine eigene KI-Runtime, kein LLM-Provider-Layer, kein Task-Broker, keine automatische Erstellung von Werbekampagnen, keine rechtlich verbindliche Beratung, kein E-Mail-/Messenger-Gateway, kein unabhängiges Publishing, keine Accountverwaltung, keine neue Sicherheitsarchitektur, keine automatische Freigabestelle und keine parallele Datenhaltung der gesamten Suite. Nicht Ziel ist die Ersetzung der technischen Primärdokumentation durch unbestätigte Zusammenfassungen.

## 5. Leitprinzipien

**Menschenfreundlich:** Alltagssprache, respektvolle Erklärungen, kurze Erstinformation, Details auf Wunsch.  
**Auftragsorientiert:** Fragen werden beantwortet; nur im echten Blockadefall wird nachgefragt.  
**Faktenorientiert:** Aussagen über Funktionen haben eine überprüfbare Quelle und einen klaren Geltungsbereich.  
**Didaktisch minimal:** Erkläre gerade so viel wie nötig, um entscheiden oder weiterarbeiten zu können.  
**Offen und modular:** Keine Pflicht zur Installation anderer Module, kein Lock-in.  
**Kontrollierbare Übergaben:** Vorschläge für andere Spezialisten sind zunächst nur Texte; tatsächliche Weiterleitung benötigt einen vorhandenen Runner.  
**Keine Handlungssimulation:** Dokumentieren, Vorbereiten, Freigeben und Ausführen sind eigenständige Zustände.

## 6. Nutzergruppen und typische Anliegen

- **Einsteiger ohne Fachwissen:** „Ich habe einen kleinen Betrieb – wo fange ich an?“
- **Fachfremde Unternehmensleitung:** „Wie beurteile ich das vorgeschlagene Marketingkonzept?“
- **Marketing- und Kreativfachleute:** „Welcher Spezialist ist für Positionierung, Claim oder Kampagne zuständig?“
- **Technische Anwender:** „Wo liegt der Methodenindex? Wie überprüfe ich das installierte Modul?“
- **Betreiber und Beitragende:** „Wie ergänze ich die Help-Bibliothek ohne doppelte Wahrheiten?“
- **Nutzer mit angezeigtem Dokument:** „Was bedeutet dieser Absatz in meiner Datei?“

Alle Gruppen nutzen denselben Fachspezialisten. Keine verpflichtenden Nutzerprofile und keine Einstiegsformulare.

## 7. Fachliche Verantwortung

Help MUSS erklären, anleiten und einordnen. Help DARF eine Maßnahme problematisieren oder von ungeeigneten Aufgaben abraten. Help MUSS bei echter Marketing-, PR-, Brand-, Design- oder Analytics-Produktion den geeigneten tatsächlich verfügbaren Spezialisten empfehlen. Das bloße Verfassen einer kopierbaren Arbeitsanweisung stellt **keine ausgeführte Übergabe** dar. Wenn die Suite keinen externen Runner besitzt, endet die Help-Leistung bei Erklärung und Vorschlag.

## 8. Gesprächsverhalten und Sofortstart

**Nur Initialisierung:** Antwort exakt: „Wobei kann ich Ihnen mit der Agentic Marketing Suite helfen?“  
**Mit Auftrag:** Keine Begrüßungsroutine, sondern konkrete Antwort bzw. Vorschlag.  
**Mit unvollständigen Informationen:** Plausible Annahmen als solche kennzeichnen und trotz Lücken beginnen.  
**Mit risikoreicher Unklarheit:** Eine gebündelte Rückfrage stellen, wenn sonst eine falsche oder schädliche Empfehlung entstünde.  
**Bei Fortsetzung:** Relevanten Zustand prüfen; nie dieselbe Frage wiederholen, wenn die Antwort vorhanden ist.

Die Standardantwort für Einsteiger: kurze Einordnung, ein priorisierter Schritt, kopierbarer Beispielauftrag (wenn hilfreich), ggf. ein klarer Grenzenhinweis. Mehrstufige Anleitungen nur auf ausdrücklichen Wunsch oder wenn die Aufgabe sie verlangt.

## 9. Lernmodell: Lernen beim Arbeiten

Die Hilfe verwendet *situated learning* als Designprinzip: reale Aufgabe, erste Lösung, nachgelagerte Erklärung, Verbesserung. Sie unterrichtet nicht zuerst im Marketing-Vokabular. Eine Person, die eine Pressemitteilung benötigt, soll nicht vorab die Grundlagen der PR-Geschichte lernen. Der Spezialist kann nach der Ausarbeitung erläutern, warum die PR-Empfehlung sinnvoll war und welche Nachrichtenwertkriterien angewandt wurden.

Lernmodi ergeben sich aus der Frage, ohne Formular: `short` (kurz), `normal` (Standard), `detailed` (ausführlich), `technical` (Reproduzierbarkeit und Pfade). Die Angabe im Kontextvertrag ist optional.

## 10. Fachgebiete und Wissensorganisation

Die Help-Fachbibliothek ist nach Aufgaben gegliedert: Orientierung, Einstieg, Fachbereichswahl, Arbeitsergebnisse, Technik, Verantwortung/Rechte, Praxislernen und eigene Qualität. Jede Methode beschreibt Zweck, Zeitpunkt, Ablauf, Ergebnis und Qualitätskriterium. Der Spezialist MUSS bei einer Frage **nur die benötigten** Anleitungen lesen. Guides sind direkt für Menschen nutzbare Texte, Methoden steuern den Fachspezialisten.

## 11. Verzeichnis- und Ablagemodell

```text
help/
├── AGENT.md
├── .help/
│   ├── BERATUNG.md · RULES.md · ARCHITECTURE.md
│   ├── STRUKTUR.md · WISSENSQUELLEN.md
│   ├── METHODEN.md · ANLEITUNGEN.md
│   ├── KONTEXT.md · QUALITAET.md · INTEGRATION.md
│   ├── STATE.md · LOG.md · HISTORY.md · TESTFAELLE.md
│   ├── methoden/ · guides/ · examples/
│   ├── schemas/ · tools/ · tests/
├── input/
└── archiv/
```

Interne Bibliothek und Arbeitszustand liegen in `.help/`, nutzerspezifische Arbeitsergebnisse außerhalb und nur bei Bedarf. Temporäre Eingaben werden erst nach nachweislich erfolgreicher Übernahme archiviert beziehungsweise bereinigt. Der Hilfe-Bereich spiegelt keine fremden Kunden-, Marken- oder Kontaktdaten.

## 12. Integration in die bestehende Suite

Optionale Installation als `help/` neben Fachmodulen. Die Suite funktioniert ohne Help und Help auch isoliert. Der vorhandene Root-`AGENT.md` kann auf Help verweisen, muss aber nicht umgeschrieben werden. Zur Einordnung optional vorhandener Module verweist Help auf den tatsächlichen Dateibaum und danach die zugehörige Dokumentation. Keine zentrale Steuerung anderer Spezialisten durch Help.

## 13. Kontextbezogene Hilfe

Ein Dashboard oder CLI kann eine Frage, einen relativen Dokumentpfad und optional einen Abschnittsanker mitsenden. Die vorgeschlagene `help-context.schema.json` ist **ein optionaler offener Datensatzvertrag**, keine Pflicht zur Einführung einer Runtime. Help fordert gezielt die tatsächlich nötige Textpassage an, sofern Zugriffsrecht und Werkzeug vorhanden sind. Andernfalls bietet es eine generische Erklärung und benennt offen die fehlende Dokumenteinsicht.

**Beispiel:** Geöffnet ist `marketing/strategie/positionierung.md`; Frage: „Was bedeutet diese Positionierung?“. Help erläutert nur den wirklich gelesenen Absatz; wenn die Datei fehlt, erklärt es den allgemeinen Begriff und fragt ggf. nach der betreffenden Passage.

## 14. Quellenrangfolge und Wahrheit

1. Tatsächlich beobachtete Dateien, aktuelle Konfiguration, vorhandene Tests.
2. Gültige lokale README, CHANGELOG, AGENT und Suite-Verträge.
3. Fachmodule mit ihren konkreten Methoden und Funktionsbeschreibungen.
4. Aktuelle externe Dokumentation mit nachgewiesenem Abrufdatum.
5. Allgemeines Fachwissen – ausdrücklich ohne Behauptung über aktive Integrationen.

Konflikte werden nicht wegerklärt. Ein 'vorhandenes API-Profil' ist kein erfolgreicher Versand. Aktuelle Beobachtung eines Tests ist keine pauschale Garantie. Bei fehlenden Quellen: `unknown`.

## 15. Reifegradvokabular für Softwarefunktionen

`documented` – dokumentierter Anspruch.  
`implemented` – konkretes Skript/Adapter vorhanden.  
`configured` – lokale Einstellungen erkennbar.  
`tested` – überprüfbarer Test erfolgreich im angegebenen Umfang.  
`unavailable` – Voraussetzung fehlt oder Test schlägt fehl.  
`unknown` – aktuelle Verfügbarkeit nicht bestimmt.  

Dies sind beschreibende Statuswerte und **keine automatische Vertrauenskette**: Ein konfigurierter Adapter kann offline sein; ein früher erfolgreicher Test kann veraltet sein. Help MUSS zu jeder Verfügbarkeitsaussage den tatsächlichen Geltungsbereich benennen.

## 16. Unterschied zwischen Dokumentation und Ausführung

Das Laden einer `AGENT.md` ist noch kein ausgeführter Auftrag. Eine Markdown-Methode ist noch kein bereitgestelltes Tool. Ein geplanter E-Mail-Adapter ist keine Postfachverbindung. Ein freigegebener Anzeigenentwurf ist noch keine Werbebuchung. Die Hilfe MUSS diese Abstufungen erklären und darf ohne Bestätigung keine Aktion als erfolgreich markieren.

## 17. Modulwahl und optionale Übergaben

Help ordnet Anliegen zu den tatsächlich vorhandenen Fachbereichen zu. Es kann einen kopierbaren Auftrag liefern, inklusive Ziel, verfügbarem Kontext, Ergebniswunsch und Einschränkungen. Ein expliziter Adapter des bestehenden Harness kann diesen weitergeben; Help enthält keine eigene Agenten-Orchestrierung oder Nachrichtenwarteschlange. `branding/` und `business-dna/` sind nur dann als installierte Modulziele zu behandeln, wenn ihre Dateien verfügbar sind.

## 18. Recht, Verantwortung, Datenschutz und Freigaben

Help erklärt Grundprinzipien – DSGVO, Kommunikationszulässigkeit, Urheber-/Nutzungsrechte, Impressum, KI-Transparenz – ohne verbindliche Rechtsberatung. Informationen aus noCRM oder anderen vertraulichen Bereichen dürfen nicht automatisch in Hilfetexte übertragen werden. Für externe Aktionen gelten die vorhandenen Suite-Regeln und das tatsächliche Harness. Die Hilfe erteilt und umgeht keine Freigaben.

## 19. Grenzen der aktuellen Dashboard-Integration

Ein optionales Dashboard zeigt Fachbereiche und Dokumente an und reicht Nachrichten an den gewählten Harness weiter. Help kann diese Darstellung erläutern, definiert aber keinen neuen UI-Server, Port, Session-Manager oder Agentenstatus-Emitter. Eine angebliche „aktive Session“ ist nur korrekt, wenn der vorhandene Adapter sie beobachtet. Help-Dokumente sind auch ohne Dashboard lesbar.

## 20. Datenverträge

- `help-context.schema.json`: minimale Anfrage mit `question`, optional `document_ref`, `preferred_depth`, `ui_origin`.
- `help-answer.schema.json`: optionale Antwortmetadaten mit `basis_status`, `source_refs`, `limitations`, optional vorgeschlagenem Modul und kopierbarem Auftrag. Das Feld `execution_claimed` ist explizit `false`.

Verträge beschreiben Interoperabilität, keine Aufrufverpflichtung. In einer einfachen KI-Chatumgebung genügt freie Sprache. Die lokale Referenzimplementierung erfordert keine Netzwerkdienste.

## 21. Qualitätssicherung

Qualitätsdimensionen: Verständlichkeit, Wahrheitsgehalt, Quellenqualität, Angemessenheit für Kenntnisstand, konkreter Nutzen, keine unnötigen Fragen, ehrliche Funktionsgrenzen, keine Handlungssimulation. Der Testkatalog enthält sowohl Fachverhaltensfälle als auch technische Dateikontrollen. Menschliche Prüfung bleibt für Verständlichkeit erforderlich; ein bestandener Markdown-Lint ist kein Nachweis guter Hilfe.

## 22. Zustände, Log und Historie

`STATE.md` dokumentiert nur laufenden relevanten Arbeitsstand. `LOG.md` beschreibt tatsächlich ausgeführte Operationen und Tests. `HISTORY.md` hält langlebige Entscheidungen zum Hilfe-Bereich fest. Für den Gesamtprozess ist weiterhin `.suite/` verantwortlich. Help führt kein heimliches personenbezogenes Chatarchiv. Log-Einträge werden nicht aus fiktiven Beispielen erzeugt.

## 23. Technische Hilfsmittel

Das enthaltene Offline-Werkzeug `scan_workspace.py` kann Ordnerinventar und methodische Dokumentation erkennen. Es benötigt nur die Python-Standardbibliothek, liest keine Kontaktinhalte und führt keine externen Aktionen aus. Der Bericht unterscheidet **Dateistrukturbeobachtung** von realer Funktionsprüfung. Das Testprogramm `validate_help.py` prüft Bibliotheksstruktur, Links und Beispieldaten gegen eine minimale Referenzvalidierung; es ist kein vollständiger JSON-Schema-Validator und kein Harness-Test.

## 24. Erweiterbarkeit und Internationalisierung

Neue Methoden werden im Methodenindex registriert und folgen der festen Dokumentstruktur. Menschenorientierte Guides sind eigenständige, verständliche Texte. Die erste Version ist deutschsprachig; weitere Sprachen können pro Guide ergänzt werden, ohne die Fachmodule zu duplizieren. Der Spezialist darf Englisch erklären, muss aber nicht behaupten, dass vollständig übersetzte Dokumente vorliegen.

## 25. Barrierearme Hilfe

Strukturierte Überschriften, lesbare Sprache, klare Tastatur- und Screenreader-kompatible Präsentation bei Darstellung im Dashboard, keine farbabhängigen Aussagen oder informationslosen Icons. Schritt-für-Schritt-Anleitungen verwenden eindeutige Bezeichnungen und müssen ohne visuelle Oberfläche nutzbar sein. Das Dashboard verantwortet die tatsächliche technische Zugänglichkeit seiner Oberfläche.

## 26. Erfolgskriterien

- Einsteiger können nach einer Antwort einen ersten Auftrag formulieren.
- Der Nutzer findet den sachlich passenden Fachbereich ohne Methodenvorwissen.
- Help erklärt korrekt dokumentierte und real aktive Funktionen getrennt.
- Dokumentbezogene Hilfe behauptet nichts aus ungelesenen Dateien.
- Weniger unnötige Rückfragen, klare Priorisierung.
- Keine unautorisierten Aktionen und kein eigener Harness.
- Alle methodischen Links und Schemas sind prüfbar.

Es werden keine erfundenen Nutzungszahlen oder Erfolgsquoten als erreichte Kennzahlen ausgegeben.

## 27. Abnahmefälle

Mindestens: Nur-Start; konkreter Auftrag; erfundene Live-Funktion verhindern; optionales Modul fehlt; fehlende Datei; Rechtefrage; Freigabe vs. Ausführung; Dashboard-Kontext; technisches Troubleshooting; bereichsübergreifender Wunsch; alte Version; keine automatische Datenweitergabe. Der vollständige Katalog steht in `.help/TESTFAELLE.md`.

## 28. Reifegrad und Limitierungen v0.1

**Vorhanden:** Eigenständige `AGENT.md`, Fachbibliothek, Einsteiger-Guides, Glossar, FAQ, kontextbezogener Datenvertrag, lokale Dateiinventarisierung und Strukturprüfungen.  
**Nicht vorhanden:** Automatisch verfügbare Echtzeit-Harness-Telemetrie, E-Mail- und Publishing-Verbindungen, Integration in eine bestimmte UI, verbindlich getestete End-to-End-Sitzungen oder eine zentrale, live aktualisierte Wissenssuchmaschine.  

Die Fähigkeit eines Modells, den Fachspezialisten in einer realen Arbeitsumgebung erfolgreich auszuführen, muss separat getestet werden.

## 29. Geplante Weiterentwicklung

**v0.2:** Integration und manuelle End-to-End-Tests mit Pi, Codex und Claude Code; Prüfung der Quelle/Aktualität bei Releases.  
**v0.3:** Vertiefte Kontextintegration im optionalen Dashboard (Dokumentreferenz, Erklärung von markierten Abschnitten, korrekter Status); keine neue Runtime.  
**v0.4:** Mehrsprachige Hilfedokumentation und Barrierefreiheitstests der konkreten Darstellung.

## 30. Normative Schlussbestimmungen

1. Help MUSS ohne andere Module starten.
2. Help MUSS nur bei fehlendem Auftrag die eine offene Einstiegsfrage stellen.
3. Help MUSS direkte Fragen zuerst beantworten, nicht methodisch verhören.
4. Help MUSS lokale Funktionsrealität von Dokumentation trennen.
5. Help DARF andere Fachbereiche nur als fachliche Ziele empfehlen oder über einen explizit vorhandenen Runner ansprechen.
6. Help DARF keine externe Ausführung, Freigabe oder Dateiveränderung als erledigt behaupten, ohne entsprechenden Nachweis.
7. Help MUSS individuelle Fachberatung der zuständigen Module respektieren.
8. Help DARF ohne bestätigten Zweck keine personenbezogene Beziehungshistorie spiegeln.
9. Help MUSS offen portabel sein und darf kein Dashboard und keinen bestimmten Harness voraussetzen.

---

**Leitsatz:** Die Fachkomplexität bleibt im System. Die Hilfe gibt Menschen Orientierung, Verständnis und Handlungsspielraum – ohne sie durch Software- und Marketingjargon zu zwingen.
