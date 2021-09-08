#!/usr/bin/env python3

import os
import time
import curses
from curses import wrapper

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

	curses.cbreak()
	screen.keypad(True)

	#Make the board
	cursor = (int(gameSize/2), int(gameSize/2))

	board = [['.' for i in range(gameSize)] for j in range(gameSize)]
	
	try:
		displayBoard(gameSize, board, screen)
	except:
		print("Incompatible board size")
		raise ValueError("Incompatible board size")
	#Main loop
	while(True):
		char = screen.getch()
		if char == 113: break
		elif char == curses.KEY_UP: cursor = (cursor[0],cursor[1]-1)
		elif char == curses.KEY_LEFT: cursor = (cursor[0]-1,cursor[1])
		elif char == curses.KEY_RIGHT: cursor = (cursor[0]+1,cursor[1])
		elif char == curses.KEY_DOWN: cursor = (cursor[0],cursor[1]+1)
		elif char == 99: board = resetBoard(gameSize, board, screen)
		
		if cursor[0] > gameSize - 1:
			cursor = (gameSize - 1, cursor[1])
		elif cursor[0] < 0:
			cursor = (0, cursor[1])
			
		if cursor[1] > gameSize - 1:
			cursor = (cursor[0], gameSize - 1)
		elif cursor[1] < 0:
			cursor = (cursor[0], 0)
		
		board[cursor[0]][cursor[1]] = 'x'
	
		displayBoard(gameSize, board, screen)
		
		time.sleep(0.1)
		
gameSize = int(input("What size would you like the game to be?"))
		
screen = curses.initscr()
try:
	wrapper(main)
except Exception as error:
	print(repr(error))
