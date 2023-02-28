from datetime import datetime

def logTime():
    now = datetime.now()
    return "[" + now.strftime("%H:%M:%S") + "] "
