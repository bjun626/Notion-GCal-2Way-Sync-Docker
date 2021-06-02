# Notion-GCal-2Way-Sync Docker Build

Original code from [akarri2001/Notion-and-Google-Calendar-2-Way-Sync](https://github.com/akarri2001/Notion-and-Google-Calendar-2-Way-Sync) (2-June-2021)

The build image is at [docker hub](https://hub.docker.com/r/bjun626/notion_sync)


## Notion Page Template

The page template has to follow the convention on this notion [template](https://www.notion.so/47c0977120094511b0ab6cbf68b20c57?v=21c35762ede544818692acb1e8deefed)


## Docker Usage

1. Get your pickle file using [GCalToken.py](https://github.com/akarri2001/Notion-and-Google-Calendar-2-Way-Sync/blob/main/GCalToken.py) locally
1. Modify the [config.json](data/config.json) file with your parameter
1. Store the **config.json** & **token.pkl** at a directory (`/YOUR_PATH`)

2a. **Option 1**
1. Edit run.sh `/YOUR_PATH` with your path
1. Execute ``run.sh``

2b. **Option 2**
1. Execute `docker run -v /YOUR_PATH:/root/python/data bjun626/notion_sync`

## config.json Parameter

| Item | Description |
|------|-------------|
|TIME_ZONE|Your current time zone in +-hours|
|NOTION_TOKEN|the secret_something from Notion Integration|
|DATABASE_ID|get the mess of numbers before the "?" on your dashboard URL|
|CALENDAR_ID|The GCal calendar id. The format is something like "xxxxxxxxxxxxxxxxxxxxxxxxxx@groups.calendar.google.com"|
|TIME_ZONE_NAME|Choose your respective time zone: http://www.timezoneconverter.com/cgi-bin/zonehelp.tzc|
|TIME_ZONE_OFFSET|Offset Hours if the system time is not the correct time zone (Use this to offset docker time)|
|URL_ROOT|open up a task and then copy the URL root up to the "p="|
|DEFAULT_EVENT_LENGTH|This is how many minutes the default event length is. Feel free to change it as you please|
|DEFAULT_EVENT_START|8 would be 8 am. 16 would be 4 pm. Only whole numbers
|ALL_DAY_EVENT_OPTION|0 if you want dates on your Notion dashboard to be treated as an all-day event, 1 if you want dates on your Notion dashboard to be created at whatever hour you defined in the DEFAULT_EVENT_START variable|
|SLEEP_TIME|Amount of time (in sec) to run synchronization

