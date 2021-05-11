import schedule
import time
import RPi.GPIO as GPIO
from gtts import gTTS
import time
import os
from time import gmtime, strftime
import smtplib


def job():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(12,GPIO.IN)
    GPIO.output(16,True)
    GPIO.setup(7,GPIO.OUT)
    #GPIO.output(7,True)
    #s="Time for tablets"
    #speakobj=gTTS(text=s,lang='en',slow=False)
    #speakobj.save("op.mp3")
    #os.system("vlc op.mp3 --play-and-exit")
    print("I'm working...")
    count=1
    #while GPIO.input(12)!= 1 :
    while count<6 and GPIO.input(12)!= 1 :
        print ("well well")
        GPIO.output(7,True)
        time.sleep(10)
        GPIO.output(7,False)
        #time.sleep(2)
        os.system("vlc op.mp3 --play-and-exit")
        count+=1
    print (count)
    GPIO.cleanup()
    if count<6:
        #s="thanks for taking your tablets. Will remind you next time again."
        #speakobj=gTTS(text=s,lang='en',slow=False)
        #speakobj.save("op2.mp3")
        f=open("pill.txt","r")
        t=f.read()
        print(t)
        f.close()
        no=int(t)
        no-=1
        f=open("pill.txt","w")
        num=str(no)
        f.write(num)
        f.close()
        if no<5:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            #Next, log in to the server
            server.login("chaithradinesh.524@gmail.com", "robertpattinson luv")
            message = "\r\n".join(['Subject: Reminding that you have to refill the pill box ',"please refill your pill box"])
            #Send the mail
            msg = "Hello!" # The /n separates the message from the headers
            server.sendmail("chaithradinesh.524@gmail.com", "chaithragowda.524@gmail.com", message)
            server.quit
            print("Email sent")
            print("count of pills less than 5")
        os.system("vlc op2.mp3 --play-and-exit")
    else:
        #s="you did not take tablets. We'll send a mail to your caretaker"
        #speakobj=gTTS(text=s,lang='en',slow=False)
        #speakobj.save("op3.mp3")
        os.system("vlc op3.mp3 --play-and-exit")
        
        #server = smtplib.SMTP_SSL('smtp.gmail.com', 465,timeout=120)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        #Next, log in to the server
        server.login("chaithradinesh.524@gmail.com", "robertpattinson luv")
        message = "\r\n".join(['Subject: Your ward did not take the pills ',"please inform your ward to take pills"])
        #Send the mail
        msg = "Hello!" # The /n separates the message from the headers
        server.sendmail("chaithradinesh.524@gmail.com", "chaithragowda.524@gmail.com", message)
        server.quit
        print("Email sent")
        #t=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        #'2009-01-05 22:14:39'
        #t=t.split(" ")
        #t=str(t[1].split(":"))
        #t#=t.split(":")
        #print t
        #t[1]=int(t[1])+60
        #if t[1]%60 >0:
          #  t[0]=int(t[0]+1)%24
         #   t[1]=t[1]%60
        #k=t[0]+":"+t[1]
        #print(k)
        #schedule.every().day.at(k).do(job)
    
        #turn on led
    

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
f=open("time.txt","r")
t=f.read()
print(t)
f.close()
schedule.every().day.at(t).do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
