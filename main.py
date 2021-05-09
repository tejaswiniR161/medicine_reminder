import RPi.GPIO as GPIO
import time

servoPIN = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start((90 / 18) + 2)

def open_box():
    time.sleep(1)
    print("opening the box")
    global p
    duty = (180 / 18) + 2
    p.ChangeDutyCycle(duty)
    time.sleep(1)

def close_box():
    duty = (90 / 18) + 2
    global p
    p.ChangeDutyCycle(duty)
    time.sleep(1)

close_box()
open_box()
close_box()

p.stop()
GPIO.cleanup()