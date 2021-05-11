import RPi.GPIO as GPIO
import time
import paho.mqtt.subscribe as subscribe
import schedule
import os
import datetime

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
        if h is not "" and m is not "":
            #print("valid lemme schedule")
            print("scheduling at : ",i)
            schedule.every().day.at(i).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

servoPIN = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)


touchip=38
touchvcc=36
GPIO.setup(touchvcc,GPIO.OUT)
GPIO.output(touchvcc,True)

GPIO.setup(touchip,GPIO.IN) 


stop=0

p = GPIO.PWM(servoPIN, 50)
p.start((90 / 18) + 2)

def open_box():
    time.sleep(1)
    print("opening the box")
    global p
    duty = (270 / 18) + 2
    p.ChangeDutyCycle(duty)
    time.sleep(1)

    os.system("cvlc ./audio/timeformeds.mp3 --play-and-exit")
    count=0
    while count<30 and GPIO.input(touchip)!=1:
        count+=1
        time.sleep(1)
        print("count = ",count)
    if count>=30:
        os.system("cvlc ./audio/alert.mp3 --play-and-exit")
        print("Pill not taken, alerting the caretaker")
        close_box()
    else:
        print("Thanks for taking the pill")
        os.system("cvlc ./audio/thanks.mp3 --play-and-exit")
        close_box()
        #pill not taken, alerting the people

    #if GPIO.input(outhelmetip)==1:
def announceAndSnooze(last_time,count=0):
    global stop
    while count<=2:
        if stop==0:
            os.system("cvlc ./audio/timeformeds.mp3 --play-and-exit")
            time.sleep(30)
            count+=1
        else:
            break
    if stop==0:
        pass
        #send email right away
    return

def close_box():
    duty = (90 / 18) + 2
    global p
    p.ChangeDutyCycle(duty)
    time.sleep(1)

close_box()
#open_box()

subscribe.callback(on_scheduler_request, "medbox/schedule")