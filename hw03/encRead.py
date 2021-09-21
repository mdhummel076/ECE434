#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

pinA="P9_16"
pinB="P9_18"

count=0

GPIO.setup(pinA, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(pinB, GPIO.IN, GPIO.PUD_UP)

lastTime = time.time()

def counter(channel):
	global count, lastTime
	#print(lastTime - time.time())
	if(time.time() - lastTime > 0.2):
		if GPIO.input(pinB):
			count += 1
		else:
			count -= 1
		print(count)
	lastTime = time.time()

GPIO.add_event_detect(pinA, GPIO.FALLING, callback=counter)

try:
	while True:
		#GPIO.wait_for_edge(pinA, GPIO.FALLING)
		#counter(pinA)
		time.sleep(100)

except KeyboardInterrupt:
	print("Goodbye")
	GPIO.cleanup()
GPIO.cleanup()
