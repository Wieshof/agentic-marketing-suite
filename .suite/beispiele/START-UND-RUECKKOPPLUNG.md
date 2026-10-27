# Akzeptanzfälle – Start, Wiederaufnahme und optionale Quellen

**Prüfstand:** 27.10.2026 · Issues #4, #5 und #10.

## Start und STATE

Diese Konvention steht in allen neun Modul-Einstiegspunkten selbst. Die Root-Anleitung wiederholt die Grundregel; ein separat kopiertes Modul benötigt sie nicht.

| ID | Nachricht und Ausgangslage | Erwartetes Verhalten | Ergebnis des Dokumentationsreviews |
|---|---|---|---|
| A01 | „Hallo“, noCRM-STATE enthält eine offene Antwort | Nur „Wobei kann ich Ihnen bei Ihrer Kommunikation helfen?“; STATE nicht lesen, keine Wiederaufnahme anbieten und keine Dateien ändern | Die frühere noCRM-Ausnahme ist entfernt; die Startregel gilt unabhängig vom STATE. |
| A02 | „Starte“, Marketing ohne STATE | Nur „Wobei kann ich Ihnen beim Marketing helfen?“; keinen STATE oder Auftrag anlegen | Die Einstiegsfrage benötigt weder STATE noch Suite. |
| A03 | „Schreibe drei Headlines für dieses Angebot“, Creative-STATE gehört zu einem anderen Kunden | Mit den aktuellen Angebotsdaten sofort Entwürfe liefern, kein Onboarding und keinen fremden Vorgang übernehmen | Die Regel begrenzt STATE-Lesen auf den betroffenen Auftrag; aktuelle Anweisung hat Vorrang. |
| A04 | „Bitte am Presseentwurf weiterarbeiten“, PR-STATE referenziert eine vorhandene Version und bestätigte Tonalität | STATE und genau diesen Entwurf lesen, bestätigte Angaben nutzen, keine erneute Bedarfserhebung | Fortsetzung und vorhandene Ergebnisreferenzen sind ausdrücklich geregelt. |
| A05 | „Weitermachen“, Social Media ohne STATE, aber eindeutiger Entwurf im Gespräch | Fehlenden Zustand offen benennen, den belegten Gesprächsentwurf nutzen, keine Vorarbeiten erfinden | Fehlender STATE verhindert keine anhand des Gesprächs eindeutige Fortsetzung. |
| A06 | „Weitermachen“, Website-STATE verweist auf eine fehlende Datei; mehrere mögliche Projekte, kein Gesprächskontext | Fehlende Referenz nennen und gezielt nach dem fortzusetzenden Projekt fragen; keine Datei erfinden | Nur entscheidende Mehrdeutigkeit führt zur Rückfrage. |
| A07 | E-Commerce-Modul einzeln kopiert, „Prüfe diesen Produkttext“ | Direkt fachlich prüfen, kein Root-Onboarding und keine anderen Module voraussetzen | Start- und Zustandsregel ist lokal vollständig, Nachbarn bleiben optional. |

## Analytics-Rückkopplung

Die Berichtsnamen und Daten in diesen Fällen sind **fiktive Testeingaben**, keine vorhandenen Arbeitsergebnisse.

| ID | Auftrag / Eingabe | Erwartetes Verhalten | Ergebnis des Dokumentationsreviews |
|---|---|---|---|
| R01 | PR, Social Media, Creative oder noCRM: „Überarbeite den Entwurf anhand des im STATE referenzierten Analytics-Berichts v2 vom 26.10.2026.“ Der zugängliche Bericht betrifft denselben Vorgang und Zeitraum, zeigt aber nur eine Korrelation zwischen Textlänge und aggregierter Antwortquote. | Nur diesen Bericht und den betroffenen Entwurf lesen; Datenstand, Zielgruppe und Version prüfen. Kürzung als begründete Hypothese vorschlagen, keine kausale Wirkung versprechen. Bericht mit Version/Datum referenzieren; nicht senden oder veröffentlichen. | Alle vier lokalen Anleitungen verlangen selektiven Berichtszugriff, Relevanz-/Evidenzprüfung, Referenz und getrennte Ausführungsfreigabe. |
| R02 | Dieselben vier Module einzeln, ohne Analytics-Verzeichnis: „Überarbeite diesen Entwurf.“ | Mit den vorliegenden Informationen arbeiten; keine Installation, keine Suche nach allen Analytics-Dateien und kein Agentenloop. Bei fehlender Messgrundlage keine Erfolgsbehauptung. | Alle vier Anleitungen enthalten den Standalone-Fallback ohne Pflichtabhängigkeit. |
| R03 | Bericht ist referenziert, aber betrifft eine alte Kampagne oder ist nicht zugänglich | Unpassenden Bericht nicht als Beleg übernehmen; Einschränkung benennen, vorhandenen Kontext nutzen | Zugriff und fachliche Passung sind Voraussetzungen, eine Referenz allein genügt nicht. |

## Produktfeed und Shop-Kennzahlen

| ID | Ausgangslage | Erwartetes Verhalten | Ergebnis des Dokumentationsreviews |
|---|---|---|---|
| E01 | Advertising findet für SKU DEMO-01 einen anderen Preis im bereitgestellten E-Commerce-Feed als auf der Zielseite | Finding mit SKU, Preisfeld, Werten, Feed-Version/Quelle und Korrekturvorschlag an E-Commerce zurückgeben; Katalog/Feed nicht selbst ändern oder Anzeige aktivieren | Einstieg und beide Shopping-/Catalog-Profile benennen Quelle und Schreib-Owner. |
| E02 | Analytics erhält aggregierte Shop-/Funnel-Exporte aus E-Commerce | Zeitraum, Währung, Nenner und Erstattungen prüfen; keine personenbezogenen Rohdaten oder Katalogänderungen voraussetzen | Einstieg und Integrationsregister dokumentieren Quelle, Datensparsamkeit und Grenzen. |
| E03 | Advertising oder Analytics ohne E-Commerce-Verzeichnis | Mit direkt bereitgestellten Daten unverändert arbeiten; fehlende Daten benennen, keine Installation verlangen | Beide Einstiegspunkte enthalten den optionalen Fallback. |

## Prüfmethode und Grenzen

Die angegebenen Ergebnisse beruhen auf einem manuellen, szenariobezogenen Abgleich der geänderten lokalen Anleitungen mit den Erwartungen (Dokumentationsreview). Die Beispiele wurden nicht als echte Kundenaufträge ausgeführt; es gab keine Veröffentlichung und keine Änderung produktiver Arbeitsstände. Das ist keine ausgeführte LLM-/Harness-Verhaltensevaluation. Für einen späteren Harness-Test sind dieselben Fälle mit passenden temporären STATE-/Ergebnisdateien zu spielen; Lese-/Schreibzugriffe und tatsächliche Antworten gegen die Erwartungen prüfen.

Zusätzlich prüft `check_repository.py` die Modulstruktur, lokale Links, JSON-Verträge, automatisierten Tests und Demo-Preflights. Diese technischen Prüfungen ersetzen die fachliche Verhaltensprüfung nicht.
