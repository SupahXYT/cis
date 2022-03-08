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

import time
def stopping_test(speed: int):
    velocity = []
    distance_travelled = []
    turn_complete = False 
    left_motor.reset_angle()
    right_angle.reset_angle()

    left_motor.run()
    right_motor.run()
    while not turn_complete:
        if (gyro.angle() < 0 and (gyro.angle() < deg + stop_deg)
        or gyro.angle() > 0 and gyro.angle() > deg - stop_deg):
            turn_complete = True
        time.sleep(.1)
    left_motor.brake()
    right_motor.brake()

axle_length = 115
wheel_diamter = 55 

import time 
import math
def mturn(theta_t: float):
    C_t = axle_length * math.pi
    C_w = wheel_diamter * math.pi 

    theta_w = (theta_t*C_t)/C_w 
    left_motor.run_angle(200, theta_w, wait=False)
    right_motor.run_angle(200, -theta_w, wait=False)

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


def main():
    turn_in_place(360)
    # mturn(-90)
    time.sleep(2)
    # move_distance(100)

if __name__ == '__main__':
    main()

# A.run(100)
# B.run(100)
# C.run_time(3000, 2000, then=Stop.HOLD, wait=False)
# B.run_time(3000, 2000, then=Stop.HOLD)

