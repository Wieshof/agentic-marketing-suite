# noCMS — STRUCTUR.md

**Strukturkarte der Website: Seiten, Layouts, gemeinsame Bausteine und Ausnahmen**  
**Spezifikationsstand:** v0.1  
**Ablage im Projekt:** `.nocms/STRUCTUR.md`  
**Projektstatus:** `VORLAGE — noch nicht anhand einer konkreten Website ausgefüllt`  
**Zuletzt mit `site/` abgeglichen:** offen

> **Grundsatz:** `site/` enthält die tatsächlich lauffähige Website. Diese Datei erklärt ihre Struktur, dokumentiert gemeinsame Elemente und dient der KI als Such- und Prüfgrundlage. Sie ersetzt **niemals** die Prüfung der vorhandenen HTML-Dateien.

## 1. Zweck, Zuständigkeit und Geltungsbereich

Diese Datei ist **die projektspezifische Karte einer noCMS-Website**. Sie beantwortet insbesondere:

- Welche Seiten gibt es, unter welchen Pfaden und URLs sind sie erreichbar?
- Welche Layouts verwenden die Seiten (z. B. Standardseite oder Landingpage)?
- Wie sind Header, Navigation, Main, Sidebar und Footer angeordnet?
- Welche Elemente sind gemeinsam, wo liegen ihre Quellen und auf welchen Seiten werden sie verwendet?
- Welche Seiten weichen bewusst vom Standard ab?
- Welche CSS-, JavaScript- und Mediendateien sind für die Struktur wichtig?
- Welche anderen Seiten oder Komponenten müssen bei einer Änderung mitgeprüft werden?

**Arbeitsteilung:**

| Datei / Ort | Zuständigkeit |
| --- | --- |
| `AGENT.md` | Verbindliche Arbeitsweise der ausführenden KI, inklusive Suche, Änderung und Prüfung |
| `.nocms/ONBOARDING.md` | Anleitung für das adaptive Briefinggespräch |
| `.nocms/BRIEFING.md` | Bestätigte Ziele, Anforderungen, Zielgruppen und Gestaltungsentscheidungen |
| **`.nocms/STRUCTUR.md`** | Tatsächliche Seiten-, Layout- und Komponentenstruktur sowie dokumentierte Ausnahmen |
| `.nocms/ARCHITECTURE.md` | Technische Entscheidungen und ihre Gründe |
| `.nocms/RULES.md` | Zusätzliche projektspezifische Vorgaben |
| `.nocms/STATE.md` | Aktueller Arbeitsstand und offene Probleme |
| `site/` | Direkt veröffentlichbare HTML-, CSS-, JS- und Mediendateien |
| `shared/` | Optionale zentrale HTML-Quellen mehrfach verwendeter Bausteine; **nicht öffentlich** |

**Priorität bei Abweichungen:** Der tatsächliche Inhalt in `site/` zeigt, was implementiert ist; `BRIEFING.md` und `RULES.md` zeigen, was vereinbart wurde. Stimmen beide nicht überein, ist dies ein zu klärender Unterschied — kein Anlass für stillschweigende Überschreibungen.

## 2. Projektübersicht (bei Einrichtung ausfüllen)

| Eigenschaft | Projektspezifischer Eintrag |
| --- | --- |
| Projekt / Website | `OFFEN` |
| Basisverzeichnis der öffentlichen Website | `site/` |
| Öffentliche Basis-URL / Hosting-Unterpfad | `OFFEN` |
| Sprachen / Sprachpfade | `OFFEN` |
| Stand der Strukturinventur | `NICHT ERFASST` |
| Anzahl erfasster HTML-Seiten | `OFFEN` |
| Anzahl Layoutvarianten | `OFFEN` |
| Letzte vollständige HTML-Suche / Prüfung | `OFFEN` |
| Besondere Einschränkungen | `OFFEN` |

**Regel:** `OFFEN` und `NICHT ERFASST` sind ausdrücklich keine Freigabe, Werte oder Strukturen zu erfinden. Bei der Einrichtung prüft die KI die realen Dateien und ersetzt die Platzhalter durch belegbare Einträge. Sind noch keine Seiten vorhanden, beschreibt sie die **geplante** Struktur getrennt vom implementierten Ist-Zustand.

## 3. Seitenverzeichnis und Navigation

