# Informationsgrenzen für Empfänger wählen

**Methode:** `kontext/empfaenger-und-verwendungszweck`  
**Fachbereich:** `kontext`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Ein interner oder externer Empfänger Unternehmenswissen erhält.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Requester, Zweck, Sichtbarkeitsklasse, notwendige Daten. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Empfänger und Begründung der Datenweitergabe klären.
2. Nur zur Aufgabe nötige Felder zulassen.
3. Besondere Risiken bei personenbezogenen oder vertraulichen Daten prüfen.
4. Export als auditierten Snapshot mit Ausschlüssen kennzeichnen.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Das Tool ersetzt keine technische Autorisierung im Harness.

## Ergebnis und Übergabe

Datensparsames Empfängerpaket. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
