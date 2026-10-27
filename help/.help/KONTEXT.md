# Kontextbezogene Hilfe – Vertrag und Leitlinien v0.1

Ein externer Client oder das Agenten-Harness **kann**, muss aber nicht, der Help-Anfrage den Dokumentbezug mitsenden. Empfohlener minimaler Kontext:

```json
{
  "schema_version": "0.1",
  "question": "Was bedeutet die SWOT-Analyse in dieser Strategie?",
  "document_ref": {"relative_path": "marketing/strategie/marketingkonzept.md", "section": "SWOT"},
  "preferred_depth": "short"
}
```

`document_ref` allein ist **kein Inhaltsnachweis**. Bei zugänglichen Dateien den relevanten Abschnitt lesen, andernfalls allgemeine Erklärung anbieten und klar sagen, dass die Datei nicht eingesehen wurde. Der Client darf auch nur Frage und Dokumentkontext (ohne Dokumenttext) liefern. Keine automatische Vollübertragung von Kontaktlisten, Zugangsdaten oder fremden Dateiverzeichnissen.

**Rückgabe:** natürliche Erklärung, optional dokumentbezogenes Beispiel, ggf. Evidenz- und Versionshinweis, genau ein nächster Schritt. Keine Vorgabe für einen bestimmten Dashboard-Transport, Stream oder Chat-SDK.

**Übergabe:** Eine Help-Antwort darf einen kopierbaren Auftrag für den zuständigen Fachspezialisten formulieren. Eine tatsächliche Weiterleitung ist eine fremde Runner-Fähigkeit und muss vor ihrer Behauptung bestätigt worden sein.
