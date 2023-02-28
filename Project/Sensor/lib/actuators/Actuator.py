

class Actuator:
    """ Top level class for actuators """
    
    def __init__(self, id):
        ## Define the sensor ID.
        self._id = id
        
    def get_id(self):
        ## Return the sensor ID.
        return self._id
        
    def calibrate(self):
        ## Requires Implementation
        pass
    
    def execute(self, data):
        ## Requires Implementation
        pass        