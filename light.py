#!/usr/bin/env python

from time import sleep
import time
import os
import RPi.GPIO as GPIO

while True:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    state = GPIO.input(4)


    if (state == 0):
            print "\033[1;33;40m Light \033[0;0m"
    else:
            print "\033[1;34;40m Dark \033[0;0m"

    time.sleep(2)

