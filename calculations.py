import time
import sys
import os

def clear():
    if sys.platform() == 'linux' :
        os.system('clear')
    elif sys.platform() == 'win32':
        os.system('clr')

def zone(zone=1): 
    return 3600 * zone

def Time():
    return time.strftime("%d %B %H:%M:%S", time.gmtime(time.time() + zone(3)))

def logger(system, message):
    print(f"{Time()} - {system} :: {message}")
