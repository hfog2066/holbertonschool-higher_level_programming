#!/bin/bash
# script that sends request to url passed argument.
curl -so /dev/null -w "%{http_code}" "$1"
