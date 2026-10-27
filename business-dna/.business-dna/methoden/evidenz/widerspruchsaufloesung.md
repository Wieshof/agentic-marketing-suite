# Konflikt zwischen Claims bearbeiten

**Methode:** `evidenz/widerspruchsaufloesung`  
**Fachbereich:** `evidenz`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Zwei Aussagen desselben Sachverhalts nicht zusammenpassen.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Konkurrierende Claims, Quellen, Zeitangaben. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Prüfen, ob unterschiedliche Zeiten oder Teilbereiche den Widerspruch erklären.
2. Gemeinsames Prädikat und gleiche Scope-Bedingungen herstellen.
3. Höherwertige, aktuell gültige Belege beschaffen oder als disputed markieren.
4. Relevante menschliche Entscheidung nur anfordern, wenn aus Quellen nicht entscheidbar.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Nicht automatisch das neueste Dokument gewinnen lassen.

## Ergebnis und Übergabe

Konfliktakte mit nachvollziehbarer Empfehlung. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
