# Architektur

Branding ist ein autonomes Modul innerhalb der Dateistruktur. `AGENT.md` startet die Beratung. `.branding/METHODEN.md` stellt passende Methoden bereit. Fachliche Entwürfe werden als Markdown-Artefakte in bedarfsgerecht erzeugten Ergebnisordnern abgelegt. Maschinenlesbare Profile/Context Packs nutzen JSON.

**Logische Strömung:** Auftrag → passende Quellen → Diagnose → Markenoptionen → Empfehlung → freigabefähiges Ergebnis → Review → freigegebene Leitplanken → zweckbezogene Handoffs → gemessene Rückmeldungen → Änderungsentscheidung.

Fachliche Verantwortungen werden nicht allein durch Dateipfade autorisiert. Branding ist kanonisch für strategische Markenentscheidungen, Business-DNA für belegbare Organisationsfakten, Creative für Ausführung, Analytics für Messung. Abhängige Module funktionieren auch ohne Branding.

**Betriebsstand v0.1:** Es existieren Fachregeln, Methoden, JSON-Verträge, formale Lints und Offline-Context-Export; kein LLM-Harness, keine gemeinsame Runtime, kein Markenregisterdienst, keine Versand-/Publishing-Schnittstelle und keine externe Markenrechtsprüfung.
