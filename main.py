from Notion_GCal_2WaySync import main
import json
import time  # For sleeping
from datetime import datetime, timedelta, date

config_map = [
    "TIME_ZONE",            #Your current time zone in +-hours
    "NOTION_TOKEN",         #the secret_something from Notion Integration
    "DATABASE_ID",          #get the mess of numbers before the "?" on your dashboard URL
    "CALENDAR_ID",          #The GCal calendar id. The format is something like "sldkjfliksedjgodsfhgshglsj@groups.calendar.google.com"
    "TIME_ZONE_NAME",       # Choose your respective time zone: http://www.timezoneconverter.com/cgi-bin/zonehelp.tzc
    "TIME_ZONE_OFFSET",     # Offset Hours if system time is not the correct time zone
    "URL_ROOT",             #open up a task and then copy the URL root up to the "p="
    "DEFAULT_EVENT_LENGTH", #This is how many minutes the default event length is. Feel free to change it as you please
    "DEFAULT_EVENT_START",  # 8 would be 8 am. 16 would be 4 pm. Only whole numbers
    "ALL_DAY_EVENT_OPTION"  #0 if you want dates on your Notion dashboard to be treated as an all-day event
                            #^^ 1 if you want dates on your Notion dashboard to be created at whatever hour you defined in the DEFAULT_EVENT_START variable
]

if __name__ == '__main__':
    config = {}
    while(1):
        with open('./data/config.json') as json_file:
            config = json.load(json_file)
        time_now = datetime.now() + timedelta(hours=config['TIME_ZONE_OFFSET'])
        print(f'Time Now = {time_now.strftime("%H:%M:%S")}')
        main(
            config[config_map[0]],
            config[config_map[1]],
            config[config_map[2]],
            config[config_map[3]],
            config[config_map[4]],
            config[config_map[5]],
            config[config_map[6]],
            config[config_map[7]],
            config[config_map[8]],
            config[config_map[9]],
            )
        time.sleep(config['SLEEP_TIME'])
