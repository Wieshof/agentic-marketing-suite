# Offene Übergabeverträge v0.1

## Ziel
Jedes Fachmodul bleibt unabhängig. Bei Zusammenarbeit wird **nicht die ganze Projektmappe** an ein anderes Modul übergeben, sondern ein kontrolliertes, beschreibbares Arbeitsobjekt.

### Arbeitsauftrag (`work-order.schema.json`)
ID, Aufgabe, führendes Modul, weitere Fähigkeiten, Ziel/gewünschte Wirkung, benötigte Eingabereferenzen, Zweck/Grenzen, Status und Risiko. Keine zwangsweisen CRM- oder Kundendaten.

### Artefakt (`artifact.schema.json`)
ID, Modul, Dateipfad, Typ, Versionsnummer, ggf. SHA-256, Ausgangsreferenzen, Inhaltsstatus, personenbezogene Daten (ja/nein), Medienrechte (geklärt/offen/nicht relevant). `draft` ≠ `approved` ≠ `published`.

### Prüfbericht (`review.schema.json`)
Artefakt-ID und Version, Prüftyp, Status, konkrete Findings, Evidenz-Referenzen, prüfende Kompetenz, Zeitpunkt. Prüfen ohne „juristisch freigegeben“ zu behaupten.

### Aktionsfreigabe (`action-approval.schema.json`)
Exakter Kanal/Aktion, Autorisierender, Zeit-/Budgetgrenze, Zielartefakt samt Hash, Freigabeergebnis, Ausführungs-ID. Niemals nur „ok“ als implizite Allzweckfreigabe speichern.

## Austauschprinzip
- `relpath` bezieht sich auf den **Suite-Root**; keine absoluten externen Pfade in Artefakten.
- IDs sind stabil, Überschreibungen erzeugen neue Version; ein einziges Modul ist Schreib-Owner des Artefakts.
- Prüfer geben Findings zurück, statt Dateien fremder Module unaufgefordert zu ändern.
- Quellenmaterial und personenbezogene Daten werden über erlaubte Referenzen, ggf. redigierte Ausschnitte übergeben.
- JSON-Schemas dürfen via Python-Standardbibliothek syntaktisch geprüft werden; vollwertige Validierung nutzt einen externen JSON-Schema-Validator oder das enthaltene lokale begrenzte Prüfwerkzeug.
