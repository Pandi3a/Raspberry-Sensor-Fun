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
            print "\033[0;34;47m It is Raining!!\033[0;0m"
    else:
            print "It is Dry !!"

    time.sleep(2)

