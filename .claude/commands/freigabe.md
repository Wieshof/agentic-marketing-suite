---
description: Konkrete Freigabeanforderung für eine geprüfte Datei vorbereiten
argument-hint: <Datei> <Aktion publish|send|spend|print|delete|modify_external> <Ziel>
---
Bereite eine Freigabeanforderung vor für: $ARGUMENTS

1. `.suite/APPROVALS.md` vollständig befolgen. Datei, Version, SHA-256, Aktion, Ziel, Review-Snapshots und gegebenenfalls Budget/Ablauf zusammenstellen.
2. Die Anforderung als JSON neben die Datei schreiben und mit `python3 .suite/tools/approval_audit.py request ...` erfassen.
3. **Niemals** selbst `decide` aufrufen oder eine Entscheidung, Person oder Bestätigung erfinden. Der Person die Anforderung vorlegen und auf ihre ausdrückliche Antwort warten.
