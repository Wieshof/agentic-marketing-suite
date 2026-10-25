# Telegram Bot

**Technischer Weg:** Telegram Bot API bei selbst initiiertem Dialog.

## Fachliche Eignung

NoCRM nutzt diesen Kanal nur, wenn die Person ihn zulässigerweise verwendet oder bevorzugt und eine technisch unterstützte, berechtigte Aktion möglich ist. Der Kanal muss das individuelle Anliegen unterstützen; ein günstiger Sendepreis allein ist keine Begründung.

## Vorbedingungen und Besonderheiten

Bots können nicht zuerst einzelne Nutzer anschreiben; Chat-ID und Bot-Rechte erforderlich, sichtbarer Bot-Status. Prüfe außerdem Empfängeridentität, länderspezifische Regeln, Nachrichtenzweck, ggf. KI-Offenlegung, Kosten und Datensicherheit.

## Ablauf

1. Kontakt und Zweck identifizieren, Beleg-/Einwilligungsstand auflösen.
2. Kontext datensparsam lesen; unbestätigte Angaben als Vermutung kennzeichnen.
3. Bei eingehender Nachricht individuell antworten, Bot-Limits/Datenschutz und Antwortfreigaben beachten.
4. Externen Versand ausschließlich bei dokumentierter Aktionserlaubnis und bestehendem Adapter starten.
5. Providerstatus und ggf. Fehler mit einem idempotenten Transaktionsschlüssel dokumentieren; bei unklarer Zustellung nicht blind wiederholen.

## Grenzen

Offizielle Bot-API, nicht mit privaten Nutzeraccounts verwechseln. 1:1-Personalisierung ersetzt weder kanaltypische Nutzungsregeln noch gesetzliche Anforderungen.

## Referenz

https://core.telegram.org/bots
