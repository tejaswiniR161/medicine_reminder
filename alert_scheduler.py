import sched, time
#scheduler answer https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds
s = sched.scheduler(time.time, time.sleep)
#fi = open("schedule.txt","r")
last_state=""
#fi.read()
#fi.close()
print(last_state)

def lookforchanges(sc): 
    print("Checking for changes")
    fi = open("schedule.txt","r")
    new_state=fi.read()
    fi.close()
    print("dhfbd")
    print(new_state)
    global last_state
    if last_state!=new_state:
        last_state=new_state
        print(last_state)
        #10:10;20:20;21:21;:
        hm=last_state.split(";")
        for i in hm:
            t=i.split(":")
            h=t[0]
            m=t[1]
            print("h ",h)
            print("m ",m)
            if h is not "" and m is not "":
                print("valid lemme check")
                pass

    
    s.enter(60, 1, lookforchanges, (sc,))

def action():
    #ask the user to take the medicine 
    #open the medicine box
    #snooze for 5 minutes and then just rerun if touch sensor is never touched
    print("there i am")
    #pass
    #webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#s.enter(60, 1, lookforchanges, (s,))
#s.run()
lookforchanges(s)