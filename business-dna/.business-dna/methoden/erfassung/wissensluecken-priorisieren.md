# Wissenslücken nach Wirkung priorisieren

**Methode:** `erfassung/wissensluecken-priorisieren`  
**Fachbereich:** `erfassung`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Unsichere, unvollständige Profile für konkrete Aufgaben verwendet werden sollen.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Gewünschter Output, vorhandene Claims, bekannte Unknowns. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Feststellen, welche fehlenden Felder eine Entscheidung wirklich beeinflussen.
2. Auswirkung eines Fehlers gegen Beschaffungskosten und verfügbare Quellen abwägen.
3. Zunächst kostengünstige vorhandene Primärquellen prüfen.
4. Nur die kritischsten Lücken zur Rückfrage vorlegen.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Unvollständigkeit ist kein Grund, nutzbare Ergebnisse zu blockieren.

## Ergebnis und Übergabe

Priorisierte kleine Lückenliste mit Bearbeitungsvorschlag. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
