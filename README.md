# Installation
## Docker
1. Die [docker-compose.yml](https://github.com/gloriousDan/danfoss_grafana/blob/main/docker-compose.yml) Datei herunterladen 
2. Die [.env.sample](https://github.com/gloriousDan/danfoss_grafana/blob/main/.env.sample) Datei herunterladen und umbenennen zu `.env` und alle Parameter passend setzen.
3. `docker-compose up -d` baut das docker image und startet die Container
4. Weiter mit Schritt 7 aus Manuell

## Manuell
1. Virtuelles Environment erstellen: `python -m venv venv`
2. Virtuelles Environment aktivieren: `source venv/bin/activate`
3. requirements installieren: `pip install -r requirements.txt`
4. `.env.sample` zu `.env` kopieren und die Variablen passend setzen
5. Crontab erstellen um das script regelmäßig auszuführen `crontab -e`
   * Davor müssen die Variablen aus `.env` geladen werden:  
     `source .env && python scraper_sqlite.py`
6. grafana starten mit `docker-compose up -d grafana`
7. Einloggen mit login und password `admin`
8. In den Einstellungen die sqlite Datenbank als Datasource einstellen
9. das `example_dashboard.json` importieren


