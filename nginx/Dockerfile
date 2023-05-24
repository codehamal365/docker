FROM alpine:3.14 as deployment

#COPY ./nginx/nginx.conf /nginx.conf

RUN apk update && \
    apk add --no-cache nginx~1.20.2 nginx-mod-http-lua~1.20.2

EXPOSE 8080/tcp

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]