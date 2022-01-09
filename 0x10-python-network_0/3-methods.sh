#!/bin/bash
# display HTTP methods
curl -sI "$1" | grep -i allow | awk -F ': ' '{print $2}'
