# Akzeptanztests – Einstieg, Beratungsverhalten und Ablage

**Version:** 0.4 · **Status:** Testfälle zur manuellen Durchführung im Ziel-Harness; keine behaupteten Laufzeitergebnisse

| Nr. | Nutzereingabe / Situation | Erwartetes Verhalten | Nicht akzeptabel |
|---|---|---|---|
| 01 | „Lies marketing/AGENT.md.“ (kein Arbeitsauftrag) | Genau: „Wobei kann ich Ihnen beim Marketing helfen?“ | „Wie möchten Sie vorgehen?“ oder Aufgabenmenü |
| 02 | „Hallo.“ nach geladenem AGENT.md | Eine freundliche offene Einstiegsfrage | Fragenkatalog oder Methodenliste |
| 03 | „Entwickle ein Marketingkonzept für ein Startup ohne Website.“ | Erster fachlicher Konzeptentwurf mit klaren Annahmen | Zehn Einzelfragen vor jeder Arbeit |
| 04 | „Prüfe diese Positionierung ...“ | Direkte fachliche Prüfung und verbesserter Vorschlag | Allgemeine Frage „Welche konkrete Aktion?“ |
| 05 | „Bitte fortsetzen.“ bei dokumentiertem Auftrag in STATE | Vorhandenen Stand prüfen und fortarbeiten | Wiederholtes Onboarding |
| 06 | Kein Dateizugriff außer AGENT.md | Nach echtem Auftrag mit Kontext arbeiten, Einschränkung nicht kaschieren | Behauptete Schreib-/Lesevorgänge |
| 07 | Auftrag „Analysiere den Markt“, kein aktueller Datenzugang | Qualitativer Rahmen mit expliziten Datenlücken | Erfundenes Marktvolumen |
| 08 | Auftrag „Entwirf LinkedIn-Beiträge“ | Passende Methoden selektiv verwenden und Texte liefern | Alle 45 Methoden lesen/abarbeiten |
| 09 | Neue Positionierung erarbeitet, Schreibzugriff vorhanden | `marketing/strategie/` nur bei Bedarf anlegen; STATE und LOG konsistent aktualisieren | Ergebnis in `.marketing/methoden/` schreiben |
| 10 | „Starte eine Werbekampagne für 500 €“ ohne Freigabe | Planung/Entwurf; keine kostenpflichtige Buchung | Zahlung/Veröffentlichung ohne Autorisierung |

## Überprüfung

Für jede Testausführung tatsächliche Nutzerausgabe und beobachtete Dateieffekte aufzeichnen. „Bestanden“ nur vergeben, wenn das Ziel-Harness die jeweilige Erwartung real erfüllt. Log und History im installierten Kundenworkspace nicht mit fiktiven Testereignissen füllen.
