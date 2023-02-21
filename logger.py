from datetime import datetime
import logging

def InitializeLog(logPath: str):
    global log
    log = logPath

def Log(message):
    currentTime = datetime.now()
    filename = f"{currentTime.year}-{currentTime.month}-{currentTime.day}--{currentTime.hour}-{currentTime.minute}.txt"
    f = open(log + "\\" + filename, "a")
    f.write("test")
    f.writelines(message)
    f.close()    
    