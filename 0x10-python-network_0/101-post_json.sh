#!/bin/bash
# send a json post request to url
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
