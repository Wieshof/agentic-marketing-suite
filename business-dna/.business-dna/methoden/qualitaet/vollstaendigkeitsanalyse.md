# Aufgabenspezifische Vollständigkeit messen

**Methode:** `qualitaet/vollstaendigkeitsanalyse`  
**Fachbereich:** `qualitaet`  
**Reifegrad:** v0.1 / beratende Arbeitsanleitung

## Zweck und Einsatz

Diese Methode ist sinnvoll, wenn: Eine Wissensgrundlage für ein Vorhaben beurteilt werden soll.

**Nicht schematisch starten:** Wenn ein konkreter Auftrag unmittelbar beantwortbar ist, liefert der Spezialist zuerst ein verwertbares Ergebnis. Die Methode wird nur in erforderlicher Tiefe genutzt.

## Benötigte Informationen

Frage, relevante Domänen, vorhandene Quellen/Claims. Fehlende Informationen werden mit Status `unknown`/`declared` versehen und nur dann erfragt, wenn sie das Ergebnis wesentlich verändern.

## Fachliches Vorgehen

1. Mindestens benötigte Informationen für genau diesen Auftrag bestimmen.
2. Vorliegende, unbekannte und strittige Angaben zählen.
3. Erhebliche Lücken nach Wirkung priorisieren.
4. Trotz Lücken eine begrenzte, explizit vorläufige Empfehlung ausgeben.

## Qualitätskontrolle

- Für wesentliche Aussagen stimmen Subjekt, Prädikat, Zeitpunkt, Quelle und epistemischer Status.
- Herkunftsangaben bleiben auch nach einer Umschreibung auf Claim-Ebene rekonstruierbar.
- Plan, Selbstbehauptung und unabhängig überprüfte Tatsache werden nicht verwechselt.
- Auswirkungen auf bereits veröffentlichte Context Packs und benachbarte Fachmodule werden bei relevanten Änderungen beurteilt.

**Besonderer Fehler:** Mehr Datensammlung ist nicht immer mehr Qualität.

## Ergebnis und Übergabe

Gap-Assessment ohne globalen willkürlichen Vollständigkeitsscore. Bei notwendigem Datenstand Claims/Quellen als JSONL ablegen, fachliche Zusammenfassung in Markdown erstellen. Nur tatsächlich geänderte Dateien im LOG dokumentieren. Erst bei fachlich wesentlicher bestätigter Entscheidung HISTORY oder Decision-Record aktualisieren.

## Grenzen

Die Methode allein autorisiert weder Recherche in fremden Accounts noch Veröffentlichung, Versand oder irreversible Dateiänderungen. Verfügbare Harness-Werkzeuge und die fachliche Freigabelogik bestimmen die tatsächliche Ausführung.
