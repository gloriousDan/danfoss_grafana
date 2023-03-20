FROM alpine:3.17

RUN apk add --no-cache --update-cache python3 py3-sqlalchemy py3-pandas tzdata
WORKDIR /app
COPY  scraper_sqlite.py .

RUN printf "#!/bin/sh\ncd /app\npython /app/scraper_sqlite.py" > "/etc/periodic/15min/start_scraper"
RUN printf "#!/bin/sh\nsh -c '/etc/periodic/15min/start_scraper' && /usr/sbin/crond -f -L /dev/stdout" > "/init.sh"
RUN chmod +x "/etc/periodic/15min/start_scraper" "/init.sh"
# CMD ["python", "scraper_sqlite.py"]
CMD ["sh", "-c", "/init.sh"]