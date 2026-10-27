# Primärquellen – technische Fähigkeiten

Stand/Abruf: 27.10.2026. Die Implementierungen verwenden eigene begrenzte Verfahren; Quellen sind keine Produktions- oder Rechtsfreigabe.

| Thema | Primärquelle | Bezug |
|---|---|---|
| SFTP / Batch / Readback | [OpenSSH sftp(1)](https://man.openbsd.org/sftp.1) | Prozessargumente, Batch-Abbruch, get/put/rename, IPv6 |
| SSH-Transportgrenzen | [OpenSSH ssh_config(5)](https://man.openbsd.org/ssh_config.5) | Host-Key-Prüfung, explizite Konfiguration, nicht interaktive Authentifizierung |
| IMAP | [Python imaplib](https://docs.python.org/3.9/library/imaplib.html) | Read-only-Auswahl, UID-Suche und Fetch; keine Expunge-/Löschaktionen |
| SMTP | [Python smtplib](https://docs.python.org/3.9/library/smtplib.html) | TLS, Empfängerablehnungen, technische Annahme, keine Zustellgarantie |
| PHP-Transport | [PHP mail()](https://www.php.net/manual/en/function.mail.php) | true bedeutet Annahme zum Transport, nicht tatsächliche Zustellung |
| Formulargrenzen | [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | Origin-Prüfung, signierte Token, keine Zustandsänderung durch GET |
| Apache-Redirects | [mod_alias / RedirectMatch](https://httpd.apache.org/docs/2.4/mod/mod_alias.html#redirectmatch) | Exakte Pfadregeln; Apache-spezifische Hostingvoraussetzungen |
| CI-Runtime | [GitHub Ubuntu-24.04-Runner](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md) | PHP-Laufzeitprüfungen; lokal kann PHP fehlen |
