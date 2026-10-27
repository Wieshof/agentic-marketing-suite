# Help & Learning – Architektur v0.1

## Komponenten

- `help/AGENT.md`: natürliche Einstiegsschnittstelle und Berufsrolle.
- `.help/`: Referenztexte, Methoden, Beispiele, Schemas, optionale lokale Prüfwerkzeuge.
- `../README.md` und `../.suite/`: referenzierte, **nicht kopierte** Suite-Informationen, nur wenn vorhanden.
- Fachmodule: eigene Autorität für Beratung/Produktion. Help darf ihre Arbeitsaufträge formulieren, aber nicht ihre Regeln ersetzen.
- Dashboard: optionaler Client, der einen Dateipfad oder Dokumentbezug mitsenden kann. Help verlangt kein Dashboard.
- Harness: externe Ausführung; kein Bestandteil von Help. Ohne Toolzugriff bleibt eine rein textliche Beratung gültig.

## Grundablauf

`Anfrage → Anliegen und Kenntnisstand aus Äußerung erschließen → gezielte Quellenprüfung → direkte verständliche Hilfe → optional Beispielauftrag / vertiefte Anleitung → Feedback`

**Contextual Assistance:** Für eine markierte Datei erhält Help im Idealfall relativen Pfad, optional einen Abschnitt/Seitenanker, bereits ausdrücklich mitgesendeten Text und den Zweck der Frage. Mehr Kontext wird nur bei Bedarf und vorhandenen Leserechten beschafft. Ein bloßer Dateiname ist kein Beleg für Dateiinhalte.

## Ausführungshoheit

Help darf keine Root-AGENT-Logik duplizieren. Es gibt keine von Help erfundenen Session-IDs, Workflowzustände oder Freigabeprozesse. Ein optionaler Handoff ist lediglich ein dokumentierter Anfrageentwurf beziehungsweise ein Aufruf einer **vorhandenen** Runner-Fähigkeit. Ohne Runner erfolgt keine Ausführung.

## Persistenz

`STATE.md` = letzter Hilfekontext ohne unnötige personenbezogene Speicherung; `LOG.md` = nur tatsächliche Aktionen; `HISTORY.md` = dauerhafte Änderungen an der Help-Bibliothek. Für die ganze Suite bleiben die `.suite/`-Dateien zuständig.

## Portabilität

Markdown/JSON, Python-Standardbibliothek nur für optionale Offline-Prüfungen. Kein verpflichtender Server, Vektordatenbank, Plugin und keine Browserabhängigkeit.
