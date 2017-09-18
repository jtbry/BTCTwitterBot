import datetime, sys, os
from collections import namedtuple
#Variables saved by other functions
PERCENTVAR = None
STARTVAR = None
CURRENTVAR = None
TIMEVAR = None
#Variables in a file
FILEPERCENT = None
FILESTART = None
FILECURRENT = None
#New values after comparing
COMPAREPERCENT = None
COMPARESTART = None
COMPARECURRENT = None
COMPAREOVERALL = None
def comparedata():
    with open("pythonout.dat", 'r+') as handler:
        data = handler.readlines()
    COMPAREOVERALL = float(data[1]) - float(data[2])
    return print(COMPAREOVERALL)
def updatedata():
    with open("pythonout.dat", 'r+') as handler:
        data = handler.readlines()
        handler.seek(0)
        handler.truncate()
        writedata = f"{PERCENTVAR}\n{STARTVAR}\n{CURRENTVAR}\n{TIMEVAR}"
        handler.write(writedata)
        handler.close()
def gethourtime():
    with open("pythonout.dat", 'r+') as handler:
        data = handler.readlines()
        handler.close()
    if len(data) < 4:
        return str(datetime.datetime.utcnow())
    else:
        return data[-1]
def sethourtime(time):
    with open("pythonout.dat", 'r+') as handler:
        data = handler.readlines()
        if len(data) < 3:
            updatedata()
            data.append(str(time))
        else:
            data[3] = str(time)
        #Clear the file so we can re-write with new time.
        handler.seek(0)
        handler.truncate()
        #Re-Write
        handler.writelines(data)
        handler.close()