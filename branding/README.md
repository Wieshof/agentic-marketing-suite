# Branding Workspace v0.1

Eigenständiger KI-Spezialist für **Brand Strategy, Markenidentität, Markenführung und Brand Governance**. Optionales Modul der Agentic Marketing Suite. Keine verpflichtende Datenbank, kein eigener Harness, keine Pflichtanbindung an externe Dienste.

## Schnellstart

1. Ordner `branding/` in einen Workspace kopieren.
2. Dem vorhandenen KI-System die Anweisung geben: **„Lies `branding/AGENT.md`.“**
3. Ohne weiteren Auftrag lautet die erwartete einzige Antwort: **„Wobei kann ich Ihnen rund um Ihre Marke helfen?“**
4. Beispielauftrag: „Entwickle aus diesen Informationen eine erste Markenpositionierung und einen Creative Brief.“ → Der Spezialist erstellt eine begründete Erstberatung, ohne Pflichtfragebogen.
5. Methodenregister: `.branding/METHODEN.md`; bei Bedarf werden die konkreten Anleitungen gelesen.

## Aufbau

- `branding/AGENT.md`: Rolle, Sofortstart und Verbindlichkeit.
- `branding/.branding/`: 51 Methoden, Regeln, Modelle, Governance, Kontextverträge, Hilfswerkzeuge und Testfälle.
- `branding/input/`: temporäre Eingänge.
- `branding/archiv/`: Ausgangsmaterialien und ältere Freigabeversionen.
- Dynamische Ordner `strategie/`, `identitaet/`, `verbal/`, `visual/`, `guidelines/`, `research/` u. a. entstehen nur bei realer Arbeit.
- `Branding-Conceptual-Architecture-Organizational-Knowledge-Specification-v0.1.md`: umfassende Architekturspezifikation.
- `INTEGRATION-SUITE.md`: nicht destruktive Integration in die Marketing-Suite.

## Ausführung / Qualität

Die Methode- und JSON-Struktur kann ohne Server verwendet werden. Offline-Lint und Context-Pack-Erstellung werden mit Python 3.10+ und Standardbibliothek bereitgestellt. `python3 branding/.branding/tools/test_contracts.py` führt lokale Verträglichkeitstests aus. Es werden **keine** Nachrichten gesendet, Marken angemeldet, Dateien veröffentlicht oder menschliche Freigaben imitiert.

Die fachlichen Akzeptanztests in `.branding/TESTFAELLE.md` sind noch mit einem realen KI-Harness auszuführen. Formale JSON-Gültigkeit ist kein Nachweis für fachliche Markenqualität oder Rechteklärung.

## Fachliche Grenzen

- Business-DNA = Unternehmensrealität; Branding = gewollte Marke; Creative = Gestaltung; Analytics = gemessene Außenwirkung.
- `approved` erfordert tatsächlichen menschlichen Nachweis. `draft` ist ein Vorschlag, kein freigegebenes Brandbook.
- Markenschutz, Lizenzen, Domainrechte und medienrechtliche Freigaben gesondert prüfen.
- Keine pauschale Datenweitergabe an andere Fachbereiche; Context Packs sind zweckgebunden.

## Lizenz

MIT für originäre Paketbestandteile. Eingebundene Schriften, Marken, Fotos, Standards und Drittmaterial bleiben unter ihren eigenen Rechten. Siehe `LICENSE.md`.

## Integration in diesem Repository

Das Paket ist als zehnter optionaler Fachbereich in der Suite registriert. Aktuelle Suite-Verträge, Kontextübergaben und Statusübersetzungen: [SUITE.md](.branding/SUITE.md). Die ursprünglichen Paketunterlagen beschreiben v0.1 und bleiben als Herkunftsdokumentation erhalten.
