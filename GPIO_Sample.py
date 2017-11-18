import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(17, GPIO.OUT)  # set up pin 17
GPIO.setup(18, GPIO.OUT)  # set up pin 18

output = 1
while True:
    time.sleep(1)
    output =  not output
    GPIO.output(17, output)  # turn on pin 17
    GPIO.output(18, 1)  # turn on pin 18

