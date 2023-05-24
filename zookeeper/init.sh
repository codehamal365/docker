#!/bin/sh
set -e
cd /file

zkCli.sh create /data

zkCli.sh create /data "$(cat test.json)"
