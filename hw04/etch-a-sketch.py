#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
'''
	Beagle GPIO Status and Control
'''
import Adafruit_BBIO.GPIO as GPIO
import smbus
from flask import Flask, render_template, request
app = Flask(__name__)

bus = smbus.SMBus(2)
matrix = 0x70

gameSize = 8
cursor = [3, 3]

board = [0x00 for i in range(gameSize)]

def updateCursor(action):
	global cursor, board
	if action == 'up':
		cursor[0] += 1
	elif action == 'down':
		cursor[0] -= 1
	elif action == 'right':
		cursor[1] -= 1
	elif action == 'left':
		cursor[1] += 1
	
	if cursor[0] < 0:
		cursor[0] = 0
	elif cursor[0] > 7:
		cursor[0] = 7

	if cursor[1] < 0:
		cursor[1] = 0
	elif cursor[1] > 7:
		cursor[1] = 7
	
	print(cursor)
	
	board[cursor[0]] |= 1 << cursor[1]
	display = [0x00, board[0], 0x00, board[1], 0x00, board[2], 0x00, board[3], 0x00, board[4], 0x00, board[5], 0x00, board[6], 0x00, board[7]]
	bus.write_i2c_block_data(matrix, 0, display)

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

@app.route("/")
def index():

	templateData = {}
	return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	templateData = {}

	updateCursor(action)

	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
