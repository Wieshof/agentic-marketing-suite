# STRUKTUR — offene und bedarfsorientierte Ablage

```text
analytics/
├── AGENT.md
├── .analytics/
│   ├── BERATUNG.md RULES.md ARCHITECTURE.md STRUKTUR.md
│   ├── METHODEN.md METRIKEN.md DATENMODELL.md INTEGRATIONEN.md
│   ├── STATE.md LOG.md HISTORY.md TESTFAELLE.md
│   ├── methoden/ quellen/ integrationen/ schemas/ tools/ tests/ beispiele/
├── input/
└── archiv/
```

Weitere Ordner entstehen **nur mit Ergebnissen** (z. B. `berichte/2026-10/`, `analysen/website/`, `experimente/`, `daten/abgeleitet/`). Kundennamen-/Mandantenhierarchie wird nicht vorausgesetzt. Eigene Firma ist Standard. Alle Reports haben stabile Quelldatei-IDs und vermeiden personenbezogene Rohdaten. Mehrere Analysekategorien dürfen fachlich zusammengeführt werden, ohne Quellenursprünge zu verwischen.

**Migration und Persistenz:** Bei Updates nie STATE, LOG, HISTORY, eigene Methoden, archivierte Quellen oder Ergebnisordner überschreiben. Starre Anweisungen und Vorlagen nur mit Versionsvergleich ersetzen.
