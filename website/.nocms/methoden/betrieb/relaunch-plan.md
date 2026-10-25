# Relaunch- und Veröffentlichungsplanung
**noCMS-Fachmethode · betrieb · v0.2**

## Ziel und fachlicher Nutzen
Ein Website-Release sicher vorbereiten, freigeben und nachvollziehbar verifizieren.

## Wann diese Methode wählen?
Go-live, Relaunch, Domainwechsel.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Geprüfte Site, Hostingzugang, Redirects, Freigaben, Tests.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Release-Scope, Rollback-Möglichkeit und betroffene URLs/Integrationen erfassen.
2. Alle relevanten Tests und Freigaben sammeln und Blocker priorisieren.
3. Vollständiges ZIP aus dem Inhalt von `site/` erstellen und verifizieren.
4. Nur autorisiert veröffentlichen, Ergebnis auf Zielhosting prüfen und Status korrekt melden.
5. Release in `archiv/releases/`, `.nocms/HISTORY/`, `.nocms/STATE.md` und ggf. `.nocms/LOG.md` nachweisbar dokumentieren.

## Konkrete Beratungsleistung / Ergebnis
Release-Checkliste, Statusbericht und Rollbackplan.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Ohne Prüfung auf Zielhosting „Deployment erfolgreich“ nicht behaupten.
- Keine privaten `.nocms/`-Dateien ins ZIP aufnehmen.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
