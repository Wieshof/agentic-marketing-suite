# E-Mail und persönliche Korrespondenz

**Technischer Weg:** Gmail API, Microsoft Graph, optional IMAP/SMTP mit expliziten Kontorechten.

## Fachliche Eignung

NoCRM nutzt diesen Kanal nur, wenn die Person ihn zulässigerweise verwendet oder bevorzugt und eine technisch unterstützte, berechtigte Aktion möglich ist. Der Kanal muss das individuelle Anliegen unterstützen; ein günstiger Sendepreis allein ist keine Begründung.

## Vorbedingungen und Besonderheiten

Gesprächs-Thread, Reply-To, Signatur, Anhänge, DMARC/SPF/DKIM, Werbezweck und Abmeldung; vor allem kein ungeprüfter Kaltversand. Prüfe außerdem Empfängeridentität, länderspezifische Regeln, Nachrichtenzweck, ggf. KI-Offenlegung, Kosten und Datensicherheit.

## Ablauf

1. Kontakt und Zweck identifizieren, Beleg-/Einwilligungsstand auflösen.
2. Kontext datensparsam lesen; unbestätigte Angaben als Vermutung kennzeichnen.
3. Mail-Draft erstellen, Vorschau, Freigabe, Provider Draft-ID, Send- und Zustellrückmeldung.
4. Externen Versand ausschließlich bei dokumentierter Aktionserlaubnis und bestehendem Adapter starten.
5. Providerstatus und ggf. Fehler mit einem idempotenten Transaktionsschlüssel dokumentieren; bei unklarer Zustellung nicht blind wiederholen.

## Grenzen

Offiziell dokumentierte Gmail- und Microsoft-Graph-Mail-Schnittstellen; keine Kontoanbindung im Paket. 1:1-Personalisierung ersetzt weder kanaltypische Nutzungsregeln noch gesetzliche Anforderungen.

## Referenz

https://developers.google.com/workspace/gmail/api/guides/drafts
