# Struktur und Ablage v0.1

```text
help/
├── AGENT.md
├── .help/
│   ├── BERATUNG.md
│   ├── RULES.md
│   ├── ARCHITECTURE.md
│   ├── STRUKTUR.md
│   ├── WISSENSQUELLEN.md
│   ├── METHODEN.md
│   ├── KONTEXT.md
│   ├── QUALITAET.md
│   ├── INTEGRATION.md
│   ├── STATE.md
│   ├── LOG.md
│   ├── HISTORY.md
│   ├── TESTFAELLE.md
│   ├── methoden/
│   ├── guides/
│   ├── examples/
│   ├── schemas/
│   ├── tools/
│   └── tests/
├── input/
└── archiv/
```

Anweisungen liegen ausschließlich unter `.help/` und dem Einstiegspunkt `AGENT.md`. Erstellte nutzerspezifische Lernpläne oder erklärende Dokumente entstehen **nur auf Auftrag** außerhalb des versteckten Systemordners, z. B. `help/anleitungen/`. Es gibt keine von vornherein angelegten Ergebnisordner. `input/` bleibt temporär und wird nur nach gesicherter Übernahme geleert. `archiv/` bewahrt bei Bedarf ursprüngliche Dateien bzw. freigegebene Versionen.

Die vollständige Suite liegt ein Verzeichnis höher; für alleinige Nutzung kann Help auch isoliert gestartet werden und informiert über fehlende Module. Keine Forderung, die Daten der übrigen Module zu spiegeln.
