#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time
import math

GPIO.setwarnings(False)
# Set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER_FRONT = 16
GPIO_ECHO_FRONT = 20

# Set up GPIO pins for the ultrasonic sensor
GPIO.setup(GPIO_TRIGGER_FRONT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_FRONT, GPIO.IN)

def get_distance():
    GPIO.output(GPIO_TRIGGER_FRONT, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_FRONT, False)
    StartTime_FRONT = time.time()
    StopTime_FRONT = time.time()

    while GPIO.input(GPIO_ECHO_FRONT) == 0:
        StartTime_FRONT = time.time()

    while GPIO.input(GPIO_ECHO_FRONT) == 1:
        StopTime_FRONT = time.time()

    TimeElapsed_FRONT = StopTime_FRONT - StartTime_FRONT
    distance_FRONT = math.floor((TimeElapsed_FRONT * 34300) / 2)
    print("distance =", distance_FRONT)
    return distance_FRONT

def distance_publisher():
    rospy.init_node('distance_publisher', anonymous=True)
    distance_pub = rospy.Publisher('distance', Float32, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        distance = get_distance()
        distance_pub.publish(distance)
        rate.sleep()

if __name__ == '__main__':
    try:
        distance_publisher()
    except rospy.ROSInterruptException:
        pass
