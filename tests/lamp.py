#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

# GPIO | Relay
# --------------
# 26     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers

gpio = 19

def switchOff():
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, GPIO.HIGH)

def switchOn():
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, GPIO.LOW)


if __name__ == "__main__":
    input = sys.argv[1]
    if input == "off":
        switchOff()
    elif input == "on":
        switchOn()
    else:
        print("Wrong param entered")