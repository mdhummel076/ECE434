#!/bin/sh

if [ $# -lt 2 ]; then
    echo "Usage: $0 <gpio pin#> <delay in seconds>"
    exit 0
fi
GPIO=$1
PERIOD=$2

cleanup() { # Set the GPIO port to 0
  echo 0 > /sys/class/gpio/gpio${GPIO}/value
  echo "Cleaning up"
  echo ""
  exit
}

if [ ! -e /sys/class/gpio/gpio$GPIO ]; then
    echo "$GPIO" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio${GPIO}/direction

trap cleanup SIGINT

THIS_VALUE=0
NEWLINE=0

while [ "1" = "1" ]; do

  # "^" for high, '_' for low
  if [ "1" = "$THIS_VALUE" ]; then
    EV="${EV}^"
    THIS_VALUE=0
   else
    EV="${EV}_"
    THIS_VALUE=1
  fi
  echo $THIS_VALUE > /sys/class/gpio/gpio${GPIO}/value

  sleep $PERIOD

  NEWLINE=`expr $NEWLINE + 1`
  if [ "$NEWLINE" = "72" ]; then
#    echo ""
    NEWLINE=0
  fi

done

cleanup
