# Installation

1. Virtuelles Environment erstellen: `python -m venv venv`
2. Virtuelles Environment aktivieren: `source venv/bin/activate`
3. requirements installieren: `pip install -r requirements.txt`
4. FTP Parameter im Python script passend setzen 
5. Crontab erstellen um das script regelmäßig auszuführen `crontab -e`
6. grafana starten mit `docker-compose up -d`
7. Einloggen mit login und password `admin`
8. In den Einstellungen die sqlite Datenbank als Datasource einstellen
9. das `example_dashboard.json` importieren
