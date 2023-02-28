from .Sensor import Sensor
from sense_hat import SenseHat
sense = SenseHat()
class MovementSensor(Sensor):
    
    def __init__(self, id):
        super().__init__(id)
        self._init_value = self.get_value();
        
    def get_type(self):
        return "movement_sensor"
    
    def get_value(self):
        acceleration = sense.get_accelerometer_raw()
        
        acceleration_dict = {}
        
        acceleration_dict['x'] = acceleration['x']
        acceleration_dict['y'] = acceleration['y']
        acceleration_dict['z'] = acceleration['z']
        
        return acceleration_dict

