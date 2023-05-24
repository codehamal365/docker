#!/bin/sh

cd $(dirname "$0")

for port in $(seq 7001 7006); do \
  mkdir -p ../"${port}"/conf \
  && PORT=${port} envsubst < ./redis-template.tmpl > ../"${port}"/conf/redis.conf \
  && mkdir -p ../"${port}"/data; \
done