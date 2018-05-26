import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5) # semleges (neutral)
        print("semleges (neutral)")
        time.sleep(1)
        p.ChangeDutyCycle(12.5) # itt fordul el 180 fokot
        print("180 fok")
        time.sleep(1)
        p.ChangeDutyCycle(2.5) # 0 fok lesz
        print("0 fok")
        time.sleep(1)

except KeyboardInterrupt:
    print("A program leállt")
    p.stop()

    GPIO.cleanup()







