# Prüfgates für organisatorisches Wissen

**Methode:** `qualitaet/acceptance-gates`  
**Fachbereich:** `qualitaet`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Eine Wissensversion als Arbeitsgrundlage freigegeben werden soll.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Schema- und Fachprüfberichte, Konfliktliste, Scope. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Formatprüfung und Nachweisprüfung unabhängig ausführen.
2. Fehler in essentielle und tolerierbare Kategorien einordnen.
3. Wesentliche ungeklärte Widersprüche und Freigabelücken dokumentieren.
4. Genau definieren, für welchen Zweck die Fassung verwendbar ist.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Keine technische Durchsetzung vortäuschen, wenn nur Dokumente geprüft wurden.

## Ergebnis und Übergabe

Zweckgebundene Annahmeempfehlung statt Pauschalsiegel. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
