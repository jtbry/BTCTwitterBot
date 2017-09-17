import datetime, sys, os
PERCENTVAR = None
STARTVAR = None
CURRENTVAR = None

def updatedata():
    with open("pythonout.dat", 'r+') as handler:
        string = f"{PERCENTVAR},{STARTVAR},{CURRENTVAR}"
        handler.write(string)