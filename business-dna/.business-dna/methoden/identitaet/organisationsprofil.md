# Unternehmensstammdaten und organisatorische Identität

**Methode:** `identitaet/organisationsprofil`  
**Fachbereich:** `identitaet`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Ein Factsheet oder organisationaler Kontext benötigt wird.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Firmenunterlagen, Registerinformationen, Selbstbeschreibung. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Rechtliche Organisation von Marken-, Projekt- und Produktnamen unterscheiden.
2. Stammdaten mit Datum/Geltungsraum und Quelle zuordnen.
3. Fehlende oder veraltete Angaben ausdrücklich kennzeichnen.
4. Nur geeignete bestätigte Angaben als offiziell geprüfte Fakten ausgeben.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Eine öffentliche Website ist nicht immer die maßgebliche Quelle für Rechtsform.

## Ergebnis und Übergabe

Unternehmensprofil mit quellengestützten Stammdaten. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
