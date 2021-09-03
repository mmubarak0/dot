#!/usr/bin/env bash

vnstati -vs -i wwan0 -o ~/.summary.png
vnstat -i wwan0
# read -t 10
xdg-open ~/.summary.png

