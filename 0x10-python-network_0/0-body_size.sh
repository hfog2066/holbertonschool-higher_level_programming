#!/bin/bash
#curl body size
curl -so /dev/null -w '%{size_download}\n' "$1"
