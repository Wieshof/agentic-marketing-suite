# Kontaktformulare und eingehende Anliegen

**Technischer Weg:** Website-Integration mit Webhook, Spamfilter und Double-Opt-in nur wo tatsächlich benötigt.

## Fachliche Eignung

NoCRM nutzt diesen Kanal nur, wenn die Person ihn zulässigerweise verwendet oder bevorzugt und eine technisch unterstützte, berechtigte Aktion möglich ist. Der Kanal muss das individuelle Anliegen unterstützen; ein günstiger Sendepreis allein ist keine Begründung.

## Vorbedingungen und Besonderheiten

Zweckbindung, Spam, Inputvalidierung, Datensparsamkeit, automatische Empfangsbestätigung und Anfrage-Quelle. Prüfe außerdem Empfängeridentität, länderspezifische Regeln, Nachrichtenzweck, ggf. KI-Offenlegung, Kosten und Datensicherheit.

## Ablauf

1. Kontakt und Zweck identifizieren, Beleg-/Einwilligungsstand auflösen.
2. Kontext datensparsam lesen; unbestätigte Angaben als Vermutung kennzeichnen.
3. Personalisierte Antwort, ohne Formularanfrage automatisch als Marketingeinwilligung zu betrachten.
4. Externen Versand ausschließlich bei dokumentierter Aktionserlaubnis und bestehendem Adapter starten.
5. Providerstatus und ggf. Fehler mit einem idempotenten Transaktionsschlüssel dokumentieren; bei unklarer Zustellung nicht blind wiederholen.

## Grenzen

Produktives Hosting und Datenverarbeitungsverzeichnis separat einrichten. 1:1-Personalisierung ersetzt weder kanaltypische Nutzungsregeln noch gesetzliche Anforderungen.

## Referenz

https://www.edpb.europa.eu/topics/key-gdpr-concepts/basic-principles_en
