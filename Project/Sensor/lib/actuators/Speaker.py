from .Actuator import Actuator
import random
from sense_hat import SenseHat
sense = SenseHat()
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)     # setting up new voice rate

import os

class Speaker(Actuator):
        def __init__(self, id):
            super().__init__(id)
            self._sense_hat = SenseHat()
        
        
        def get_type(self):
            return "voice_actuator"

        def say(text):
            engine.say(text)
            engine.runAndWait()
            
        def alarm(time):
            freq = 440  # Hz
            os.system('play -nq -t alsa synth {} sine {}'.format(time, freq))
