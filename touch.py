import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
touchip=38
touchvcc=36
GPIO.setup(touchvcc,GPIO.OUT)
GPIO.output(touchvcc,True)

GPIO.setup(touchip,GPIO.IN)

try:
    while True:
        if GPIO.input(touchip)==1:
            os.system("mosquitto_pub -t medbox/schedule -m cancel")
except KeyboardInterrupt:
    GPIO.cleanup()