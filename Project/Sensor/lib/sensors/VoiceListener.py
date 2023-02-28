from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt
sense = SenseHat()
from pocketsphinx import LiveSpeech
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)     # setting up new voice rate

# Establish connection details.
broker="broker.hivemq.com"
client = mqtt.Client()

# Establish Connection
client.connect(broker)

client.loop_start()
def say(text):
    engine.say(text)
    engine.runAndWait()
    

print("Listening for vocal input...")
while True:
    #Listen for voice input
    needsHelp = LiveSpeech(lm=False, keyphrase='phil i need help', kws_threshold=1e-20)
    for phrase in needsHelp:
        if phrase.segments(detailed=True):
            print("User has asked for help")
            client.publish("sensor/data", '{"voice_listener":{"type":"voice", "value":"danger"}}')
