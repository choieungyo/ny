import time
import socket
import exceptions
import math
import argparse

from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException
from pymavlink import mavutil

import cv2
import cv2.aruco as aruco
import numpy as np

from imutils.video import WebcamVideoStream
import imutils

vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)
output add 127.0.0.1:14550