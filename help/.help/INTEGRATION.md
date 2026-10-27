# Optionale Integration in die Agentic Marketing Suite v0.1

1. Den Ordner `help/` neben `marketing/`, `website/`, `pr/` usw. ablegen; vorhandene Inhalte nicht überschreiben.
2. Im Suite-Modulregister **optional** `help` ergänzen. Nichts in den bestehenden Fachmodulen muss auf Help verweisen.
3. Einsteiger-Einstieg: `Lies help/AGENT.md` ohne weiteren Auftrag; erwartete Antwort: „Wobei kann ich Ihnen mit der Agentic Marketing Suite helfen?“
4. Mit Auftrag: `Lies help/AGENT.md. Wie fange ich mit meinem Handwerksbetrieb an?` → kurze Hilfe und ein kopierbarer Marketing-Auftrag.
5. Optionales Dashboard: Help als auswählbaren Fachbereich anzeigen; bei Kontextfragen relativen Dokumentpfad und Frage an den **bereits gewählten** Agenten-Harness übergeben. Keine neue Runner-Logik im Help-Modul.
6. Die lokale Suite kann mittels `help/.help/tools/scan_workspace.py --root /pfad/zur/suite` inventarisiert werden; das Ergebnis beweist **Dateiexistenz**, nicht aktive Funktionsfähigkeit.
7. Nach Änderungen an der Suite Grundlagen- und Versionsguide überprüfen; niemals fest verdrahtete Modulzahlen als ständige Tatsache ausgeben.

**Bei Standalone-Betrieb** erklärt Help allgemeine Abläufe; Hinweise zur Installation und Konfiguration können nur nach Einsicht in die tatsächliche Umgebung konkretisiert werden.

## Konkreter Suite-Stand

Help ist in dieser Arbeitskopie als zwölfter optionaler Fachbereich registriert; Branding und Business-DNA sind ebenfalls vorhanden. Für andere Installationen weiterhin die tatsächlichen Pfade prüfen. [SUITE.md](SUITE.md) beschreibt vorhandenen Dashboard-Transport, Dokumentreferenzen und Vertragsmapping, ohne eine neue Runtime einzuführen.
