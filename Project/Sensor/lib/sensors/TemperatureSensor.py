from .Sensor import Sensor
from sense_hat import SenseHat

class TemperatureSensor(Sensor):
    def __init__(self, id):
        super().__init__(id)
        self.sense_hat = SenseHat()
        self._init_value = self.get_value();
        
    def get_type(self):
        return "temperature_sensor"
        
    def get_value(self):
        return self.sense_hat.get_temperature()

