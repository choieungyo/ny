import time
import math
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
print("connecting to Vehicle")
vehicle= connect("/dev/ttyACM0", baudrate = 57600, wait_ready=True)
vehicle.airspeed = 0.3
vehicle.groundspeed = 0.3
time.sleep(1)
def arming():
    print ("Basic pre-arm checks")
    while not vehicle.is_armable:
        print("waiting for vehicle to initialise...")
        time.sleep(1)
    
    print ("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
  
    while not vehicle.armed:
        print("waiting for arming...")
        time.sleep(1)
   
arming()
time.sleep(3)
print("close vehicle")
vehicle.close()

%%test3
