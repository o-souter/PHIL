#!python3
import paho.mqtt.client as mqtt
import time
import webbrowser



from utilities.bcolors import bcolors
from utilities.time import logTime
from utilities.act import process_data

# Callbacks
from utilities.MQTT import on_log
from utilities.MQTT import on_connect
from utilities.MQTT import on_disconnect

# Establish connection details.
broker="broker.hivemq.com"
client = mqtt.Client("GatewayNode")

print("Please enter your name");
config = {}
config['name'] = input();
print("Attempting connect")

# recieved_data is binded to client.on_message
def recieved_data(client, userdata, command):
    data = str(command.payload.decode("utf-8"))
    # print(bcolors.ENDC + logTime() + "Recieved Data: " + data)
    process_data(config, data, cb = broadcast_command);
    
def broadcast_command(command):
    client.publish("sensor/commands", command)

# Bind callbacks.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client._on_message = recieved_data
client.on_log = on_log

# Establish Connection
client.connect(broker)


client.loop_start()
time.sleep(2)

client.subscribe("sensor/data")
    
webbrowser.open("https://dakboard.com/app/screenPredefined?p=3f792e80005d71aba625fca7c36ddc75")
while True:
    pass
# client.loop_stop()

# client.disconnect()
