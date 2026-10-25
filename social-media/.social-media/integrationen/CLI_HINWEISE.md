# Lokaler Job-Preflight (ohne Netzwerk)

Mit `python3 .social-media/tools/validate_job.py .social-media/integrationen/BEISPIEL_JOB.json` kann eine neutrale Inhalts-/Schema-Vorprüfung ausgeführt werden. Das Skript **veröffentlicht nichts**, authentifiziert sich nirgends und hat keine Credentials. Ein Publishing-Dienst muss Format, Konto, Scopes, Richtlinien, Medien und Freigaben erneut prüfen.

Das optionale JSON-Schema kann mit einem JSON-Schema-Validator geprüft werden, ist aber keine Abhängigkeit des mitgelieferten Skripts. Ein Status `approved` oder `scheduled` darf erst nach tatsächlicher Freigabe bzw. Queue-/Plattformbestätigung persistiert werden.
