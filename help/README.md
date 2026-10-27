# Help & Learning Workspace v0.1

Eigenständiger KI-Hilfespezialist für die Agentic Marketing Suite: verständliche Erklärungen, Einstieg, Fachbereichswahl, Kontext-Hilfe und realistische Funktionsaussagen.

## Start

Ohne Auftrag: `Lies help/AGENT.md` → „Wobei kann ich Ihnen mit der Agentic Marketing Suite helfen?“

Mit Auftrag: `Lies help/AGENT.md. Ich betreibe einen kleinen Handwerksbetrieb und möchte mehr Kunden gewinnen – wie beginne ich?`

## Inhalt

- Hauptspezifikation: `Help-and-Learning-Conceptual-Architecture-User-Guidance-Contextual-Assistance-Specification-v0.1.md`
- `help/AGENT.md` – Rolle und Sofortstart.
- `help/.help/METHODEN.md` – **39 Methoden** in 8 Themenbereichen.
- `help/.help/ANLEITUNGEN.md` – **18** menschenlesbare Guides, FAQ, Glossar und Praxisfälle.
- `help/.help/KONTEXT.md` – optionaler Kontextvertrag für Dokumentfragen.
- `help/.help/WISSENSQUELLEN.md` – reale Funktion vs. Dokumentation.
- `help/.help/TESTFAELLE.md` – 30 fachliche Akzeptanzfälle.
- `.help/tools/` – optionale Offline-Datei- und Strukturprüfungen.
- `INTEGRATION-SUITE.md` – nicht-destruktive Übernahme in eine bestehende Suite.

**Kein eigener Harness, kein Dashboard, keine technischen Freigabe- oder Versandfunktionen.** Das Paket funktioniert auch ohne Zugriff auf die anderen Module als grundlegender Lernbegleiter. Die konkreten installierten Fähigkeiten müssen vor Auskünften zur Laufzeit geprüft werden.

## Lokale Checks

```bash
python3 help/.help/tools/scan_workspace.py --root .
python3 help/.help/tools/validate_help.py --root .
```

Keine Zusatzpakete und kein Internet notwendig.

## Lizenz

MIT, Copyright © 2026 Markus Ertel. Siehe `LICENSE.md`.

## Integration in diesem Repository

Help ist als zwölfter optionaler Fachbereich registriert. [Konkrete Dashboard-Nutzung, Übergaben und Statusmapping](.help/SUITE.md). Die ursprünglichen Paketunterlagen bleiben als Herkunftsdokumentation erhalten; Versions-/Funktionsauskünfte benötigen immer die aktuelle Installation.
