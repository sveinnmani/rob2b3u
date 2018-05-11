#Libraries
import RPi.GPIO as GPIO
import random
import time

#GPIO MOde (Board / BCM)
GPIO.setmode(GPIO.BCM)
#print("Something something darkside")
#set GPIO Pins
GPIO_TRIGGER = 5
GPIO_ECHO = 6
Motor1A = 10
Motor1B = 9
Motor1E = 11
Motor2A = 17
Motor2B = 27
Motor2E = 22
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

def rndm5050(a, b):
    test = random.random()
    if test < 0.5: return a
    else: return b
def motorForward():
    #Setting the first motor to move forward
    print("Driving forward")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    #Setting the other motor to move forward
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def motorBackward():
    #Setting the first motor to move backwards
    print("Backing up")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    #Setting the other motor to move backwards
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def motorLeft():
    #Setting the first motor to move forwards
    print("Turn left")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    #Setting the other motor to move backwards
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def motorRight():
    #Setting the first motor to move backwards
    print("Turn right")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    #Setting the other motor to move forward
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def motorStop():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)

def distance():
    #set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    #set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    #save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    #save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    #time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    #multiply with the sonic speed (34300 cm/s)
    #and divide by 2, because there and back
    distance = (TimeElapsed * 343000) / 2
    return distance
print("dfdfk")

try:
    while True:
        dist = distance()
        print("Measured Distance = % if cm" % dist)
        #Herna kemur kodinn fyrir verkefnid
        if dist > 1000: #A eftir ad meta hversu langt talan a ad vera
            motorForward()
        else:
            motorStop()
            time.sleep(1)
            direct = rndm5050(1,2)
            if(direct == 1):
                motorRight()
            else:
                motorLeft()
        time.sleep(1)
#Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