Pflege eine **vollständige Liste der real vorhandenen HTML-Seiten**. Für jede Seite sind Dateipfad, veröffentlichte URL (soweit bekannt), Layouttyp, Navigation und wichtige Ausnahmen zu erfassen. Eine Sitemap aus dem Briefing ist zunächst nur ein **Plan**, nicht der Nachweis einer implementierten Seite.

### 3.1 Ist-Zustand: Tatsächlich vorhandene Seiten

| Seiten-ID | Datei unter `site/` | Öffentliche URL | Layout | Navigation / Verweise | Ausnahmen / Status |
| --- | --- | --- | --- | --- | --- |
| *Noch nicht inventarisiert* | — | — | — | — | — |

**Konventionen:**

- Verwende für Seiten eindeutige, beständige IDs, etwa `home`, `services`, `contact` oder `campaign-spring`.
- Dokumentiere den **Dateipfad** und die **URL** getrennt; die URL kann von Hosting- oder Weiterleitungsregeln abhängen.
- Beispielsweise *kann* `site/leistungen/index.html` unter `/leistungen/` erreichbar sein — überprüfe das tatsächliche Deployment.
- Beziehe auch versteckte, nicht in der Navigation verlinkte Landingpages, Fehlerseiten und Sprachvarianten ein, sofern sie zur Website gehören.
- Erfasse Seiten, die absichtlich nicht in der Navigation erscheinen, ausdrücklich als Ausnahme.
- Wenn eine bestehende URL verändert wird, dokumentiere notwendige Weiterleitungen und prüfe eingehende Links, soweit möglich.

### 3.2 Geplante, noch nicht umgesetzte Seiten

| Geplante Seite | Vorgesehene URL | Anlass / Quelle | Status |
| --- | --- | --- | --- |
| *Keine erfasst* | — | — | — |

### 3.3 Navigation und Seitenbeziehungen

Trage hier die tatsächlich verwendete primäre und gegebenenfalls sekundäre Navigation ein. Halte außerdem strukturelle Beziehungen fest, die bei Änderungen betroffen sein können: Breadcrumbs, Footer-Links, CTA-Verweise, verwandte Inhalte, Sprachwechsel und besondere Landingpage-Einstiege.

- **Hauptnavigation:** `OFFEN`
- **Footer-Navigation:** `OFFEN`
- **Weitere Navigationsbereiche:** `OFFEN`
- **Spezielle Verweisregeln und Ausnahmen:** `OFFEN`

## 4. Layoutvarianten und Regionen

Ein **Layout** beschreibt die übliche Anordnung von Bereichen einer Seite. Es ist in noCMS zunächst eine **dokumentierte Konvention**, kein verpflichtendes Template, keine Runtime und keine vorgeschriebene Build-Transformation. Die HTML-Dateien in `site/` sind vollständig und eigenständig veröffentlichbar.

### 4.1 Layoutregister (tatsächliches Projekt)

| Layout-ID | Zweck | Regionen in Reihenfolge | Gilt für | Ausnahmen |
| --- | --- | --- | --- | --- |
| *Noch nicht erfasst* | — | — | — | — |

### 4.2 Illustratives Beispiel — **nicht** als tatsächlich implementiert behandeln

**`default` — Standardseite**

```text
<body>
  Header                 [gemeinsam: header-default]
  Navigation             [gegebenenfalls Teil des Headers]
  Main                   [individueller Seiteninhalt]
  Sidebar                [optional; seitenspezifisch]
  Footer                 [gemeinsam: footer-default]
</body>
```

**`landing` — Landingpage**

```text
<body>
  Landing-Header         [gemeinsam: header-landing oder individuell]
  Main
    Hero                 [individuell]
    Vorteile / Inhalt    [individuell]
    Call-to-Action       [individuell]
  Footer                 [gemeinsam: footer-default]
</body>
```

Mögliche Unterschiede: keine Hauptnavigation, keine Sidebar, eigener Header, andere Reihenfolge von Abschnitten, besondere CTA-Führung oder reduzierte Footer-Navigation. Solche Abweichungen sind **keine Fehler**, wenn sie dokumentiert und mit dem Briefing vereinbar sind.

### 4.3 Layoutbeschreibung pro tatsächlich verwendetem Typ

Für jede Layout-ID aus Abschnitt 4.1 dokumentieren:

