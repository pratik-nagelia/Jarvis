#!/usr/bin/python
import RPi.GPIO as GPIO


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

def switch(gpio, state):
    GPIO.setup(gpio, GPIO.OUT)
    if state == "ON":
        GPIO.output(gpio, GPIO.LOW)
    elif state == "OFF":
        GPIO.output(gpio, GPIO.HIGH)


def init():
    GPIO.setmode(GPIO.BCM)
