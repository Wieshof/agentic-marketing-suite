# Governance, Freigaben und Verantwortung v0.1

## Verantwortungen (nicht zwingend zusätzliche KI-Agenten)
- **Fachspezialist:** fachlich richtige Erstellung, Selbstprüfung, Übergabe, Kennzeichnung von Unsicherheit.
- **Unabhängige Prüfkompetenz:** QA-Resultate mit Evidenz und Kritik; ein LLM allein darf sich die eigene Arbeit nicht unbeschränkt freigeben.
- **Rechts- / Datenschutzkompetenz:** situative rechtliche Beurteilung; bei komplexen Fällen kompetente juristische Prüfung.
- **Handlungsberechtigte Person / Instanz:** gibt riskante externe Aktionen mit spezifizierter Reichweite frei (Medium, Artefaktversion, Konto, Budgetlimit, Zeitraum).
- **Ausführungsschnittstelle:** prüft vor Aktion erneut Status und Berechtigungen; dokumentiert echte Anbieterantworten und Fehler.

## Policy-Gates (harte Stopps)
`G0` Zugriff erlaubt? → `G1` Zweck/Briefing plausibel? → `G2` fachliche/technische Qualität? → `G3` Legal/Privacy/Assetrechte? → `G4` autorisierte konkrete Aktion? → `G5` tatsächliche technische Ausführung? → `G6` Nachkontrolle & Messung.

Ohne erfolgreiche `G2`/`G3`/`G4` **keine Außenwirkung**. `G5` ist ausdrücklich kein KI-Wunschdenken. Veröffentlichungs- und Sende-APIs dürfen nicht durch Antworttext simuliert werden.

## Freigabeobjekt
Referenziert exakte Artefaktversion/Hash, Aktionstyp, Zielsystem, Autorisierende, Zeitpunkt und ggf. Budget/Limit. Ein „Bitte überarbeite den Post“ autorisiert **nicht** automatisch „veröffentliche den Post“. Ein allgemeines „mach Marketing“ autorisiert **keinen kostenpflichtigen Einkauf**.

## Delegation
Module dürfen fachliche Arbeit untereinander beauftragen, aber **keine Berechtigungen ausweiten**. Für personenbezogene Daten immer Zweck-/Zugriffsprüfung, strenge Need-to-know-Regel; nur die notwendigen Felder weitergeben.

## Ausnahmen
Dokumentierte Ausnahmen nur, wenn rechtlich zulässig und von befugter Person verantwortet. Nicht ausnehmbar: fehlende rechtmäßige Grundlage, fehlende essentielle Schutzmaßnahmen, nicht autorisierte Ausgaben oder schwerwiegende Sicherheitsverstöße.
