# Integration von help/ in die Agentic Marketing Suite

1. Sicherungskopie/Commit der vorhandenen Suite anlegen.
2. Den ganzen Ordner `help/` in die Wurzel der bestehenden Suite kopieren; `.help/` (versteckter Ordner) erhalten.
3. Vorhandene Fachmodule, `.suite/`, Root-`AGENT.md`, Arbeitsergebnisse, Logs und Historien **nicht überschreiben**.
4. Optional im Modulregister `.suite/MODULES.md` Help als nicht-ausführenden Beratungsbereich ergänzen. Nur wenn dieses Register in der konkreten Version besteht.
5. Test: `Lies help/AGENT.md` → exakt eine natürliche Eröffnungsfrage.
6. Test mit Auftrag: `Lies help/AGENT.md. Wie beginne ich mit lokaler Werbung für einen Kleinbetrieb?` → direkte, kurze Hilfe plus Beispielauftrag.
7. Falls ein Dashboard vorhanden ist: `help/` in der Fachbereichsnavigation auflisten; Fragen und ggf. selektive Dokumentreferenz über den bestehenden Harness weiterreichen. Keine neue Chat- oder Freigabeengine bauen.
8. Vor Versionsangaben immer aktuelle Installation/README prüfen; neue Module nur nach Existenz nennen.
9. Fachtests auf Basis `.help/TESTFAELLE.md` durchführen. Offline-Tests sind kein Ersatz für echte Harness-Prüfung.

**Standalone-Nutzung:** Nur den Ordner `help/` lesen lassen; fehlende Nachbarmodule werden weder gefordert noch erfunden.
