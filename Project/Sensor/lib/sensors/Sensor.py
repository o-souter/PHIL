
class Sensor():
    """ Top level class for sensors """
    
    def __init__(self, id):
        ## Define the sensor ID.
        self._id = id
        
    def get_id(self):
        ## Return the sensor ID.
        return self._id
    
    def get_value(self):
        ## Requires Implementation
        pass
    
    def get_type(self):
        ## Requires Implementation
        pass
    
    def calibrate(self):
        ## Requires Implementation
        pass