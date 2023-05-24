FROM wiremock/wiremock:2.32.0-alpine

COPY ./supervisord/supervisord.conf /supervisord.conf

RUN apk update && \
    apk add --no-cache nginx~1.20.2 python3~3.9.5 py3-pip~20.3.4 && \
    pip3 install --upgrade pip --no-cache-dir && \
    pip3 install --no-cache-dir supervisor==4.2.2


CMD ["/usr/bin/supervisord", "-c", "/supervisord.conf"]