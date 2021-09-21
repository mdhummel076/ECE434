#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

bus = smbus.SMBus(2)
matrix = 0x70

Al="P9_16"
Bl="P9_18"
Ar="P9_21"
Br="P9_23"

GPIO.setup(Al, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Bl, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Ar, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Br, GPIO.IN, GPIO.PUD_UP)

gameSize = 8

cursor = [3, 3]

board = [0x00 for i in range(8)]

lastTime = time.time()

def updateCursor(channel):
	global cursor, lastTime
	if(time.time() - lastTime > 0.2):
		if channel == Al:
			if not GPIO.input(Bl):
				cursor[0] += 1
			else:
				cursor[0] -= 1
			if cursor[0] > 7:
				cursor[0] = 7
			elif cursor[0] < 0:
				cursor[0] = 0
		elif channel == Ar:
			if GPIO.input(Br):
				cursor[1] += 1
			else:
				cursor[1] -= 1
			if cursor[1] > 7:
				cursor[1] = 7
			elif cursor[1] < 0:
				cursor[1] = 0
		lastTime = time.time()

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

GPIO.add_event_detect(Al, GPIO.FALLING, callback=updateCursor)
GPIO.add_event_detect(Ar, GPIO.FALLING, callback=updateCursor)

try:
	while True:
		board[cursor[0]] |= 1 << cursor[1]

		display = [0x00, board[0], 0x00, board[1], 0x00, board[2], 0x00, board[3], 0x00, board[4], 0x00, board[5], 0x00, board[6], 0x00, board[7]]

		bus.write_i2c_block_data(matrix, 0, display)

		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Goodbye")
GPIO.cleanup()


