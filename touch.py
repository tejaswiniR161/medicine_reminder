import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
touchip=38
touchvcc=36
GPIO.setup(touchvcc,GPIO.OUT)
GPIO.output(touchvcc,True)

GPIO.setup(touchip,GPIO.IN)