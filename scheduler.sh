#!/bin/bash
# author: Jody LeSage
# creates a cronjob that scrapes data daily at midnight

(crontab -l 2>/dev/null; echo -n "0 0 * * * ";realpath scrapedata.sh) | crontab -
