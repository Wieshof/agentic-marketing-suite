# Abweichungen zwischen Wissen und Realität erkennen

**Methode:** `qualitaet/drift-und-aenderungen`  
**Fachbereich:** `qualitaet`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Externe oder interne Änderungen die bestehende Wissensgrundlage gefährden.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Alte Claims, neue Berichte, Reviews und Produktereignisse. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Geänderte Sachverhalte gegenüber alten Claims identifizieren.
2. Zwischen neuem Fakt, geänderter Selbstaussage und bloßer Nachricht unterscheiden.
3. Betroffene Pakete und Fachmodule benennen.
4. Änderungsantrag mit Evidenz priorisieren.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Nicht aus jedem neuen Social-Media-Post eine Faktenänderung machen.

## Ergebnis und Übergabe

Drift-Bericht und gezielte Aktualisierungsvorschläge. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
