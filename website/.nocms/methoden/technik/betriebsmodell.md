# Website-Betrieb und Verantwortlichkeiten
**noCMS-Fachmethode · technik · v0.2**

## Ziel und fachlicher Nutzen
Wartung, Monitoring und Wiederherstellung realistisch planen.

## Wann diese Methode wählen?
Produktivbetrieb, Übergabe, Betrieb ohne Team.

**Nicht automatisch anwenden:** Wenn das Anliegen bereits durch eine einfachere Handlung beantwortet werden kann oder keine verlässliche Datengrundlage vorliegt, zuerst beraten statt Formalanalyse simulieren.

## Benötigter Kontext
Hosting, Deploy-Zugänge, Pflegekapazität, Domains, Archive.

Kennzeichne **bestätigte Angaben**, **Beobachtungen**, **Quellen**, **Arbeitsannahmen** und **offene Entscheidungen**. Verwende gegebenenfalls `../marketing/` oder andere Nachbarmodule nur bei wirklicher Existenz und Berechtigung.

## Arbeitsanleitung
1. Betreiberpflichten und Zuständigkeiten für Inhalte, Domain, Hosting, Sicherheit und Freigaben zuordnen.
2. Deployment-Prozess aus `site/` samt Veröffentlichungskontrolle definieren.
3. Backups, Wiederherstellung und Release-ZIPs voneinander abgrenzen.
4. Wartungs- und Aktualisierungsbedarf inklusive externer Abhängigkeiten priorisieren.
5. Notfall- und Übergabeschritte so dokumentieren, dass ein anderer Harness übernehmen kann.

## Konkrete Beratungsleistung / Ergebnis
Betriebscheckliste, Verantwortungsmatrix, Notfallplan.

Das Ergebnis muss verständlich, priorisiert und entscheidungsfähig sein: eine bevorzugte Empfehlung, nachvollziehbare Begründung, bei Bedarf Alternativen und ein kleiner nächster Schritt. Bei Beratungsauftrag keine automatische Änderung von `site/`.

## Fachliche Qualitätsprüfung
- Release-ZIP ist kein vollständiges Offsite-Backup.
- Kein „24/7 Monitoring“ behaupten ohne tatsächliche Infrastruktur.
- Ergebnisse nicht als ausgeführte Tests, tatsächliche Kundenaussagen oder verbindliche Freigaben ausgeben, wenn das nicht belegt ist.
- Bestehende `RULES.md`, `BRIEFING.md`, Sicherheitsgrenzen und bestätigte Designregeln berücksichtigen.

## Zusammenspiel und Persistenz
Diese Methode kann mit anderen Methoden aus `.nocms/METHODEN.md` kombiniert werden, wenn der aktuelle Auftrag das verlangt. Kundenbezogene Ergebnisse **nicht** in dieser Anleitung speichern, sondern in der Antwort oder – mit Dateiwerkzeugen und Auftrag – im passenden Projektartefakt (z. B. `.nocms/KNOWLEDGE/`, `.nocms/BRIEFING.md` oder einem zweckbezogenen Ergebnisdokument). Markante Entscheidungen gehören unter `.nocms/HISTORY/`, echte Aktionen in `.nocms/LOG.md`, aktiver Stand nach `.nocms/STATE.md`.
