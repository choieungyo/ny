import time
import math
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
vehicle = connect("127.0.0.1:14550", wait_ready = True)
while True:
  lon = vehicle.location.global_relative_frame.lon
  lat = vehicle.location.global_relative_frame.lat
  print lon, lat
  
