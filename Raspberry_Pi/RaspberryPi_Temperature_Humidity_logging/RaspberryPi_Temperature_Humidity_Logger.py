"DHT22 Temperature and humidity sensor is used according to this blog: https://www.rototron.info/dht22-tutorial-for-raspberry-pi/"

import Adafruit_DHT
from time import sleep
import datetime
from utilities import *

sensorport=7
measurement_interval=60

targetFolder='/home/pi/Documents/Temperature_Humidity_logs'

NewFile=FileTweaks.LogFilenameGenerator(targetFolder,"temperature_humidity_log")

with open(NewFile, 'a') as f:
	f.write('Time;Temperature[degC];Humidity[%]\n')
while True:
	try:
		humidity, temperature= Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,sensorport)
	except:
		pass
	try:
		with open(NewFile, 'a') as f:
			linetowrite=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+';'+str(temperature)+';'+str(humidity)+'\n'
			f.write(linetowrite)
	except:
		pass
	sleep(measurement_interval)
