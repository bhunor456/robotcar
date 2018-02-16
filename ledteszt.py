import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
for x in range(0,9):
    GPIO.output(7,True)
    time.sleep(0.125)
    GPIO.output(7,False)
    GPIO.output(13,True)
    time.sleep(0.125)
    GPIO.output(13,False)
    GPIO.output(15,True)
    time.sleep(0.125)
    GPIO.output(15,False)
    time.sleep(0.125)
GPIO.cleanup()


