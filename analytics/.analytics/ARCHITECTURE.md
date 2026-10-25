# ARCHITECTURE — fachliche und technische Architektur v0.1

## Funktionsschichten
1. **Intent:** konkrete Entscheidungsfrage, betrieblicher Kontext und erlaubte Datenquellen.
2. **Discovery:** verfügbare Daten und optionale benachbarte Module entdecken, Methoden selektiv wählen.
3. **Ingest (read-only):** CSV/JSON/zugelassene APIs über austauschbare Adapter; Rohquelle unverändert speichern oder extern referenzieren.
4. **Semantik:** Quellenmetadaten, Metrikdefinition, Zeitzone, Granularität, Population, Filter, Einheiten harmonisieren; nicht unzulässig zusammenführen.
5. **Analyse:** deterministische Rechnungen, Qualitätsprüfungen, statistische Modelle nur wenn erforderlich und validiert.
6. **Kritische Interpretation:** Alternativerklärungen, Evidenzstärke, Unsicherheit und vermiedene Aussagen.
7. **Entscheidung:** priorisierte Maßnahmen und Prüfdesign; Fachmodul zur Ausführung nur nach explizitem Mandat.
8. **Provenienz:** Log, History, State, Datenstand, Codeversion und reproduzierbare Report-Artefakte.

## Betriebsgrenzen
- `.analytics/` ist Systemwissen und Zustand; ein `berichte/`, `analysen/`, `experimente/`, `dashboards/`, `messkonzepte/` entsteht nur bei Bedarf außerhalb davon.
- `input/` ist temporäre, kontrollierte Eingangszone. Nach verifizierter Übernahme Original unter `archiv/inputs/` sichern und input leeren, sofern die Zuordnung erfolgreich ist; nie vor Archivierung löschen.
- `archiv/` für Originale, alte freigegebene Berichte, Datenauszüge nach Aufbewahrungsregeln. Personenbezogene Daten nicht ungeprüft dauerhaft archivieren.
- Datenadapter dürfen nicht ungefragt externe Trackingänderungen vornehmen.
- APIs, Datenbanksysteme, KI-Modelle und Dashboards sind auswechselbar; CSV/JSON/Markdown bleiben Referenz.

## Kontrollfluss
Intent → Dateninventar → Qualität & Kennzahlen → Analyse & Gegenhypothesen → Handlungsempfehlung → Review → dokumentiertes Ergebnis.

## Ergebnisvertrag
Ein Resultat enthält: Fragestellung, Datenquelle, Zeitraum, Stand, Definitionen, Befund, Unsicherheit, Alternativerklärungen, Empfehlung, Nachmessung und Evidenzstatus (`insufficient|descriptive|associative|experimental|causal` nur falls gerechtfertigt).

## Zusammenarbeit
- `../advertising/`: Mediaplan- und Kampagnendaten; keine Budgetänderung durch Analytics.
- `../social-media/`: Formate, Posts und Metriken; keine Veröffentlichung.
- `../website/`: SEO, Webkennzahlen, Conversion; keine Tracking-/Site-Änderung.
- `../pr/`: Medienresonanz, redaktionelle Qualität und Befragungen; keine Medienkontakte.
- `../marketing/`: Unternehmensziele, KPIs und Strategien; keine Umdefinition von Zielen ohne Bestätigung.
- `../noCRM/`: aggregierte Beziehungsergebnisse unter Zweck- und Berechtigungsprüfung; kein Zugriff auf persönliche Kommunikation ohne Freigabe.
- `../creative/`: Creative-Tests und Qualitätsdaten; keine Medienänderung.
