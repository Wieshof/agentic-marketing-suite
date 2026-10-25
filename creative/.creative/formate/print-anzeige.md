# Druckanzeige

**Profil:** `print-anzeige` · **Zweck:** Gestaltungs- und Produktionsbriefing.

## Erforderliche Parameter
Format, Trim/Bleed/MediaBox, Profil, 1-/mehrseitig, Zielmedium, Text, Layout; PDF/X nur nach validiertem Profil.

## Konkrete Arbeitsweise
1. Beschaffe reale Spezifikationen von Auftraggeber, Druckerei oder Plattform und fixiere die Version/Quelle.
2. Definiere Gestaltungshierarchie, Texte, Bilder und editierbare Quellen; bestimme Varianten.
3. Wähle Renderer/Produktionsengine und plane Vorschau sowie Produktionsformat getrennt.
4. Prüfe Export und Inhalt mit unabhängigem Werkzeug sowie visuellem Review.
5. Dokumentiere QA-Ergebnisse, offene Fehler und Freigaben; ohne bestandene Produktionsprüfung nur `proof_only`.

## Akzeptanzkriterien
Druckerei-Jobticket, effektive ppi, Fonts, Anschnitt und Sichtproof. Keine fest angenommene Beschnittzugabe.

## Grenzen
Kein genereller Beschnitt-, DPI-, ICC-, Codec- oder Kanalwert gilt ohne konkrete Spezifikation. Produktionsausgabe nur bei nachweislich passendem Validierungsprofil als bereit zur Freigabe bezeichnen.
