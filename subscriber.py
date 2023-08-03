#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor driver pins for the two front wheels
IN1 = 17
IN2 = 18
ENA = 27
IN3 = 22
IN4 = 23
ENB = 24

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

pwm_a = GPIO.PWM(ENA, 100)
pwm_b = GPIO.PWM(ENB, 100)

pwm_a.start(0)
pwm_b.start(0)

moving_forward = False

def move_wheels(right_wheel_fwd, left_wheel_fwd, right_speed=50, left_speed=50):
    pwm_a.ChangeDutyCycle(right_speed)
    pwm_b.ChangeDutyCycle(left_speed)
    GPIO.output(IN1, right_wheel_fwd)
    GPIO.output(IN2, not right_wheel_fwd)
    GPIO.output(IN3, left_wheel_fwd)
    GPIO.output(IN4, not left_wheel_fwd)

def move_forward():
    global moving_forward
    move_wheels(True, True)
    print('Moving forward')
    moving_forward = True

def move_backward():
    global moving_forward
    move_wheels(False, False)
    print('Moving backward')
    moving_forward = False

def turn_right():
    global moving_forward
    move_wheels(False, True)
    print('Turning right')
    moving_forward = False

def turn_left():
    global moving_forward
    move_wheels(True, False)
    print('Turning left')
    moving_forward = False

def stop():
    global moving_forward
    move_wheels(False, False)
    print('Stopped')
    moving_forward = False

def callback(data):
    global moving_forward
    distance = data.data
    rospy.loginfo("Received Distance: {:.2f} cm".format(distance))

    if distance < 20:  # Adjust this value according to your desired obstacle detection range
        if moving_forward:  # Only take action if the robot is moving forward
            stop()
            rospy.sleep(0.5)
            turn_right()
            rospy.sleep(.5)
            move_forward()
            rospy.sleep(0.5)
    else:
        move_forward()

def motor_subscriber():
    # Initialize ROS node
    rospy.init_node('motor_subscriber', anonymous=True)
    rospy.Subscriber('distance', Float32, callback)

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:

        motor_subscriber()
    except rospy.ROSInterruptException:
        pass
