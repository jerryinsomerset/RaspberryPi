import RPi.GPIO as GPIO
from time import sleep
import StringIO
import subprocess
import os
import time
from datetime import datetime
import Image

# Threshold      - (how much a pixel has to change by to be marked as changed)
# Sensitivity    - (how many changed pixels before capturing an image) needs to be higher if noisy view
# ForceCapture   - (whether to force an image to be captured every forceCaptureTime seconds)
# filepath       - location of folder to save photos
# filenamePrefix - string that prefixes the file name for easier identification of files.
threshold = 10
sensitivity = 180
forceCapture = True
forceCaptureTime = 60 * 60 # Once an hour
filepath = "/home/pi/python_programs/pictures"
filenamePrefix = "capture"
saveWidth = 1280
saveHeight = 960


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
    while True:
        if (GPIO.input(17)):
            time = datetime.now()
            filename = filepath + "/" + filenamePrefix + "-%04d%02d%02d-%02d%02d%02d.jpg" % ( time.year, time.month, time.day, time.hour, time.minute, time.second)
            subprocess.call("raspistill -w 1296 -h 972 -t 0 -e jpg -q 15 -o %s" % filename, shell=True)
            print("Captured %s" %filename)
        else:
            print("Button Not Pressed")
        sleep(0.1)

finally:
    GPIO.cleanup()


            

