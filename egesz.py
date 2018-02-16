import curses
import RPi.GPIO as GPIO
import time

#GPIO kimenetek megszámpzása
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT) #Motor1: előre
GPIO.setup(13,GPIO.OUT) #Motor1: hátra
GPIO.setup(15,GPIO.OUT) #Motor2: előre
GPIO.setup(29,GPIO.OUT) #Motor2: hátra
#for x in range(0,4):
#GPIO.output(7,True) 
#GPIO.output(13,True)
#time.sleep(2)
#GPIO.output(7,False)
#GPIO.output(13,False)
#time.sleep(2)
#GPIO.output(11,True)
#GPIO.output(15,True)
#time.sleep(2)
#GPIO.output(11,False)
#GPIO.output(15,False)

#A billentyűk és a képernyő kezelése
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
            print("Előre/up")
            GPIO.output(7,False)
            GPIO.output(13,True)
            GPIO.output(15,False)
            GPIO.output(29,True)
        elif char == curses.KEY_DOWN:
            print("Hátra/down")
            GPIO.output(7,True)
            GPIO.output(13,False)
            GPIO.output(15,True)
            GPIO.output(29,False)
        elif char == curses.KEY_RIGHT:
            print("Jobbra/right")
            GPIO.output(7,True)
            GPIO.output(13,False)
            GPIO.output(15,False)
            GPIO.output(29,True)
        elif char == curses.KEY_LEFT:
            print("Balra/left")
            GPIO.output(7,False)
            GPIO.output(13,True)
            GPIO.output(15,True)
            GPIO.output(29,False)
        elif char == 10:
            print("Állj/stop")
            GPIO.output(7,False)
            GPIO.output(13,False)
            GPIO.output(15,False)
            GPIO.output(29,False)

finally:
    curses.nocbreak(); scree.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
