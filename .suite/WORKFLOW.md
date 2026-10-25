# Gesamtablauf / Dynamic Coordination v0.1

## Ziel und Nicht-Ziel
Der Ablauf ist **intent-gesteuert, ereignisbasiert und dynamisch**. Kein starrer linearer Acht-Modul-Prozess, kein zentrales Agenten-Hierarchiesystem. Ein Auftrag kann in einem einzigen Modul abgeschlossen werden.

## Phasen (nur nach Bedarf)
**0. Auftrag erkennen.** Was soll erreicht werden, welche Entscheidung oder welches Ergebnis zählt? Bestehende Informationen und Historie beachten. Nur bei echtem Blocker fragen.

**1. Betroffene Fähigkeiten wählen.** Primär zuständiges Modul bestimmen; optionale Nachbarn nur bei Mehrwert. Rechte-/Datenzugriffsgrenzen respektieren. Beispiel „Landingpage reparieren“ = `website/`; „Kampagne zum Produktstart“ = mehrere.

**2. Vorhandene Artefakte lesen.** Referenz auf bestätigte Unternehmens-/Markeninformation, nicht alles redundant kopieren. Annahmen explizit kennzeichnen.

**3. Plan und Abhängigkeiten.** Nur falls nötig ein kurzes Arbeitsobjekt mit Aufgaben, zuständigen Modulen, Eingaben, erwarteten Ergebnissen und Qualitätsrisiken. Parallelisierung dort, wo echte Unabhängigkeit besteht.

**4. Entwurf / Beratung.** Fachmodul arbeitet eigenständig, zeigt erste nutzbare Version, begründet Entscheidungen; benutzt nur passende Methoden.

**5. Produktion.** Artefakt mit Versionskennung, Quellenreferenzen, Medienrechten und technischen Parametern erzeugen. Bei noch fehlenden Tools als Entwurf/Manifest ausgeben, nicht falsche Produktion behaupten.

**6. QA & Legal.** Risikoadaptive Prüfung pro Artefakt und übergreifend auf Konsistenz: Stimmen Claims, Corporate Design, Zahlen und Rechte zwischen Website, Anzeige, PR und Social zusammen? Offene Compliance-Fragen blockieren bei erforderlicher Außenwirkung.

**7. Korrekturschleife.** Defekt an verursachendes Fachmodul zurückgeben; neue Version; genau betroffene Gates erneut prüfen. Nicht unbegrenzt still iterieren: erkennbare Qualitätsgrenzen bzw. Konflikte offenlegen.

**8. Konkrete Freigabe.** Für relevante Außenwirkung eine berechtigte Person/Instanz mit exakt definierter Aktion. Freigabe auf Artefaktversion/Hash, Kanal, Budget und Zeitrahmen begrenzen; bei Budget nie aus einer allgemeinen Aufgabenbeschreibung ableiten.

**9. Ausführung.** Adapter prüft Freigabe unmittelbar vor der Aktion, erstellt Idempotency-Key, sendet einmal und dokumentiert tatsächlichen technischen Status. Bei Timeout/unklarer Antwort Status abrufen, **nicht blind wiederholen**.

**10. Messung und Lernen.** Analytics nutzt zulässige Daten, prüft Qualität und Kausalitätsgrenzen, stellt Verbesserungsaufträge. Strategie/Creative/Media können überarbeitet werden; neue Releases durchlaufen wieder Gates.

## Beispiel – bereichsübergreifende Markenbekanntheitskampagne
`marketing/`: Hypothesen, Ziel und Positionierung → `advertising/`: Media/Leitidee + `pr/`: Themen/Medienstrategie → `creative/`: Varianten/Assets → `website/`: Landingpage + `social-media/`: kanalbezogene Adaption → **gemeinsame QA/Legal** → getrennte Freigaben/Publikation → `analytics/`: Messplan, Wirkung, Verbesserungen. `noCRM/` **nur** bei einem tatsächlich relevanten, rechtlich zulässigen 1:1-Kommunikationsfall; keine verpflichtende Kontaktkampagne.

## Beispiel – kleiner Direktauftrag
„Überarbeite diesen Webtext“ → `website/` führt aus; nur betreffende Fakten-, Marken- und Rechteprüfungen; keine künstliche Campaign-ID oder Acht-Modul-Gespräch.

## Hand-off
Arbeitsauftrag nach `contracts/work-order.schema.json`, Ergebnis nach `contracts/artifact.schema.json`, QA nach `contracts/review.schema.json`, Freigabe/Aktion nach `contracts/action-approval.schema.json`. Für minimale Arbeiten genügt eine lesbare Markdown-Datei; maschinenlesbarer Vertrag erst bei Automatisierung/Mehrmodulverknüpfung nötig.
