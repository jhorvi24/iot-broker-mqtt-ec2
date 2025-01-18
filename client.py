import sys

import paho.mqtt.client as paho

client = paho.Client()

if client.connect("54.87.187.153", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.publish("test/topic", "Hi, paho mqtt client works fine!", 0)
client.disconnect()