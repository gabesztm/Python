#
#https://www.youtube.com/watch?v=MCGeeqKfv7Q
#
import Adafruit_DHT
import BMP085
from time import sleep
import datetime
from utilities import *
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
import Adafruit_GPIO as GPIO
from Adafruit_GPIO import MCP230xx
from time import sleep

mcp=MCP230xx.MCP23017(busnum=1, address=0x20)		#io expander
mcp.setup(0,GPIO.IN)

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

sensorport=21
measurement_interval=60
checkbuttonfreq=3
measurementrepeat=5
pressure_sensor = BMP085.BMP085()
targetFolder='/home/pi/Documents/Temperature_Humidity_Pressure_logs'

NewFile=FileTweaks.LogFilenameGenerator(targetFolder,"temperature_humidity_log")

with open(NewFile, 'a') as f:
	f.write('Time;Temperature[degC];Humidity[%];Pressure[Pa]\n')
while True:
	temperatureList=[]
	humidityList=[]
	pressureList=[]
	for i in range(0,measurementrepeat):
		try:
			humidity, temperature= Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,sensorport)
			humidityList.append(round(float(humidity),2))
			temperatureList.append(round(float(temperature),2))
			pressure=pressure_sensor.read_pressure()
			pressureList.append(round(float(pressure),2))
		except:
			pass
	try:
		with open(NewFile, 'a') as f:
			linetowrite=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+';'+str(round(Statistics.ArithmeticMean(temperatureList),2))+';'+str(round(Statistics.ArithmeticMean(humidityList),2))+';'+str(round(Statistics.ArithmeticMean(pressureList),2))+'\n'
			f.write(linetowrite)
	except:
		pass
	for i in range(0,measurement_interval*checkbuttonfreq):
		sleep(1/checkbuttonfreq)
		if mcp.input(0):
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			draw.text((0,-2),"Temperature  "+str(round(Statistics.ArithmeticMean(temperatureList),2))+"  C" , fill=255)
			draw.text((0,10),"Humidity    "+str(round(Statistics.ArithmeticMean(humidityList),2))+"  %" , fill=255)
			draw.text((0,22),"Pressure "+str(round(Statistics.ArithmeticMean(pressureList),2))+"  Pa" , fill=255)
			disp.image(image)
			disp.display()
			sleep(4)
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			disp.image(image)
			disp.display()
