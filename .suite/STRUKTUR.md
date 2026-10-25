# Struktur- und Ablageregeln v0.1

```text
agentic-marketing-suite/
├── AGENT.md                  # optionaler übergreifender Einstieg
├── .suite/                   # nur gemeinsame Anweisungen und Governance
│   ├── legal/                # Querschnittsrecht
│   ├── qa/                   # Prüfkataloge
│   ├── contracts/            # JSON-Schemas
│   ├── tools/                # lokale Prüfer
│   ├── STATE.md LOG.md HISTORY.md
│   └── ...
├── marketing/                # bestehend, unverändert
├── pr/                       # bestehend, unverändert
├── social-media/             # bestehend, unverändert
├── website/                  # bestehend, unverändert
├── advertising/              # bestehend, unverändert
├── creative/                 # bestehend, unverändert
├── noCRM/                    # bestehend, unverändert
├── analytics/                # bestehend, unverändert
└── vorhaben/                 # optional, erst bei echtem Mehrmodulauftrag
    └── <vorgangs-id>/        # Kontext, referenzierte Ergebnisse, Prüf-/Freigabeakte
```

- `.suite/` enthält **keine** persönlichen Kontakte, keine Kampagnenassets, keine vertraulichen Kundendaten, keine API-Schlüssel. Nur Standards und **übergreifende** Statusinformationen mit Referenzen.
- Alle bestehenden `input/`- und `archiv/`-Ordner und Ergebnisse bleiben unangetastet.
- Ein neuer Auftrag aus `website/` darf dort allein bearbeitet werden; `vorhaben/` ist dafür nicht nötig.
- Bei wirklich gemeinsamen Aufträgen eine Vorgangs-ID erzeugen, Modulergebnisse referenzieren statt kopieren, Artefakte mit Version und Hash versehen und nur angemessene Daten übergeben.
- Arbeitszustand, Log und Entscheidungshistorie lokal je Fachmodul pflegen; die Suite schreibt ausschließlich auftragsübergreifende Änderungen. Keine dauernden Synchronkopien.
- Bei Archiveinträgen auf zulässige Aufbewahrungsfristen, Löschrechte und Sperrkonzepte achten. Kein unveränderliches PII-Archiv gegen Betroffenenrechte.
