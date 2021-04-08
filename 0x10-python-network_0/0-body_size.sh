#!/usr/bin/env bash
# gets body size

curl -s "$1" | wc -c
