from .Sensor import Sensor
from sense_hat import SenseHat

class LightSensor(Sensor):
    def __init__(self, id):
        super().__init__(id)
        self._sense_hat = SenseHat()
        self._init_value = self.get_value();
        
    def get_type(self):
        return "light_sensor"
        
    def get_value(self):
        return self._sense_hat.get_light(0,255)
