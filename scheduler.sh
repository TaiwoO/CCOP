#!/bin/bash

(crontab -l 2>/dev/null; echo -n "0 0 * * * ";realpath scrapedata.sh) | crontab -
