import time
import math
from __future__ import print_function
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
print("connecting to Vehicle")
vehicle= connect("127.0.0.1:14551",wait_ready=True)
sleep(1)
print("change mode to guided")
vehicle.mode = VehicleMode("GUIDED")
print("mode GUIDED")
sleep(1)
print("try to arming")
vehicle.armed = True
print("arming done")

