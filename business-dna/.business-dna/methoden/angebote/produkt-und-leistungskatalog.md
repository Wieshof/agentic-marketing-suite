# Angebote konsistent katalogisieren

**Methode:** `angebote/produkt-und-leistungskatalog`  
**Fachbereich:** `angebote`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Produkte und Dienstleistungen als Basis für Kommunikation benötigt werden.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Leistungsblätter, Preislisten, Produktstatus, Demo-Unterlagen. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Produktfamilien, Varianten, Leistungen und Lieferumfang unterscheiden.
2. Verfügbarkeit und Zielmarkt je Angebot erfassen.
3. Preisangaben mit Gültigkeit, Währung und Quelle versehen.
4. Unbestätigte Leistungen nicht als erhältlich beschreiben.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Kategorie „geplant“ darf nicht in Checkout- oder Verkaufsbehauptung übergehen.

## Ergebnis und Übergabe

Aktueller Angebotskatalog mit Reifegradhinweisen. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
