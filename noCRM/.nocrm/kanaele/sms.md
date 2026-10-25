# SMS

**Technischer Weg:** SMS-Gateway oder Telekommunikationsprovider.

## Fachliche Eignung

NoCRM nutzt diesen Kanal nur, wenn die Person ihn zulässigerweise verwendet oder bevorzugt und eine technisch unterstützte, berechtigte Aktion möglich ist. Der Kanal muss das individuelle Anliegen unterstützen; ein günstiger Sendepreis allein ist keine Begründung.

## Vorbedingungen und Besonderheiten

Knappe Texte; Telefonnummer-Format; Belege; Werberecht; Kosten; STOP-Verfahren wo erforderlich. Prüfe außerdem Empfängeridentität, länderspezifische Regeln, Nachrichtenzweck, ggf. KI-Offenlegung, Kosten und Datensicherheit.

## Ablauf

1. Kontakt und Zweck identifizieren, Beleg-/Einwilligungsstand auflösen.
2. Kontext datensparsam lesen; unbestätigte Angaben als Vermutung kennzeichnen.
3. Klaren kurzen Entwurf erstellen, opt-out/Antwortkanal prüfen und nach Freigabe via Provider abwickeln.
4. Externen Versand ausschließlich bei dokumentierter Aktionserlaubnis und bestehendem Adapter starten.
5. Providerstatus und ggf. Fehler mit einem idempotenten Transaktionsschlüssel dokumentieren; bei unklarer Zustellung nicht blind wiederholen.

## Grenzen

Kein SMS-Anschluss enthalten. 1:1-Personalisierung ersetzt weder kanaltypische Nutzungsregeln noch gesetzliche Anforderungen.

## Referenz

https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011678&Paragraf=174
