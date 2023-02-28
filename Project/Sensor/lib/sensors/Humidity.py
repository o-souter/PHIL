from .Sensor import Sensor
from sense_hat import SenseHat
sense = SenseHat()
class HumiditySensor(Sensor):
    
    def __init__(self, id):
        super().__init__(id)
        self._sense_hat = SenseHat()
        self._init_value = self.get_value();
        
    def get_type(self):
        return "humidity_sensor"
    
    def get_value(self):
        humidity = sense.get_humidity()
        return humidity
