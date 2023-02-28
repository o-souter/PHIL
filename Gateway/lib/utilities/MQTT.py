from .bcolors import bcolors
from .time import logTime
from .act import process_data

# Callbacks

def on_log(client, userdata, level, buf):
    #print(bcolors.HEADER + logTime() + "Log: ", buf)
    pass
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(bcolors.OKGREEN + logTime() + "Gateway node successfully connected.")    
    else:
        print(bcolors.FAIL + logTime() + "Gateway node failed to connect [code=" + rc + "].")    
        
def on_disconnect(client, userdata, flags, rc=0):
    print(bcolors.FAIL + logTime() + "Gateway node has disconnected. [code=" + str(rc) + "].")
    

    