#!python3
import paho.mqtt.client as mqtt
import time

from utilities.bcolors import bcolors
from utilities.data import collect_data
from utilities.data import pacakge_data
from utilities.time import logTime

# Clear
from actuators.Face import Face
Face.blank() 

# Import Sensors
from sensors.FakeTestSensor import FakeTestSensor
from sensors.Humidity import HumiditySensor
from sensors.MovementSensor import MovementSensor
from sensors.TemperatureSensor import TemperatureSensor
#from sensors.LightSensor import LightSensor

# Initialise Sensors
sensors = [];
sensors.append(HumiditySensor("humidity_sensor"))
sensors.append(MovementSensor("movement_sensor"))
sensors.append(TemperatureSensor("temperature_sensor"))



# Callbacks
from utilities.MQTT import on_log
from utilities.MQTT import on_connect
from utilities.MQTT import on_disconnect
from utilities.MQTT import process_command
    
# Establish connection details.
broker="broker.hivemq.com"
client = mqtt.Client()
# Bind callbacks.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client._on_message = process_command
client.on_log = on_log

# Establish Connection
client.connect(broker)

client.loop_start()
time.sleep(2)

# Listen on the required topic.
client.subscribe("sensor/commands")


while True:
    # Collect Sensor Data
    time.sleep(5)
    sensor_data = pacakge_data(
        collect_data(sensors)
    )
    # Send Sensor Data
    client.publish("sensor/data", sensor_data)
    print(bcolors.OKGREEN + logTime() + "successfully sent the following data: ", sensor_data)

    
client.loop_stop()

client.disconnect()