- **Zweck:** Für welche Art von Seiten ist das Layout gedacht?
- **Regionen:** Welche Bereiche sind vorhanden, optional oder ausgeschlossen?
- **Komponenten:** Welche gemeinsamen Bausteine gehören zum Layout?
- **Gestaltung:** Welche relevanten CSS-Dateien, Klassen oder Konventionen gelten?
- **Verhalten:** Welche JS-Module oder Interaktionen sind layoutgebunden?
- **Ausnahmen:** Welche Seiten weichen bewusst ab und warum?

Nur belegbare Informationen eintragen. Keine überflüssige Verdoppelung von CSS- oder HTML-Code in diese Datei kopieren.

## 5. Gemeinsame HTML-Bausteine (`shared/`)

Ein gemeinsamer Baustein ist beispielsweise ein Header, Footer, eine Navigation, ein Kontaktblock oder ein wiederkehrender CTA. **Bei mehrfacher Verwendung empfiehlt sich eine zentrale Quelle in `shared/`**, etwa `shared/header.html`; die HTML-Seiten erhalten dennoch jeweils den vollständigen Baustein. Der Webserver benötigt `shared/` nicht.

### 5.1 Komponentenregister (tatsächliches Projekt)

| Komponenten-ID | Zentrale Quelle oder Referenz | Verwendung / Layouts | Besondere Varianten und Ausnahmen |
| --- | --- | --- | --- |
| *Noch nicht erfasst* | — | — | — |

Für jeden registrierten Baustein gilt:

- **Kennung:** Eindeutig und in `STRUCTUR.md` sowie in den HTML-Kommentaren gleich geschrieben.
- **Quelle:** Projektrelativer Pfad, beispielsweise `shared/header.html`, oder dokumentierte **Referenzseite**, falls kein `shared/` verwendet wird.
- **Geltungsbereich:** Layouts und **konkrete Seiten**, auf denen der Baustein vorkommt; die Liste darf eine zusätzliche projektweite Suche nicht ersetzen.
- **Varianten:** Beispiel `header-default` und `header-landing` getrennt führen, wenn sie unabhängig geändert werden dürfen.
- **Abhängigkeiten:** Relevante CSS-, JS-, Medien- oder andere Verweise nur soweit nötig benennen.

### 5.2 Markierung gemeinsamer Regionen in HTML

**Empfohlene einfache Markierung:**

```html
<!-- nocms:begin header-default -->
<header class="site-header">
  <a href="/">Beispielmarke</a>
  <nav aria-label="Hauptnavigation">
    <!-- Navigation der konkreten Website -->
  </nav>
</header>
<!-- nocms:end header-default -->
```

Dabei gelten diese Regeln:

1. Der Text nach `nocms:begin` bzw. `nocms:end` ist die **exakte Komponenten-ID** aus dem Register.
2. Beginn und Ende müssen in derselben HTML-Datei vorhanden, eindeutig zuordenbar und korrekt angeordnet sein.
3. Der Bereich **zwischen** beiden Markierungen kann gezielt ersetzt werden. Die Markierungen selbst bleiben stehen.
4. Verwende eine Komponenten-ID nicht für inhaltlich unterschiedliche Varianten. Gib Varianten eigene Kennungen.
5. Verwende keine überlappenden Markierungsbereiche; verschachtelte Komponenten nur nach ausdrücklicher projektspezifischer Regel und mit gesonderter Prüfung.
6. Nicht betroffene Inhalte außerhalb der Markierung bleiben unverändert. **Zusätzliche `editable`-Markierungen sind nicht nötig.**
7. Kommentare sind **Orientierungs- und Austauschgrenzen**, kein dynamisches Include. HTML muss ohne noCMS-Runtime funktionieren.

Die Datei in `shared/` enthält in der Regel den **HTML-Inhalt** des Bausteins ohne äußere `nocms:begin`-/`nocms:end`-Kommentare. Deren Position liegt jeweils in den vollständigen HTML-Seiten. Halte mögliche Abweichungen von dieser Konvention hier fest.

### 5.3 Illustratives Komponentenverzeichnis — **kein Ist-Zustand**

| Komponenten-ID | Quelle | Beispielverwendung | Bemerkung |
| --- | --- | --- | --- |
| `header-default` | `shared/header.html` | Standardseiten | Hauptnavigation enthalten |
| `header-landing` | `shared/landing-header.html` | Landingpages | Reduzierte Navigation |
| `footer-default` | `shared/footer.html` | Standard- und Landingpages | Gemeinsame rechtliche Links |

**Beispiele sind vor Einsatz mit den tatsächlichen Dateien abzugleichen.** Es besteht keine Pflicht, alle genannten Komponenten anzulegen.

