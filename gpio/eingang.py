#!/usr/bin/env python
#coding: utf8 
 
import RPi.GPIO as GPIO
 
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)
 
# Pin 18 (GPIO 24) als Eingang festlegen
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
 
# Schleifenzähler
i = 0
 
# Endlosschleife
while 1:
    # Eingang lesen
    if GPIO.input(18) == GPIO.HIGH:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print "Eingang HIGH " + str(i)
        # Schleifenzähler erhöhen
        i = i + 1
