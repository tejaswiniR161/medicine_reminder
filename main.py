import RPi.GPIO as GPIO
import time
import paho.mqtt.subscribe as subscribe
import schedule
import os

def job():
    print("executed?")
    open_box()

def on_scheduler_request(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    
    fi = open("schedule.txt","r")
    new_state=fi.read()
    fi.close()
    print(new_state)
    last_state=new_state
    #print(last_state)
    #10:10;20:20;21:21;:
    hm=last_state.split(";")
    for i in hm:
        t=i.split(":")
        h=t[0]
        m=t[1]
        #print("h ",h)
        #print("m ",m)
        if h is not "" and m is not "":
            #print("valid lemme schedule")
            print("scheduling at : ",i)
            schedule.every().day.at(i).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

    #open_box()
    #close_box()

#os.system("mosquitto_pub -t medbox/schedule -m on")


servoPIN = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start((90 / 18) + 2)

def open_box():
    time.sleep(1)
    os.system("cvlc ./audio/timeformeds.mp3 --play-and-exit")
    print("opening the box")
    global p
    duty = (270 / 18) + 2
    p.ChangeDutyCycle(duty)
    time.sleep(1)


def close_box():
    duty = (90 / 18) + 2
    global p
    p.ChangeDutyCycle(duty)
    time.sleep(1)

close_box()

#close_box()
""" p=0
while True:
    print("waiting?")
    schedule.run_pending()
    if p==0: """

open_box()

subscribe.callback(on_scheduler_request, "medbox/schedule")

"""         p+=1
    time.sleep(1) """


""" p.stop()
GPIO.cleanup() """