## 6. Zentrale CSS-, JS- und Medienressourcen

Die Website besteht nicht nur aus HTML. Erfasse **strukturrelevante** gemeinsame Ressourcen, damit bei einer Änderung die betroffenen Seiten gefunden werden.

| Ressource / Pfad | Aufgabe | Genutzt durch | Besondere Abhängigkeit |
| --- | --- | --- | --- |
| *Noch nicht erfasst* | — | — | — |

Typische Kategorien sind globale Gestaltung, Komponentenstyles, Layoutstyles, Navigation, Interaktionen, Schriftdateien, Logos und wiederverwendete Bildmaterialien. Spezifische technische Entscheidungen gehören nach `.nocms/ARCHITECTURE.md`; hier reichen auffindbare Pfade und ihre Verwendungen.

**Wichtig:** Die Quellpfade aus `shared/` sind nicht automatisch öffentliche Ressourcen. Wenn CSS, JavaScript oder Medien für den Browser benötigt werden, müssen sie in der veröffentlichten Website (`site/`) vorhanden und von den HTML-Seiten korrekt referenziert sein.

## 7. Ausnahmen und bewusste Abweichungen

Registriere Abweichungen, die bei einer pauschalen Änderung **nicht** vereinheitlicht werden dürfen.

| Seite / Seiten-ID | Standard / Baustein | Abweichung | Grund / Quelle | Prüffolge |
| --- | --- | --- | --- | --- |
| *Keine erfasst — noch zu prüfen* | — | — | — | — |

Beispiele für dokumentationswürdige Abweichungen:

- Landingpage ohne Hauptnavigation oder mit eigenem Header;
- Seite ohne Sidebar oder mit anderer Spaltenstruktur;
- abweichender Footer für eine Kampagne;
- länderspezifische Kontakt- oder Rechtshinweise;
- besondere Navigation für eine Sprachversion;
- absichtlich nicht veröffentlichte oder nicht indexierbare Seite.

**Keine stillen Sonderfälle:** Wenn eine Ausnahme bei der Arbeit entdeckt wird, kläre ihren Zweck. Besteht sie berechtigt, dokumentiere sie; andernfalls plane eine Korrektur anhand des Briefings.

## 8. Verbindlicher Ablauf für strukturrelevante Änderungen

Die konkreten Arbeitsanweisungen stehen in `../AGENT.md`. Für diese Strukturkarte gelten folgende Schritte als **Prüfkontrakt**, ohne dass ein eigenes noCMS-Programm erforderlich ist:

1. **Änderung verstehen:** Welche Seiten, Layouts, Komponenten, Styles, Skripte und Ausnahmen können betroffen sein?
2. **Soll ermitteln:** Lies die zutreffenden Abschnitte aus `BRIEFING.md`, `RULES.md` und diesem Register.
3. **Ist ermitteln:** Durchsuche **alle HTML-Dateien unter `site/`** nach relevanten `nocms`-Markierungen und — unabhängig davon — nach möglichen unmarkierten Vorkommen, Klassen, IDs oder Strukturmustern.
4. **Abweichungen untersuchen:** Stimmen Register, Markierungen, tatsächliche HTML-Struktur und eventuelle zentrale Quellen überein? Bei Unklarheit nicht blind ersetzen.
5. **Gezielt ändern:** Bei zentralen HTML-Quellen diese zuerst aktualisieren; dann **nur die passenden markierten Regionen** in den betreffenden Seiten ersetzen. Ohne Marker den konkreten HTML-Kontext prüfen und sorgfältig bearbeiten.
6. **Ausnahmen schützen:** Layout- oder seitenbezogene Sonderfälle nicht versehentlich vereinheitlichen. Keine Inhaltsbereiche außerhalb des Änderungsauftrags überschreiben.
7. **Alle betroffenen Seiten prüfen:** Nach einer gemeinsamen Änderung **jede tatsächliche Verwendung** kontrollieren, auch wenn sie nicht im Register stand. Prüfe relevante HTML-, CSS-, JS-, Verweis- und Darstellungsfolgen.
8. **Erneut suchen:** Keine veralteten Vorkommen, falschen IDs, fehlenden Endmarkierungen oder widersprüchlichen Varianten zurücklassen. Prüfe auch die Vollständigkeit der dokumentierten Seitenliste.
9. **Dokumentation abgleichen:** Aktualisiere Seitenregister, Layouts, Komponentenverwendungen, Abhängigkeiten und Ausnahmen, soweit betroffen; erfasse offene Abweichungen in `STATE.md`.
10. **Ergebnis berichten:** Sage ausdrücklich, welche Seiten geprüft wurden und ob die Prüfung vollständig war. Falls nicht, kennzeichne den Auftrag als nur teilweise validiert.

