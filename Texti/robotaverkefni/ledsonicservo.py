import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 14
GPIO_ECHO = 15
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
pwm=GPIO.PWM(18,100)
pwm.start(5)

def servo():
    angle1=10
    duty1= float(angle1)/10+2.5
    angle2=160
    duty2 = float(angle2)/10+2.5
    pwm.ChangeDutyCycle(duty1)
    time.sleep(0.5)
    distance()
    pwm.ChangeDutyCycle(duty2)
    time.sleep(0.5)
    distance()
    
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    if distance < 20:
            print("LED ON // Distance > %.1f cm" % distance)
            GPIO.output(23,GPIO.HIGH)
            time.sleep(1)
    else:
        print("led off")
        GPIO.output(23,GPIO.LOW)
    return


if __name__ == '__main__':
    try:
        while True:
            servo()
            time.sleep(1)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        GPIO.cleanup()
