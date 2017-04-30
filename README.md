# Team++ Criminal Common Operating Picture

## Getting started

1. Begin with a fresh install of a debian-based linux distribution (Mint/Ubuntu/Kali)
2. Run setup.sh  This installs dependencies in a Python virtual environment and builds an empty database
3. Run scrapedata.sh to pull data from the endpoints into the database
4. Run scheduler.sh to schedule a cron job that scrapes new data daily at midnight
5. Run init_host.sh to start the local server on port 5000
