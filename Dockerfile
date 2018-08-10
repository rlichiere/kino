FROM python:2.7.13
MAINTAINER Remi LICHIERE <remi.lichiere@visiativ.com>

ARG ENV2BUILD=kino
ENV IMGTYPE=$ENV2BUILD

RUN apt-get update && apt-get install -y wget \
                  libjpeg62-turbo-dev \
                  libapparmor1 \
                  libsystemd-journal0 \
                  libsasl2-dev \
                  libldap2-dev \
                  libssl-dev \
                  gettext \
                  mysql-client libmysqlclient-dev \
                  freetds-dev \
                  postgresql-client libpq-dev \
                  sqlite3 \
       --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV PROVDIR=/usr/src/app

RUN mkdir -p $PROVDIR

WORKDIR $PROVDIR

COPY requirements.txt $PROVDIR
RUN pip install  -r requirements.txt

COPY . $PROVDIR

RUN mkdir -p /var/log/supervisor  /etc/supervisor
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Admin Settings
ENV ADMIN_USER='admin' \
    ADMIN_EMAIL='admin@example.com' \
    ADMIN_PASSWORD='admin123456'

#Database Settings
ENV DB_NAME='kinodb' \
    DB_HOST='mysql' \
    DB_USER='mysql' \
    DB_PASS='mysql'

COPY app-start.sh /app-start.sh
RUN chmod +x /app-start.sh

EXPOSE 8000
VOLUME ["/data/kino"]

CMD ["/usr/local/bin/supervisord", "--nodaemon", "--configuration", "/etc/supervisor/supervisord.conf"]
