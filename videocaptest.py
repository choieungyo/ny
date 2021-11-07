import numpy as np
import cv2
import cv2.aruco as aruco
import sys, time, math

calib_path  = ""
camera_matrix   = np.loadtxt(calib_path+'cameraMatrix_webcam.txt', delimiter=',')
camera_distortion   = np.loadtxt(calib_path+'cameraDistortion_webcam.txt', delimiter=',')
aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters  = aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame', frame)
sleep(5)
cv2.destroyAllWindows()
