#!/bin/bash

while true; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') mytest працює, каталог: $(pwd)" | tee -a /tmp/test.log
    sleep 60
done
