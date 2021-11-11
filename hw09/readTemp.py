#!/usr/bin/env python3

f = open('/sys/class/hwmon/hwmon0/temp1_input','r')

print(f.read())
