import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

#os.system("mosquitto_pub -t medbox/schedule -m on")
subscribe.callback(on_message_print, "medbox/schedule")