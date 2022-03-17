#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# initialize motors and sensors 
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm = Motor(Port.C)
gyro = GyroSensor(Port.S1)
touch_sensor = TouchSensor(Port.S4)

# drive = DriveBase(left_motor, right_motor)

def turn_in_place(deg: int):
    stop_deg = 0 # equivilant to a 'braking distance'
    turn_complete = False 
    gyro.reset_angle(0)

    left_motor.run(-100)
    right_motor.run(100)
    while not turn_complete:
        print(gyro.angle())
        if (gyro.angle() < 0 and (gyro.angle() < deg + stop_deg)
        or gyro.angle() > 0 and gyro.angle() > deg - stop_deg):
            turn_complete = True
    left_motor.hold()
    right_motor.hold()
axle_length = 115
wheel_diamter = 55 

import time 
import math
def mturn(theta_t: float):
    C_t = axle_length * math.pi
    C_w = wheel_diamter * math.pi 

    theta_w = (theta_t*C_t)/C_w 
    print(theta_w)
    left_motor.run_angle(200, theta_w, wait=False)
    right_motor.run_angle(200, -theta_w, wait=False)
    time.sleep(1)

wheel_circumference = math.pi * wheel_diamter

def move_distance(mm: float):
    left_motor.reset_angle(0)
    theta_wheel = 360 * mm / wheel_circumference
    left_motor.run(100)
    right_motor.run(100)
    print('angle to move wheel: ' + str(theta_wheel))

    while left_motor.angle() < theta_wheel:
        print(left_motor.angle())

    print('final angle: ' + str(left_motor.angle()))

    left_motor.hold()
    right_motor.hold()

def impolite_bumper():
    bumped = False 
    left_motor.run(3000)
    right_motor.run(3000)
    while not bumped:
        if touch_sensor.pressed():
            bumped = True

    left_motor.hold()
    right_motor.hold()
    # ev3.speaker.say("get out of the way")
    ev3.screen.print("get out of the way")
 
def correct():
    left_motor.stop()
    right_motor.stop()
    left_motor.run_time(-300, 1000, wait=False)
    right_motor.run_time(-300, 1000, wait=False)
    time.sleep(1.2)
    mturn(90)

def roomba():
    arm.hold()
    while True:
        left_motor.run(300)
        right_motor.run(300)
        if touch_sensor.pressed():
            correct()

from random import random 
def randint(min, max):
    return round((max-min)*random()+min)

def proomba():
    arm.hold()
    while True:
        left_motor.run(300)
        right_motor.run(300)
        if touch_sensor.pressed():
            left_motor.stop()
            right_motor.stop()
            left_motor.run_time(-300, 1000, wait=False)
            right_motor.run_time(-300, 1000, wait=False)
            time.sleep(1.2)
            direction = randint(0, 1)
            mturn(90*direction + -90*(not direction))

def main():
    # turn_in_place(360)
    # mturn(-90)
    # ev3.speaker.set_volume(40)
    # ev3.speaker.play_notes(['A4/8', 'A4/8', 'A4/16','C4/16','B4/16', 'A4/16', 
    # 'E4/8', 'E3/8', 'E3/16', 'G3/16#', 'F3/16#', 'E'], tempo=60)
    # impolite_bumper()
    proomba()
    time.sleep(10)
    # move_distance(100)
if __name__ == '__main__':
    main()

# A.run(100)
# B.run(100)
# C.run_time(3000, 2000, then=Stop.HOLD, wait=False)
# B.run_time(3000, 2000, then=Stop.HOLD)

