from .bcolors import bcolors
from .time import logTime
import json
from actuators.Face import Face
from actuators.Speaker import Speaker

# Callbacks

def on_log(client, userdata, level, buf):
    print(bcolors.WARNING + logTime() + "Log: ", buf)
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(bcolors.OKGREEN + logTime() + "Sensor node successfully connected.")    
    else:
        print(bcolors.FAIL + logTime() + "Sensor node failed to connect [code=" + rc + "].")    
        
def on_disconnect(client, userdata, flags, rc=0):
    print(bcolors.FAIL + logTime() + "Sensor node has disconnected. [code=" + str(rc) + "].")
    
    # process_command is binded to client.on_message
def process_command(client, userdata, command):
    command = str(command.payload.decode("utf-8"))
    parsed_command = json.loads(command)
    
    if parsed_command['type'] == "face":
        getattr(Face, parsed_command['method'])()
        # Face.sad();
    elif parsed_command['type'] == "speaker":
        if parsed_command['method'] == "say":
            Speaker.say(parsed_command['data'])
        elif parsed_command['method'] == "alarm":
            Face.alarm()
            Speaker.alarm(5)
    
    print(bcolors.ENDC + logTime() + "Recieved Command: " + command)
    
    