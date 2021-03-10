import time
import os

def clear():
    os.system('clear')

def zone(zone=1): 
    return 3600 * zone

def Time():
    return time.strftime("%d %B %H:%M:%S", time.gmtime(time.time() + zone(3)))

def logger(system, message):
    print(f"{Time()} - {system} :: {message}")
