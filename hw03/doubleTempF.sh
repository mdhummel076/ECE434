#!/bin/sh

temp1=`i2cget -y 2 0x49`
temp2=`i2cget -y 2 0x4a`

temp1C=`echo $((temp1))`
temp2C=`echo $((temp2))`

temp1F=$(($temp1C * 2 + 32))
temp2F=$(($temp2C * 2 + 32))

echo "$temp1F"
echo "$temp2F"

