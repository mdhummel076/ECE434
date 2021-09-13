#!/usr/bin/env python3

import os
import time
import curses
from curses import wrapper
import Adafruit_BBIO.GPIO as GPIO

def displayBoard(gameSize, board, screen):

	screen.clear()
	for i in range(gameSize):
		for j in range(gameSize):
			screen.addch(i*2, j*3, board[j][i])
	screen.addstr(gameSize*2+2, 0, "Use arrow keys to move, c to clear board, and q to exit")
			
def resetBoard(gameSize, board, screen):
	
	board = [['.' for i in range(gameSize)] for j in range(gameSize)]
	
	return board
	

def main(screen):

	global gameSize
	global cursor
	global board

	curses.cbreak()
	screen.nodelay(True)
	screen.keypad(True)

	GPIO.add_event_detect(button1, GPIO.RISING, callback=updateCursor)
	GPIO.add_event_detect(button2, GPIO.RISING, callback=updateCursor)
	GPIO.add_event_detect(button3, GPIO.RISING, callback=updateCursor)
	GPIO.add_event_detect(button4, GPIO.RISING, callback=updateCursor)

	try:
		displayBoard(gameSize, board, screen)
	except:
		print("Incompatible board size")
		raise ValueError("Incompatible board size")
	#Main loop
	while(True):
		char = screen.getch()
		if char == 113: break
		elif char == curses.KEY_UP: cursor[1] = cursor[1] - 1
		elif char == curses.KEY_LEFT: cursor[0] = cursor[0] - 1
		elif char == curses.KEY_RIGHT: cursor[0] = cursor[0] + 1
		elif char == curses.KEY_DOWN: cursor[1] = cursor[1] + 1
		elif char == 99: board = resetBoard(gameSize, board, screen)
		
		if cursor[0] > gameSize - 1:
			cursor[0] = gameSize - 1
		elif cursor[0] < 0:
			cursor[0] = 0
			
		if cursor[1] > gameSize - 1:
			cursor[1] = gameSize - 1
		elif cursor[1] < 0:
			cursor[1] = 0
		
		board[cursor[0]][cursor[1]] = 'x'
	
		displayBoard(gameSize, board, screen)
		
		time.sleep(0.1)
		
gameSize = int(input("What size would you like the game to be?"))

cursor = [int(gameSize/2), int(gameSize/2)]

#Make the board

board = [['.' for i in range(gameSize)] for j in range(gameSize)]

screen = curses.initscr()

button1="P9_16"
button2="P9_17"
button3="P9_19"
button4="P9_21"

GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, GPIO.PUD_DOWN)

def updateCursor(channel):
	
	global gameSize
	global cursor
	global board
	global screen
	
	if channel == button1: cursor[1] = cursor[1] - 1;
	elif channel == button2: cursor[0] = cursor[0] - 1
	elif channel == button3: cursor[0] = cursor[0] + 1
	elif channel == button4: cursor[1] = cursor[1] + 1
	
	if cursor[0] > gameSize - 1:
		cursor[0] = gameSize - 1
	elif cursor[0] < 0:
		cursor[0] = 0
	
	if cursor[1] > gameSize - 1:
		cursor[1] = gameSize - 1
	elif cursor[1] < 0:
		cursor[1] = 0

	board[cursor[0]][cursor[1]] = 'x'
	
	displayBoard(gameSize, board, screen)
		
try:
	wrapper(main)
except Exception as error:
	print(repr(error))
	GPIO.cleanup()
GPIO.cleanup()
