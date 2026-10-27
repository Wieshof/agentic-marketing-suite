# ARCHITECTURE – Domänen und Laufzeitgrenzen

**Kern:** Organisation -> Claims -> Quellen -> Entscheidungen -> Events -> Context Packs.

- Human readable: Markdown-Profil und thematische Wissensdokumente.
- Machine readable: UTF-8 JSONL für Claim-/Source-/Decision-/Event-Records.
- Context Pack: selektierter JSON-/Markdown-Snapshot.
- Methodenbibliothek: nur situativ geladene Verfahren.
- Optionale CLI: kleine Offline-Datenprüfungen ohne Server.
- Ausführung: vorhandener Harness; keine neue Agenten-Runtime.

Daten und Methoden strikt trennen. Business-DNA betreibt weder Produktdatenbank/ERP noch CRM; es bildet relevante Fakten referenziert ab. Für Fachmodule und externe KI-Systeme nur zweckgebundene Datenpakete.
