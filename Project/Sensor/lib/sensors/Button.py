from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt

# Establish connection details.
broker="broker.hivemq.com"
client = mqtt.Client()

# Establish Connection
client.connect(broker)

client.loop_start()

sense = SenseHat()
while True:
    event = sense.stick.wait_for_event()
    if event.action == "pressed":
        client.publish("sensor/data", '{"button":{"type":"panic_btn", "value":"pressed"}}')
