# Integration in die Agentic Marketing Suite v0.2.1

Dieses Paket ergänzt die Suite **additiv**. Es überschreibt weder vorhandene `AGENT.md`-Dateien noch `.suite/`, noch die neun bestehenden Fachbereiche.

1. Ordner `business-dna/` auf oberster Suite-Ebene hinzufügen.
2. Root-`AGENT.md` oder `.suite/MODULES.md` können anschließend optional folgenden Hinweis erhalten: `business-dna/AGENT.md`: Beratung zum Unternehmenswissen, Status-/Quellenprüfung und Kontext-Exporte.
3. Andere Spezialisten können `../business-dna/` gezielt nutzen. Bei nicht installiertem Modul arbeiten sie ohne Änderung weiter.
4. Nur bei fachlichem Auftrag Ergebnisordner anlegen; `.business-dna/` ist die interne Methodenbibliothek.
5. Betriebsdaten wie `business-dna/wissen/`, `input/`, `archiv/` dürfen nicht versehentlich veröffentlicht werden. Die beigelegte `.gitignore` zeigt eine mögliche Untergrenze; prüfe die bestehenden Repo-Regeln bei Integration.
6. Die Suite-Governance (`.suite/QUALITY.md`, `.suite/LEGAL.md`, Freigaben) bleibt unverändert. Ein Context Pack ist keine technische Freigabe.

**Einführungsempfehlung:** Zuerst den eigenständigen Betrieb testen, dann selektive Übergaben an Marketing und Branding implementieren.
