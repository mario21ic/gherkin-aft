FROM python:3.5-slim

ENV DISPLAY=0
ENV SCREEN=0
ENV DISPLAY_MODE=1024x768x16
ENV APP_DIR=/app
ENV FF_VERSION="42.0"

RUN mkdir /app/
RUN apt-get update && apt-get install -y zlib1g-dev xvfb libxcomposite1 libasound2 libdbus-glib-1-2 libgtk2.0-0
RUN apt-get install -y wget
RUN wget "https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FF_VERSION}/linux-x86_64/en-US/firefox-${FF_VERSION}.tar.bz2" \
    -O /tmp/firefox.tar.bz2 && \
    tar xvf /tmp/firefox.tar.bz2 -C /opt && \
    ln -s /opt/firefox/firefox /usr/bin/firefox

COPY requirements.txt $APP_DIR
RUN cd $APP_DIR && pip install -r requirements.txt

WORKDIR $APP_DIR