### 8.1 Beispiel einer Suche (optional; kein vorgeschriebenes Werkzeug)

Falls `rg`/ripgrep verfügbar ist:

```bash
# Markierte Verwendungen eines bestimmten Bausteins finden
rg -n --glob '*.html' 'nocms:(begin|end) header-default' site/

# Potenzielle unmarkierte Header zusätzlich finden
rg -n --glob '*.html' '<header\b|site-header' site/

# HTML-Dateien für die Seiteninventur auflisten
rg --files site/ -g '*.html'
```

Ein anderes geeignetes Dateiwerkzeug ist gleichwertig. Ein Suchtreffer allein beweist weder die korrekte Verwendung noch die vollständige Synchronisierung. Prüfe den Kontext und die betroffenen Dateien.

### 8.2 Umgang mit defekten oder fehlenden Markierungen

- **Fehlender Beginn / fehlendes Ende:** Nicht über Dateigrenzen hinweg ersetzen; Fehler dokumentieren und vorsichtig korrigieren.
- **Doppelte, widersprüchliche ID:** Verwendungszweck und Komponentengrenzen klären, gegebenenfalls Varianten trennen.
- **Baustein ohne Marker:** Per HTML-Struktur und dokumentierter Seitenliste finden; bei sinnvoller Wiederverwendung Marker ergänzen.
- **Dokumentierte, aber nicht vorhandene Seite:** Als entfernt, geplant oder fehlerhaft dokumentiert kennzeichnen — nicht ungefragt wiederherstellen.
- **Gefundene, aber nicht dokumentierte Seite:** In das Seitenregister aufnehmen, nachdem Zweck und Veröffentlichungsstatus geklärt sind.
- **Fehlende zentrale Quelle:** Nicht automatisch eine beliebige HTML-Instanz zum Standard erklären. Gemeinsame Fassung aus Briefing, Varianten und bestehenden Seiten ableiten und bestätigen, falls nötig.

## 9. Pflege dieser Datei

Aktualisiere `STRUCTUR.md` insbesondere nach:

- Anlegen, Löschen, Verschieben oder Umbenennen einer Seite;
- Änderung der URL-, Navigations- oder Sprachstruktur;
- Einführung, Änderung oder Entfernung einer Layoutvariante;
- Hinzufügen, Aufspalten oder Zusammenführen gemeinsamer Komponenten;
- Einführung oder Aufhebung einer dokumentierten Layoutausnahme;
- wesentlichen Änderungen gemeinsam genutzter Stylesheets, Skripte oder Ressourcen.

**Nicht erforderlich:** Für eine reine Rechtschreibkorrektur im individuellen Inhalt einer Seite muss dieses Dokument normalerweise nicht verändert werden, wenn die Struktur unverändert bleibt.

Bei Strukturänderungen müssen auch `.nocms/STATE.md` und — bei relevanten Änderungen — `.nocms/HISTORY/` aktualisiert werden. Projektentscheidungen und technische Hintergründe gehören gegebenenfalls in `.nocms/ARCHITECTURE.md`. Wiederhole hier nicht den vollständigen Änderungsverlauf.

### Prüfvermerk für eine abgeschlossene Strukturinventur

```text
Prüfdatum: OFFEN
Geprüfter Dateistand / Version: OFFEN
HTML-Dateien unter site/ insgesamt: OFFEN
Seitenregister vollständig abgeglichen: NEIN / OFFEN
Komponentenmarker und Zuordnungen geprüft: NEIN / OFFEN
Layoutausnahmen geprüft: NEIN / OFFEN
Abweichungen / offene Punkte: OFFEN
Prüfende KI / verwendete Werkzeuge (soweit bekannt): OFFEN
```

Dieser Vermerk darf nur nach einer **tatsächlich durchgeführten** Prüfung aktualisiert werden. Vermutungen und reine Dokumentationslektüre gelten nicht als vollständiger Abgleich.

---

**Leitsatz:** Beschreibe die reale Website. Kennzeichne gemeinsame Bausteine. Schütze bewusste Ausnahmen. Suche vor Änderungen vollständig und prüfe nach Änderungen jede betroffene Seite.
