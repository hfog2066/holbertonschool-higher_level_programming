#!/bin/bash
# show methods
curl -sI "$1"| grep Allow | cut -d' ' -f2-
