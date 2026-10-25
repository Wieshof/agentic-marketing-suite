# ABLAUF – durchgehende Qualitätskette

```mermaid
flowchart TD
 A[Auftrag / bestehendes Briefing] --> B[Creative-Beratung und Fachdiagnose]
 B --> C[Leitidee / Art Direction / Varianten]
 C --> D[Produktionsmanifest und Quellenprüfung]
 D --> E[Editierbare Quellen und Render]
 E --> F[Technische QA]
 E --> G[Visuelle / redaktionelle / auditive QA]
 F --> H{Alle Blocker behoben?}
 G --> H
 H -- Nein --> I[Korrektur mit Provenienz]
 I --> E
 H -- Ja --> J[Dokumentierte Freigabe]
 J --> K[Kontrollierte Übergabe / optional externer Auftrag]
 K --> L[Archiv / Lernwissen]
```

Eine Freigabe nach dem eigentlichen Render hängt an der **konkret geprüften Dateiversion**, nicht an der Entwurfsidee. Externe Aktionen benötigen gesonderte Autorisierung.
