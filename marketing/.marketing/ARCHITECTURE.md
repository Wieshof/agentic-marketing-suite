# ARCHITECTURE – Arbeitsmodell, Persistenz und Zusammenarbeit

**Version:** 0.4

## Start ohne Arbeitsauftrag

Wenn nur `AGENT.md` gelesen wird und kein konkreter Marketingauftrag vorliegt, ist das **kein fachlicher Arbeitsschritt**. Genau eine Begrüßungsfrage gemäß `AGENT.md` stellen, danach auf den Nutzer warten. Keine Methoden laden, keine Ergebnisdateien anlegen, keinen LOG-Eintrag als Arbeitsleistung erfinden. Bestehende Zustandsdateien nicht ohne Auftrag verändern.

## Aufgabe → Beratung → Ergebnis

1. **Intent erfassen:** Welche Entscheidung, Wirkung oder Lieferung wird benötigt?
2. **Kontext sichern:** `STATE.md`, relevante vorhandene Ergebnisartefakte, bei Bedarf `HISTORY.md` und freigegebene Geschwistermodule sichten.
3. **Methodenwahl:** Bei nichttrivialen Fachfragen `METHODEN.md` prüfen und nur relevante Methodenanleitungen laden.
4. **Arbeiten:** Eigenständige Analyse, Abwägung, Beratung und konkrete Produktion. Ungewissheiten markieren.
5. **Qualität:** fachliche Tragfähigkeit, Quellenlage, Zielbezug, Machbarkeit, Recht/Sicherheit und Konsistenz prüfen.
6. **Ergebnis ablegen:** In vorhandener Ergebnisakte aktualisieren oder benötigtes Ergebnisverzeichnis erst jetzt erstellen. Nicht in `.marketing/methoden/`.
7. **Persistenz:** tatsächliche wichtige Operationen ins `LOG.md`; fachliche Beschlüsse/Meilensteine in `HISTORY.md`; aktueller Stand in `STATE.md`.
8. **Kommunizieren:** Ergebnisse, Empfehlung und nur tatsächlich erforderliche Entscheidungspunkte knapp darstellen.

## Internes Gedächtnismodell

| Objekt | Zweck | Änderung | Was gehört nicht hinein? |
|---|---|---|---|
| `STATE.md` | Aktueller Stand, Arbeitsziel, relevante Pfade, nächste Handlung | Zusammenfassend fortschreiben | Vollständige Protokolle |
| `LOG.md` | Reale Operationen, Änderungen, Fehler und überprüfbare Vorgänge | Chronologisch anhängen | Beliebiger interner Gedankengang, Gesprächstranskript |
| `HISTORY.md` | Bestätigte Beschlüsse, wesentliche Strategieänderungen, Meilensteine | Chronologisch ergänzen; Korrekturen explizit | Routineaktionen, bloße Spekulationen |
| `archiv/` | Unveränderte Originale, freigegebene oder ersetzte Artefaktversionen | Dateiversionen hinzufügen | Betriebsanweisungen |
| Ergebnisordner | Aktuelle fachliche Artefakte | Bedarfsorientiert | Methodeninstruktionen |

## Konsistenz und Wiederaufnahme

- `STATE.md` ist ein Wegweiser, **keine** zweite Kopie aller Konzepte. Quellen bleiben die Original-Artefakte und ihre Versionen.
- Bei widersprüchlichen Fassungen die letzte belegte Freigabe bzw. autorisierte Entscheidung prüfen, Konflikt dokumentieren und nicht stillschweigend entscheiden.
- Log nur für tatsächlich ausgeführte Aktionen schreiben, keine geplanten als erledigt kennzeichnen.
- Bei Schreibfehlern keine Erfolgsmeldung; im Dialog den noch nicht persistierten Stand transparent machen.
- Große Arbeiten dürfen in Teilergebnisse zerlegt werden; keine künstlich verpflichtenden Phasen.

## Arbeit mit Fachmodulen

Der Bereich ist ohne weitere Module funktionsfähig. Wenn `../website/`, `../social-media/`, `../advertising/` etc. vorhanden sind, können sie auf autorisierte Marketingartefakte und Ergebnisse verweisen. Sie dürfen ihre eigenen Fachregeln behalten und benötigen weder ein übergeordnetes Agentursystem noch eine zentrale Datenbank. Übertragene Aufträge nennen Ziel, Stand, Quellen/Version, erforderliches Ergebnis und Qualität – nicht automatisch jede interne Datei.
