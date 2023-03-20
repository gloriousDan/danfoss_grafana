FROM alpine:3.17

RUN apk add --no-cache --update-cache python3 py3-sqlalchemy py3-pandas
WORKDIR /app
COPY  scraper_sqlite.py .

RUN printf "#!/bin/sh\ncd /app\npython /app/scraper_sqlite.py" > "/etc/periodic/15min/start_scraper"
RUN chmod +x "/etc/periodic/15min/start_scraper"
# CMD ["python", "scraper_sqlite.py"]
CMD ["sh", "-c" ,"/etc/periodic/15min/start_scraper", "&&", "/usr/sbin/crond", "-f", "-L", "/dev/stdout"]