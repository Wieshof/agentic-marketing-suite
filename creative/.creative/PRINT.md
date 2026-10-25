# PRINT – automatisierte Printproduktion und Prüfregeln

## Architektur
**KI-Entwurf → parametrisches Layout → DTP-/PDF-Engine → technischer Preflight → gerenderter Sichtproof → Korrektur → gültiger Preflight → Freigabe.** Kein KI-basiertes Vollbild als alleinige Quelle für rechtsverbindliche Texte, Logos, Kleingedrucktes oder präzise Typografie.

## Mögliche Toolchain
- **Offen:** SVG + Python zum reproduzierbaren Aufbau einfacher Plakate/Anzeigen; Scribus/Scripter als DTP-Backend (CMYK, Satzspiegel, Seitenboxen, PDF-Export); `qpdf`, `pdfinfo`/`mutool`, Bildanalyse für Teilprüfungen.
- **Optional kommerziell:** InDesign/InDesign Server für komplexe Daten-/Katalogproduktionen, callas pdfToolbox oder gleichwertiger Industriestandard für Preflight/Color Conversion und reproduzierbare Prüfberichte.
- **Wichtig:** Programm/SVG-Export oder `pdfinfo` beweisen **nicht** PDF/X-Konformität, korrektes Überdrucken oder Druckfähigkeit. Dafür Profilvalidierung gegen reale Druckerei-/GWG-Anforderungen.

## Druckparameter – vor Freigabe zwingend
1. Druckerei/Druckverfahren/Material/Auflage/Format/Ausrichtung und Verarbeitung; Sonderfarben/Stanzkonturen/Falze.
2. TrimBox/BleedBox/MediaBox, geforderter Beschnitt und Sicherheitsabstände; Beschnittwerte druckereispezifisch (z.B. 3 mm **nur** als häufiges Beispiel).
3. ICC-Ausgabeprofil/Output Intent, CMYK-/Sonderfarbenanforderungen, Transparenz-/Überdruckverhalten, Farbauftrag-Grenzen.
4. Tatsächliche effektive Rasterauflösung bei Platzierung; keine starre 300-dpi-Regel bei allen Materialien/Großformaten.
5. Schriftdateien mit korrekter Lizenz, eingebettet/subset, keine fehlenden Glyphen/Textüberläufe.
6. PDF/X-Konformität entsprechend **vereinbartem** Standard, bevorzugt PDF/X-4 **nur wenn akzeptiert**; GWG-spezifische Profile bei Bedarf.
7. Proof auf korrekte Texte, Logos, Barcodes, Markenfarben, Sicherheitszone, Falz/Anschnitt, Überdruck und Stand.

## Statusdisziplin
`SVG-Proof erstellt` ≠ `Druck-PDF erstellt` ≠ `PDF/X-Preflight bestanden` ≠ `Druckfreigabe` ≠ `Druckauftrag erfolgt`.

## Serienprint / Variable Data
Datenquelle CSV/JSON mit geprüften Spalten, Datentypen und Zeichensätzen; Textlängen-Fallback/Überlaufkontrolle, zeilenbezogener Export und Report. Personenbezogene Daten minimieren; Versand/Bestellung nur mit separater Freigabe.
