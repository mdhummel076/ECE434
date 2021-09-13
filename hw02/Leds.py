#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

button1="P9_16"
button2="P9_17"
button3="P9_19"
button4="P9_21"

led1="P8_8"
led2="P8_10"
led3="P8_12"
led4="P8_14"

map = {button1: led1, button2: led2, button3: led3, button4: led4}

GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

def updateLED(channel):
	state = GPIO.input(channel)
	print("Channel "+channel+" = "+str(state))
	GPIO.output(map[channel], state)
	
GPIO.add_event_detect(button1, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button2, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=updateLED)

try:
	while True:
		time.sleep(100)
		
except KeyboardInterrupt:
	print("Goodbye")
	GPIO.cleanup()
GPIO.cleanup()
