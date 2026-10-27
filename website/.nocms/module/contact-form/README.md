# Kontaktformular · Capability v0.1

## Zweck / Voraussetzungen

Unabhängiges PHP-Kontaktformular ohne Datenbank, Framework oder noCRM-Laufzeit. [Gemeinsame Einrichtung](../common/README.md), PHP 8.3+, HTTPS, private Konfiguration und ein freigegebener begrenzter Serviceauftrag sind erforderlich.

## Konfiguration / Ein- und Ausgaben

Selektiv `webmodules.py --site /projekt/site install contact-form` ausführen. `/api/contact.php` liefert bei GET ein einfaches zugängliches Formular mit serverseitigem Token und Datenschutzlink. In `contact` sind fester Betreiberempfänger `to`, fester `from`, `transport`, Servicefreigabe und Aktivierung einzurichten. Benutzer dürfen keinen Empfänger oder freie Header vorgeben.

POST nimmt ausschließlich Name, E-Mail, Nachricht, Honeypot und Token entgegen. Namen/E-Mail-Adressen können keine Header-Zeilen einschleusen; die Besucheradresse wird nur als validiertes Reply-To verwendet. Felder sind größenbegrenzt. `outbox` schreibt einen privaten Eingang für Betreiber/noCRM; `mail` reicht die Anfrage an den konfigurierten Server-MTA weiter. Der Browser erhält 202 „entgegengenommen“, niemals eine behauptete Zustellbestätigung.

Der Mail-Adapter kann `import-contact --input /privat/inbound-<id>.json --output incoming.json` verwenden; Inhalte bleiben untrusted Daten. Ein Kontaktformular ist keine Werbeeinwilligung. Fehlende PHP-Unterstützung verlangt einen explizit konfigurierten externen Form-Endpunkt, keinen simulierten Empfang.

## Prüfung / Status

Servervalidierung, feste Header/Empfänger, HTTPS-Origin, signierter kurzlebiger Token, Replay-Sperre, Honeypot, Quoten und privater Speicher. Erfolgsstatus bedeutet `queued` oder `accepted`; bei Fehler keine stille alternative Zustellung. Falsche Eingaben liefern 422, Token/Herkunft 403, Quote 429 und nicht sicher verarbeitbare Anfragen 503. Keine automatische Wiederholung nach unklarem Transport. Tests prüfen diese Fälle mit fiktiven Adressen und privater Outbox, ohne echten Versand.
