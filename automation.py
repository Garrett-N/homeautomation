"""
Simple program to turn my outside lights on/off at sunset/sunrise
I need something quick to replace ifttt
"""

import os
import datetime
from suntime import Sun, SunTimeException
import pytz

# my location
lat = 42
long = -88.2 
sun = Sun(lat, long)

# hardcoded things for now
plug2_on = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device 10.0.0.51 --on"
porch_on = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device 10.0.0.39 --on"
porch_off = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device 10.0.0.39 --off"
patio_on = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device 10.0.0.122 --on"
patio_off = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device 10.0.0.122 --off"

sunrise = sun.get_local_sunrise_time()
sunset = sun.get_local_sunset_time()
now = datetime.datetime.now(pytz.utc)

from_sunset = abs(sunset - now)
from_sunrise = abs(sunrise - now)

# turn on lights at sunset
if from_sunset < datetime.timedelta(minutes=5):
	os.system(porch_on)
	os.system(patio_on)

# turn off lights at sunrise
if from_sunrise < datetime.timedelta(minutes=5):
	os.system(porch_off)
	os.system(patio_off)
