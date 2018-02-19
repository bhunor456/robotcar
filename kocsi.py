import curses
#import time
import RPi.GPIO as GPIO
from time import sleep 

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

#def setup():

#Motor1 = GPIO.PWM(25, 50)
#Motor1 = start(0)
#Motor2 = GPIO.PWM(11, 50)
#Motor2 = start(0)

Motor1A = 23 #16-os láb input 1, sárga kábel
Motor1B = 24 #18-as láb input 2 zöld kábel
Motor1E = 25 #22-es láb enable 1,2 lila kábel

Motor2A = 5 #29-es láb input 4 sárga kábel
Motor2B = 6 #31-es láb input 3 zöld kábel
Motor2E = 13 #33-as láb enable 3,4 lila kábel

#GPIO.setup(7,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)
#GPIO.setup(15,GPIO.OUT)
#for x in range (0,7):
    #GPIO.output(7,True)
    #time.sleep(0.125)
    #GPIO.output(7,False)
    #time.sleep(0.125)
    #GPIO.output(13,True)
    #time.sleep(0.125)
    #GPIO.output(13,False)
    #time.sleep(0.125)
    #GPIO.output(15,True)
    #time.sleep(0.125)
    #GPIO.output(15,False)
    #time.sleep(0.125)

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

#A billentyűk, és a képernyő kezelése 

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print("Előre")
            GPIO.output(Motor1A,GPIO.HIGH)# True, (1)
            GPIO.output(Motor1B,GPIO.LOW) #False, (0)
            GPIO.output(Motor1E,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2A,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2B,GPIO.LOW) #False, (0)
            GPIO.output(Motor2E,GPIO.HIGH) #True, (1)
        elif char == curses.KEY_DOWN:
            print("Hátra")
            GPIO.output(Motor1A,GPIO.LOW) #False, (0)
            GPIO.output(Motor1B,GPIO.HIGH) #True, (1)
            GPIO.output(Motor1E,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2A,GPIO.LOW) #False, (0) 
            GPIO.output(Motor2B,GPIO.HIGH) #True (1)
            GPIO.output(Motor2E,GPIO.HIGH) #True (1)
        elif char == curses.KEY_RIGHT:
            print("Jobbra")
            GPIO.output(Motor1A,GPIO.LOW) #False, (0)
            GPIO.output(Motor1B,GPIO.HIGH) #True, (1)
            GPIO.output(Motor1E,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2A,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2B,GPIO.LOW) #True, (1)
            GPIO.output(Motor2E,GPIO.HIGH) #True, (1)
        elif char == curses.KEY_LEFT:
            print("Balra")
            GPIO.output(Motor1A,GPIO.HIGH) #True, (1)
            GPIO.output(Motor1B,GPIO.LOW) #False, (0)
            GPIO.output(Motor1E,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2A,GPIO.LOW) #False, (0)
            GPIO.output(Motor2B,GPIO.HIGH) #True, (1)
            GPIO.output(Motor2E,GPIO.HIGH) #True, (1)
        elif char == 10:
            print("Állj")
            GPIO.output(Motor1A,GPIO.LOW) #False, (0)
            GPIO.output(Motor1B,GPIO.LOW) #False, (0)
            GPIO.output(Motor1E,GPIO.LOW) #False, (0)
            GPIO.output(Motor2A,GPIO.LOW) #False, (0)
            GPIO.output(Motor2B,GPIO.LOW) #False, (0)
            GPIO.output(Motor2E,GPIO.LOW) #Fasle, (0)


#Előre haladás:
#def loop()
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.lOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    #Motor1.ChangeDutyCycle(speed)
    #Motor2.ChangeDutyCycle(speed)

    print ("1-es motor indul")
    print("előre")

    sleep(1)

#Hátrafelé haladás:
#def backward(speed)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    #Motor1.ChangeDutyCycle(speed)
    #Motor2.ChangeDutyCycle(speed)
    
    sleep(1)

    #Balra fordulás
    #def left(speed)

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
        #Motor1.ChangeDutycycle(speed)

    #Jobbra fordulás
    #def right(speed)

    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
        #Motor2.ChangeDutycycle(speed)

    #Megállás:
    #def stop()
    
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    #Motor1.changeDutyCycle(0)
    #Motor2.ChangeDutycycle(0)
    
    #forward(100)
    #sleep(2)
    #backward(100)
    #sleep(2)
    #forward(50)
    #sleep(3)
    #stop(0)
    #left(75)
    #sleep(3)
    #right(75)
    #sleep(2)
    #stop()

finally:
    curses.nocbreak(); scree.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    



