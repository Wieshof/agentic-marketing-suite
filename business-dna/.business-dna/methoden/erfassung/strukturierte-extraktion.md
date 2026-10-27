# Atomare Aussagen aus Freitext gewinnen

**Methode:** `erfassung/strukturierte-extraktion`  
**Fachbereich:** `erfassung`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Texte viele Behauptungen oder Produktmerkmale enthalten.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Absätze und Fundstellen. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Zusammengesetzte Sätze in einzelne überprüfbare Aussagen auflösen.
2. Subjekt und Prädikat präzisieren, besonders Produkt/Unternehmen/Marke unterscheiden.
3. Jede Aussage vorläufig als declared, planned oder hypothesis klassifizieren.
4. Originalfundstelle, Zeitbezug und konkurrierende Formulierungen beibehalten.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Keine Vermutung als explizite Quellbehauptung ausgeben.

## Ergebnis und Übergabe

Claim-Kandidaten mit eindeutigen Quellstellen. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
