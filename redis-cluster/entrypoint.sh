#!/bin/sh
set -e

if [ "$1" = 'redis-cluster' ]; then
  redis-cli \
    --cluster create \
      $(dig redis1 +short):7001 \
      $(dig redis2 +short):7002 \
      $(dig redis3 +short):7003 \
    --cluster-yes
  sleep infinity
else
  exec "$@"
fi
