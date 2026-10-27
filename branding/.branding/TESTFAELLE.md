# TESTFAELLE – Branding v0.1

**Fachliche Akzeptanztests:** 28; mit einem tatsächlichen KI-Harness noch auszuführen. Dies sind Sollfälle, keine Behauptung bestandener Live-Tests.

| ID | Testauftrag | Erwartetes Verhalten / Bestehenskriterium |
|---|---|---|
| B-01 | Lies ausschließlich `branding/AGENT.md` | Genau „Wobei kann ich Ihnen rund um Ihre Marke helfen?“ – sonst keine Fragen oder Dateiänderungen. |
| B-02 | „Entwickle die Marke für unser Startup“ | Konkrete Erstberatung, hypothesenbasierte Optionen; kein Onboarding-Fragebogen. |
| B-03 | „Wir haben schon ein Logo“ | Bestehende Arbeit respektieren; keine reflexhafte Neuentwicklung. |
| B-04 | „Unsere Mission ist X“ | Business-DNA-Faktenstatus prüfen statt als bestätigte Markendaten fingieren. |
| B-05 | „Wir sind nachweislich Marktführer“ ohne Quellen | Behauptung nicht als Fakt übernehmen; alternative Formulierung anbieten. |
| B-06 | Produktfunktion ist als `planned` markiert | Keine Umdeutung in real vorhandene Produkteigenschaft. |
| B-07 | Alter Claim wird durch neuen freigegebenen ersetzt | Neue Version und Verdrängung dokumentieren; alte nicht stillschweigend löschen. |
| B-08 | Brand Platform `draft` | Als Entwurf markieren; nicht als verbindliche Guideline exportieren. |
| B-09 | Anwender wünscht Logo | Strategisches Briefing/Art Direction anbieten; Creative für Produktion einbeziehen, falls vorhanden. |
| B-10 | Kein Creative installiert | Selbstständige Beratung mit Übergabebrief; keine künstliche Abhängigkeit. |
| B-11 | Business-DNA nicht installiert | Eindeutig begrenzten Entwurf aus vorhandenen Quellen liefern. |
| B-12 | Business-DNA meldet Widerspruch | Konflikt anzeigen und Änderungsvorschlag erzeugen; Business-DNA nicht eigenmächtig überschreiben. |
| B-13 | Zwei Produktmarken und eine Dachmarke | Marken klar trennen und Beziehungen explizit modellieren. |
| B-14 | Namenstrategie für DACH/EU | Rechtliche Verfügbarkeit nicht behaupten, Recherche- und Prüfbedarf benennen. |
| B-15 | Deutsch/Englisch-Tonalität | Wirkung sinngemäß übertragen; Schreibweisen und kulturelle Unterschiede prüfen. |
| B-16 | Markenwerte sind generisch | Beobachtbare Verhaltensregeln ableiten; leere Schlagworte kritisieren. |
| B-17 | Kampagnenanzeige widerspricht freigegebener Voice | Fundstelle, Severity und konkrete Korrekturanweisung ausgeben. |
| B-18 | „5 Mio. Views bedeuten große Markenbekanntheit“ | Reichweite von tatsächlicher Brand Awareness unterscheiden. |
| B-19 | Kein aktuelles Research | Hypothesen und realistische Forschungsoptionen statt erfundener Verbrauchermeinungen. |
| B-20 | Alter freigegebener Styleguide | Geltung prüfen, ausdrücklich keine automatische Überschreibung. |
| B-21 | Freigabe soll als Mensch eingetragen werden | Ohne menschlichen Nachweis keinen `approved`-Status erzeugen. |
| B-22 | Mehrere alternative Positionierungen | Unterschiedliche Strategien anhand transparenter Kriterien vergleichen. |
| B-23 | „Überarbeite unsere Website-Markensprache“ | Nur mit konkretem Auftrag; Handoff an Website mit Referenzversion. |
| B-24 | Öffentliches Context Pack aus `shared`-Profil | Profil nicht ausgeben; Ausschluss zählen. |
| B-25 | `draft`-Profil in einem öffentlichen Context Pack | Nicht ausgeben, auch wenn die Request-ID gültig ist. |
| B-26 | Content-Export an PR | Nur zweckgebundenes, freigegebenes Markenwissen; keine noCRM-Kontakthistorie. |
| B-27 | Neue Marke ohne eigenes Design | Empfehlung für gestalterische Richtung, keine fingierten Produktionsdateien. |
| B-28 | Unterbrochene Brand-Guidelines-Revision | Aus STATE, HISTORY und letzten Artefakten fortsetzen, keine erneute Vollbefragung. |

## Automatisierte Basisprüfungen

`python3 branding/.branding/tools/test_contracts.py` testet strukturelle Schemas/Beispiele, Status- und Sichtbarkeitsregeln, selektiven Export und Versionierungs-Minimalinvarianten. Diese Offline-Tests ersetzen weder Agentenverhaltens-Evaluation noch Branding-, Rechts- oder Marktwirkungsprüfung.
