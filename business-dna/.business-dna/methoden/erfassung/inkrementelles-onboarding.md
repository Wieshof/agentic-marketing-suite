# Inkrementelle Wissenserfassung

**Methode:** `erfassung/inkrementelles-onboarding`  
**Fachbereich:** `erfassung`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Ein Unternehmen erstmals beschrieben wird oder wesentliche Informationen fehlen.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Vorhandenes Briefing, Ordner, Ziel des Nutzers. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. In vorhandenen Dokumenten nach den für den Auftrag relevanten Informationen suchen.
2. Einen ersten Faktenentwurf mit Herkunft und epistemischem Status schreiben, bevor Fragen gestellt werden.
3. Wissenslücken nach Risiko und fachlicher Relevanz statt nach alphabetischer Vollständigkeit priorisieren.
4. Nur Fragen stellen, deren Antwort die aktuelle Empfehlung oder Ausgabe wesentlich verändert.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Nicht aus dem ersten Gespräch eine 50-Fragen-Pflichterhebung machen.

## Ergebnis und Übergabe

Ein vorläufiges Organisationsprofil mit beschränkter Liste blockierender Fragen. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
