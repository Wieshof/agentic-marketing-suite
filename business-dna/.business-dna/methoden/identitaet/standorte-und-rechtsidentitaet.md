# Standorte, Handelsnamen und Rechtsidentität

**Methode:** `identitaet/standorte-und-rechtsidentitaet`  
**Fachbereich:** `identitaet`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Impressum, Unternehmensdarstellung oder rechtliche Stammdaten geklärt werden.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Aktuelle Register- und Firmendaten, Selbstauskunft. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Sitz, Betriebsstätte, Kontaktadresse und regionale Marktpräsenz getrennt erfassen.
2. Rechtsform und Handelsnamen anhand geeigneter offizieller Quellen abgleichen.
3. Gültigkeitsdatum, abweichende Unternehmensbezeichnungen und Änderungen prüfen.
4. Unsichere Angaben zur Fachprüfung markieren.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Kein Ersatz für rechtsverbindliche Firmenbuch- oder Rechtsprüfung.

## Ergebnis und Übergabe

Strukturiertes Rechtsidentitätsprofil mit Stand der Prüfung. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
