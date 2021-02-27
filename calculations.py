import time

def time_zone(zone):
    return 3600 * zone

def get_time():
    return time.strftime("%d %B %H:%M:%S", time.gmtime(time.time() + time_zone(3)))

def logger(system, message):
    print(f"{get_time()} - {system.name} :::: {message}")