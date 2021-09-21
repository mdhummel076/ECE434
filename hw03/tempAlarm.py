#!/usr/bin/env python3

import smbus
import Adafruit_BBIO.GPIO as GPIO
import time

upper1 = 0x19
upper2 = 0x19
lower1 = 0x19
lower2 = 0x19

bus = smbus.SMBus(2)
address1 = 0x49
address2 = 0x4a

bus.write_byte_data(address1, 2, lower1)
bus.write_byte_data(address1, 3, upper1)
bus.write_byte_data(address2, 2, lower2)
bus.write_byte_data(address2, 3, upper2)

alarm1="P9_15"
alarm2="P9_13"

GPIO.setup(alarm1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(alarm2, GPIO.IN, GPIO.PUD_DOWN)

def alert(channel):
	if channel == alarm1:
		temp = bus.read_byte_data(address1, 0) * 1.8 + 32
		print("Alarm1 triggered at "+str(temp)+"F")
	elif channel == alarm2:
		temp = bus.read_byte_data(address2, 0) * 1.8 + 32
		#print("Alarm2 triggered at "+str(temp)+"F")

try:
	while True:
		if not GPIO.input(alarm1):
			alert(alarm1)
		elif not GPIO.input(alarm2):
			alert(alarm2)

except KeyboardInterrupt:
	print("Goodbye")
	GPIO.cleanup()
GPIO.cleanup()
