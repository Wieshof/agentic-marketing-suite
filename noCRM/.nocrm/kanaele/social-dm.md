# Social-Media-Direktnachrichten

**Technischer Weg:** Plattformspezifische zugelassene Inbox-/Messaging-APIs, optional Social-Media-Modul.

## Fachliche Eignung

NoCRM nutzt diesen Kanal nur, wenn die Person ihn zulässigerweise verwendet oder bevorzugt und eine technisch unterstützte, berechtigte Aktion möglich ist. Der Kanal muss das individuelle Anliegen unterstützen; ein günstiger Sendepreis allein ist keine Begründung.

## Vorbedingungen und Besonderheiten

Kanalpolitik, Berechtigung, Session-/Reply-Fenster, Spamregeln, Kontaktidentität und vorhandene Interaktionen je Plattform prüfen. Prüfe außerdem Empfängeridentität, länderspezifische Regeln, Nachrichtenzweck, ggf. KI-Offenlegung, Kosten und Datensicherheit.

## Ablauf

1. Kontakt und Zweck identifizieren, Beleg-/Einwilligungsstand auflösen.
2. Kontext datensparsam lesen; unbestätigte Angaben als Vermutung kennzeichnen.
3. Kontextbezogene Antwort und Freigabe entwerfen; cross-platform ID nicht raten.
4. Externen Versand ausschließlich bei dokumentierter Aktionserlaubnis und bestehendem Adapter starten.
5. Providerstatus und ggf. Fehler mit einem idempotenten Transaktionsschlüssel dokumentieren; bei unklarer Zustellung nicht blind wiederholen.

## Grenzen

Nicht jede Plattform hat eine offizielle sendefähige öffentliche DM-API. 1:1-Personalisierung ersetzt weder kanaltypische Nutzungsregeln noch gesetzliche Anforderungen.

## Referenz

https://developers.facebook.com/docs/messenger-platform/
