import json

# Get sensor values from an array of sensors.
def collect_data(sensors):
    sensor_dictionary = {}
    
    for sensor in sensors:
        sensor_value_dictionary = {}
        sensor_value_dictionary['type'] = sensor.get_type()
        sensor_value_dictionary['value'] = sensor.get_value()
        sensor_value_dictionary['init_value'] = sensor._init_value
        
        sensor_dictionary[sensor.get_id()] = sensor_value_dictionary
        
    return sensor_dictionary

# Package JSON ready to be sent over MQTT
def pacakge_data(dictionary):
    return json.dumps(dictionary)
