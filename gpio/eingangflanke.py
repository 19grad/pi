#!/usr/bin/env python
#coding: utf8 

# https://indibit.de/raspberry-pi-gpio-ausgaenge-schalten-eingaenge-lesen/#Steigende_und_fallende_Flanke
 
import time
import RPi.GPIO as GPIO
 
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)
 
# Pin 18 (GPIO 24) als Eingang festlegen
channel = 18
GPIO.setup(channel , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
 
# Schleifenzähler
i = 0
 
# Ereignis-Funktion für Eingang HIGH
def doIfHigh(channel):
    # Zugriff auf Variable i ermöglichen
    global i
 
    if GPIO.input(channel) == GPIO.HIGH:
        # Wenn Eingang HIGH ist, Ausgabe im Terminal erzeugen
        print "Eingang " + str(channel) + " HIGH " + str(i)
    else:
        # Wenn Eingang LOW ist, Ausgabe im Terminal erzeugen
        print "Eingang " + str(channel) + " LOW " + str(i)
 
    # Schleifenzähler erhöhen
    i = i + 1
 
# Ereignis deklarieren

GPIO.add_event_detect(channel, GPIO.BOTH, callback = doIfHigh, bouncetime = 500)
 
# Eigentlicher Programmablauf
print "Warte auf Eingang " + str(channel)
while 1:
    time.sleep(0.1)
