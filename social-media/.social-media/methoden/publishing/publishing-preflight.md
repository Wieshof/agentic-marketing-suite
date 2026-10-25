# Publishing-Preflight

**Interner Methodenpfad:** `publishing/publishing-preflight` · **Version:** 0.1 · **Nur bei fachlichem Bedarf laden**

## Zweck und Entscheidung über den Einsatz
Veröffentlichungsblockaden systematisch erkennen. Prüfe zuerst, ob der tatsächliche Auftrag diese Analyse oder Technik benötigt. Wenn nicht: nicht anwenden. Bereits vorhandene Fakten und freigegebenes Kontextwissen priorisieren. Die Methode führt nicht automatisch zu einer Veröffentlichung.

## Vorgehen
1. **Auftrags- und Evidenzprüfung:** Kläre aus vorhandenem Material das Kommunikationsziel, die relevanten Menschen, den Kanal, die Verfügbarkeit von Quellen sowie die Grenzen der eigenen Werkzeuge. Fehlende nichtkritische Informationen als Hypothesen kennzeichnen.
2. **Kernschritt 1:** Asset-, Konto-, Scopes- und Policy-Fähigkeit prüfen.
3. **Kernschritt 2:** Freigaben, Uhrzeit/Zeitzone, Kosten und Idempotenz prüfen.
4. **Kernschritt 3:** Fehler als `blocked` mit konkreten Schritten zurückmelden.
5. **Beraterurteil:** Benenne das begründete Ergebnis, erkennbare Widersprüche, eine umsetzbare Empfehlung und höchstens die entscheidende offene Frage. Bei zweifelhaftem Nutzen begründet von der Maßnahme abraten.

## Ergebnis
**Liefern:** Preflight-Report mit Go/No-Go. So konkret wie das verfügbare Belegmaterial erlaubt. Bei reinem Dialog Ergebnis direkt zeigen; bei tatsächlichem Schreibzugriff unter einem **bedarfsgerecht erstellten** Ergebnisverzeichnis außerhalb `.social-media/` ablegen. Nicht in Methodenordner schreiben.

## QA und Grenzen
**Spezifisches Risiko:** Keine Veröffentlichung bei unbekanntem Connector-Support. Dazu immer Rechte, Privatsphäre, Werbe- und gegebenenfalls KI-Kennzeichnung, barrierefreie Umsetzung, reale Tool-Verfügbarkeit und potenzielle Reputationswirkung prüfen. Bei Veröffentlichung separates Freigabe- und Publishing-Gate erforderlich.

## Nützliche Übergaben
Beobachtungen/Entscheidungen können an andere Methoden, an kanalbezogene Formatanleitungen oder – wenn vorhanden und berechtigt – an `../marketing/`, `../pr/`, `../website/`, `../creative/` übergeben werden. Bestehendes Ergebnis mit Quellen/Datum und Revision referenzieren; kein unkontrolliertes Kopieren.
