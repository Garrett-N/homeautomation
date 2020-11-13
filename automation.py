"""
Simple program to turn my outside lights on/off at sunset/sunrise
I need something quick to replace ifttt
"""

import os
import datetime
from suntime import Sun, SunTimeException
import pytz
import socket

# my location
lat = 42
long = -88.2 
sun = Sun(lat, long)

# my devices now have hostnames on my network
# the ouimeaux only works with IP addresses so 
# i need to get the ip addresses
plug2_ip = socket.gethostbyname("plug2")
porch_ip = socket.gethostbyname("porch")
patio_ip = socket.gethostbyname("patio")

# client commands that will be executed 
plug2_on = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device " + plug2_ip + " --on"
porch_on = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device " + porch_ip + " --on"
porch_off = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device " + porch_ip + " --off"
patio_on = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device " + patio_ip + " --on"
patio_off = "/usr/bin/python3 /home/gman/ouimeaux/client.py --device " + patio_ip + " --off"

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
