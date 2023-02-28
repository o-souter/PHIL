import json
import time

# Act on recieved data.
def process_data(config, data, cb):
    print(data)
    parsed_data = json.loads(data)

    for sensor_id, sensor in parsed_data.items():
        #Takes in humidity value
        if(sensor['type'] == "humidity_sensor"):
            #checks if the difference between the inital humidity value and current are more than/equal to 20, if so command is sent
            if(sensor['value'] - sensor['init_value'] >= 10):
                cb('{"type": "speaker", "method": "say", "data": "Hello ' + config['name'] + '! We sense your presence, if you are ever in danger please press the panic button located on top of me."}')
                print("Humidity is high, possible presence")
                
        if(sensor['type'] == "panic_btn"):
            cb('{"type": "speaker", "method": "alarm"}')
            print("panic pressed")
        
        if(sensor['type'] == "temperature_sensor"):
            temperatureDiff = (sensor['value'] - sensor['init_value'])
            if(sensor['value'] - sensor['init_value'] >= 2):
                cb('{"type": "speaker", "method": "say", "data":"Your house seems to be warm if there is a fire please press the panic button and if possible make a safe exit."}')
                cb('{"type": "face", "method":"sad"}')
                #print("Temperature is high, " + str(diff) + " more than " + str(init)

        
        if(sensor['type'] == "movement_sensor"):
            #Processing the current values
            acceleration_dict = (sensor['value'])
            x = abs(acceleration_dict['x'])
            y = abs(acceleration_dict['y'])
            z = abs(acceleration_dict['z'])
            xyz = x+y+z
            
            #Processing the initial values
            acceleration_dict_init = sensor['init_value']
            xinit = abs(acceleration_dict_init['x'])
            yinit = abs(acceleration_dict_init['y'])
            zinit = abs(acceleration_dict_init['z'])
            xyzinit = xinit+yinit+zinit
            #print("Comparing " + str(xyz) + " and " + str(xyzinit))
            #print("Difference of " + str(xyz-xyzinit))
            #Values are compared, if there is a difference of 1.5/-1.5 or more then the command will be sent
            if(xyz-xyzinit >= 1):
                cb('{"type": "speaker", "method": "say", "data":"High Movement detected. Help is on the way, get cover possible earthquake!"}')
                cb('{"type": "speaker", "method": "alarm"}')
                print("high movement")
                # Future implementation of contacing help to be implemented   
               #Processing vocal input
        if(sensor['type'] == "voice"):
            #Sad Face
            cb('{"type": "face", "method": "sad"}')
            #Reassure user that help is on the way
            cb('{"type": "speaker", "method": "say", "data":"Help is on the way, please stay calm"}')
            cb('{"type": "speaker", "method": "alarm"}')

                    
