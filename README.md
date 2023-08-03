# AutomaticFloor Cleaning Robot using ROS
### Introduction
The Floor Cleaning Robot using ROS is an
innovative project that explores the integration
of robotics and automation technology into
everyday cleaning tasks. This project aims to
design and develop an autonomous robot
capable of cleaning
indoor environments, thereby revolutionizing
traditional floor cleaning methods. By
leveraging the power of the Robot Operating
System (ROS), the robot's capabilities are
enhanced, allowing seamless communication
between its various components for improved
efficiency and performance

### Objective
The system will be programmed in Python with rospy
libraries, enabling seamless communication between
Raspberry Pi and ROS nodes for effective control and
data exchange. Key goals include:
<ul>Building a robust robot platform integrating
Raspberry Pi for control.</ul>
<ul>
Implementing object detection for collision
avoidance during navigation.</ul>

<ul>Creating a structured ROS software architecture with Python and rospy. Developing path planning and cleaning algorithmsx
for efficient floor cleaning.</ul>
<ul>Integrating a vacuum mechanism for effective
cleaning.</ul>
<ul>Designing a user-friendly interface for easy
cleaning of the floor</ul>

### Working
<li>The Ultrasonic Sensor detects obstacles and relays data to
the Raspberry Pi 4.</li>
<li>The Raspberry Pi 4 processes the sensor data and
determines the optimal cleaning path, sending commands
to the L298N Motor Driver Module.</li>
<li>The Motor Driver Module controls the robot's movement,
allowing it to navigate around obstacles while cleaning
efficiently.</li>
<li>The mop and vacuum are activated by the Servo Motor,
providing a dual-cleaning mechanism for spotless floors.</li>
<li>The robot operates autonomously, maximizing cleaning
coverage and minimizing human intervention.</li>
