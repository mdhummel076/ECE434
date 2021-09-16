#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

pin="P9_12"

GPIO.setup(pin, GPIO.OUT)

state = True

print("Running")

try:
	while True:
		state = not state
		GPIO.output(pin, state)

except KeyboardInterrupt:
	print("Goodbye")
	GPIO.cleanup()
GPIO.cleanup()
