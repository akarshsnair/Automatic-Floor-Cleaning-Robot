import RPi.GPIO as GPIO
import time
import math

GPIO.setwarnings(False)
# Set GPIO mode
GPIO.setmode(GPIO.BCM)
 
IN1 = 17
IN2 = 18
ENA = 27
IN3 = 22
IN4 = 23
ENB = 24

GPIO_TRIGGER_FRONT = 16
GPIO_ECHO_FRONT = 20

GPIO.setup(GPIO_TRIGGER_FRONT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_FRONT, GPIO.IN)
# Set up GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)

pwm_a=GPIO.PWM(ENA, 50)
pwm_b=GPIO.PWM(ENB, 50)

pwm_a.start(0)
pwm_b.start(0) 
 
def move_wheels(right_wheel_fwd, left_wheel_fwd, right_speed=50, left_speed=50):
    pwm_a.ChangeDutyCycle(right_speed)
    pwm_b.ChangeDutyCycle(left_speed)
    GPIO.output(IN1, right_wheel_fwd)
    GPIO.output(IN2, not right_wheel_fwd)
    GPIO.output(IN3, left_wheel_fwd)
    GPIO.output(IN4, not left_wheel_fwd)

def move_forward():
    move_wheels(True, True)
    print('moving forward')
 
def move_backward():
    move_wheels(False, False)
    print('moving backward')

def turn_right():
    move_wheels(False, True) 
    print('turning right')
 
def turn_left():
    move_wheels(True, False)
    print('turning left')
    
def stop():
    move_wheels(False, False)
    print('stopped')

def get_distance():

    GPIO.output(GPIO_TRIGGER_FRONT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_FRONT, False) 
    StartTime_FRONT = time.time()
    StopTime_FRONT = time.time()    

    while GPIO.input(GPIO_ECHO_FRONT) == 0:
        StartTime_FRONT = time.time()
    # save time of arrival right
    while GPIO.input(GPIO_ECHO_FRONT) == 1:
        StopTime_FRONT = time.time()
 
    TimeElapsed_FRONT = StopTime_FRONT - StartTime_FRONT

    distance_FRONT = math.floor((TimeElapsed_FRONT * 34300) / 2)

    return (distance_FRONT)


try:
    while(True):
        obstacle_distance = get_distance()
        if obstacle_distance < 20:  
            stop()
            time.sleep(.5)
            turn_right()
            time.sleep(1)
            move_forward()
            time.sleep(.5)
        else:
            move_forward()


except KeyboardInterrupt:
    print('Existing...')

finally:
    stop()
    GPIO.cleanup()