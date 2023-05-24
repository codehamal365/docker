FROM redis:6.2.5-alpine

RUN apk update && apk add bind-tools=9.16.25-r0
COPY ./redis-cluster/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
CMD ["redis-cluster"]

HEALTHCHECK --interval=5s CMD redis-cli --cluster call redis1:7001 PING || exit 1