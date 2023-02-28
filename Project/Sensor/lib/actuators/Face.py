from .Actuator import Actuator
from random import randint
from sense_hat import SenseHat
import time
sense = SenseHat()

r = 153
g = 50
b = 204

red = (255, 0, 0)

class Face(Actuator):
        def __init__(self, id):
            super().__init__(id)
            self._sense_hat = SenseHat()
        
        def get_type(self):
            return "face_actuator"

        def blank():
            sense.clear()

        def happy():
            sense.clear()
            sense.set_pixel(2, 2, r, g, b)
            sense.set_pixel(2, 3, r, g, b)
            sense.set_pixel(5, 2, r, g, b)
            sense.set_pixel(5, 3, r, g, b)
            sense.set_pixel(1, 5, r, g, b)
            sense.set_pixel(6, 5, r, g, b)
            sense.set_pixel(2, 6, r, g, b)
            sense.set_pixel(5, 6, r, g, b)
            sense.set_pixel(3, 6, r, g, b)
            sense.set_pixel(4, 6, r, g, b)
            
        def sad():
            sense.clear()
            sense.set_pixel(2, 2, r, g, b)
            sense.set_pixel(2, 3, r, g, b)
            sense.set_pixel(5, 2, r, g, b)
            sense.set_pixel(5, 3, r, g, b)
            sense.set_pixel(1, 6, r, g, b)
            sense.set_pixel(6, 6, r, g, b)
            sense.set_pixel(2, 5, r, g, b)
            sense.set_pixel(5, 5, r, g, b)
            sense.set_pixel(3, 5, r, g, b)
            sense.set_pixel(4, 5, r, g, b)
        def normal():
            sense.clear()
            sense.set_pixel(2, 2, r, g, b)
            sense.set_pixel(2, 3, r, g, b)
            sense.set_pixel(5, 2, r, g, b)
            sense.set_pixel(5, 3, r, g, b)
            sense.set_pixel(1, 5, r, g, b)
            sense.set_pixel(6, 5, r, g, b)
            sense.set_pixel(2, 5, r, g, b)
            sense.set_pixel(5, 5, r, g, b)
            sense.set_pixel(3, 5, r, g, b)
            sense.set_pixel(4, 5, r, g, b)
            
        def lights():
            sense.clear()
            randRep = randint(0,50)
            i=0
            while i < randRep:
                time.sleep(0.1)
                i=i+1
                sense.set_pixel(randint(0,7),randint(0,7), randint(0,255), 0,0)
        
        def alarm():
            sense.clear()
            sense.show_letter("!", red)
