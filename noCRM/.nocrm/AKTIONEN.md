# Ausführungsvertrag: Entwurf → Prüfung → Autorisierung → Aktion → Nachweis

## Zustandsautomat

`proposed → drafted → reviewed → approved → queued → sent → delivered`.
Alternative Zustände: `blocked`, `cancelled`, `failed`, `unknown_outcome`, `expired`.

Nicht jeder Provider bestätigt `delivered`. `queued` und `accepted` dürfen nicht zu `delivered` hochgestuft werden. Bei Timeout nach Sendversuch zunächst providerseitig nach idempotency_key oder Referenz suchen; nicht blind erneut senden.

## Gate vor jeder externen Aktion

1. Existiert eindeutige Zielperson (`contact_id`) und die richtige Kanalidentität?
2. Ist der Zweck eindeutig (service, personal, marketing, transactional)?
3. Ist der Zweck nach geltendem Recht und Kanalanforderungen zulässig und dokumentiert?
4. Wird beim Empfänger die KI-Natur der direkten Interaktion ausreichend kenntlich gemacht?
5. Sind Inhalt, Links, Fakten, Anhänge, sensible Inhalte, Tonalität und Empfängerkontext geprüft?
6. Gibt es Autorisierung des Betreibers für **diese Aktion** (bzw. ausdrücklich eingeräumten automatischen Kompetenzrahmen)?
7. Ist das Zielmedium angebunden, getestet und sendefähig? Gibt es Rate-/Kostenlimits und Fallback?
8. Wird die Action gegen Doppelversand geschützt, und kann ein Ergebnis belegt werden?

## Untergrenzen

Dry-Run-Tools in diesem Paket dürfen **nichts extern versenden**. Bei Nichterfüllung nur Entwurf, manuellen Hinweis oder Blockadereport produzieren. Eine Consent-CSV allein ist keine nachgewiesene gesetzliche Zulässigkeit.

## Menschliche Kontrolle

Für ungewöhnliche, rechtlich riskante, werbliche, streitige oder reputationsrelevante Kontakte mindestens Review; Routine-Servicekommunikation darf später innerhalb eines explizit dokumentierten Kompetenzrahmens automatisiert werden. Gesetzliche oder plattformseitige Eskalationswege nicht abschalten.
