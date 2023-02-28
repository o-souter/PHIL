from .Sensor import Sensor
import random

class FakeTestSensor(Sensor):
    def __init__(self, id):
        super().__init__(id)
        
    def get_type(self):
        return "sensor_mock"
        
    def get_value(self):
        return random.randint(0,255)