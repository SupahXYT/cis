#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time, math, wrapper

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Create your objects here.
ev3 = EV3Brick()

# initialize motors and sensors 
lm = Motor(Port.A)
rm = Motor(Port.B)
# arm = Motor(Port.C)
_cs = ColorSensor(Port.S4)
cs = wrapper.ColorSensor(_cs)
gyro = GyroSensor(Port.S1)
# touch_sensor = TouchSensor(Port.S3)
# us = UltrasonicSensor(Port.S1)

def gyro_turn(deg: int):
    stop_deg = 0 # equivilant to a 'braking distance'
    turn_complete = False 
    gyro.reset_angle(0)

    lm.run(-100)
    rm.run(100)
    while not turn_complete:
        print(gyro.angle())
        if (gyro.angle() < 0 and (gyro.angle() < deg + stop_deg)
        or gyro.angle() > 0 and gyro.angle() > deg - stop_deg):
            turn_complete = True
    lm.hold()
    rm.hold()
axle_length = 115
wheel_diamter = 55 

def turn(theta_t: float):
    C_t = axle_length * math.pi
    C_w = wheel_diamter * math.pi 

    theta_w = (theta_t*C_t)/C_w 
    print(theta_w)
    lm.run_angle(200, theta_w, wait=False)
    rm.run_angle(200, -theta_w, wait=False)
    time.sleep(1)

wheel_circumference = math.pi * wheel_diamter

def move_distance(mm: float):
    lm.reset_angle(0)
    theta_wheel = 360 * mm / wheel_circumference
    lm.run(100)
    rm.run(100)
    print('angle to move wheel: ' + str(theta_wheel))

    while lm.angle() < theta_wheel:
        print(lm.angle())

    print('final angle: ' + str(lm.angle()))

    lm.hold()
    rm.hold()

def impolite_bumper():
    bumped = False 
    lm.run(3000)
    rm.run(3000)
    while not bumped:
        if touch_sensor.pressed():
            bumped = True

    lm.hold()
    rm.hold()
    # ev3.speaker.say("get out of the way")
    ev3.screen.print("get out of the way")
 
def correct():
    lm.stop()
    rm.stop()
    lm.run_time(-300, 1000, wait=False)
    rm.run_time(-300, 1000, wait=False)
    time.sleep(1.2)
    mturn(90)

def roomba():
    arm.hold()
    ev3.speaker.say("Initiating cleaning of current space")

    while True:
        lm.run(300)
        rm.run(300)
        if touch_sensor.pressed():
            lm.stop()
            rm.stop()
            lm.run_time(-300, 1000, wait=False)
            rm.run_time(-300, 1000, wait=False)
            time.sleep(1.1)
            mturn(90)


from random import random 
def randint(min, max):
    return round((max-min)*random()+min)

def proomba():
    arm.hold()
    ev3.speaker.say("Must clean now clean room move clean")

    while True:
        lm.run(300)
        rm.run(300)
        if touch_sensor.pressed():
            lm.stop()
            rm.stop()
            lm.run_time(-300, 1000, wait=False)
            rm.run_time(-300, 1000, wait=False)
            time.sleep(1.1)
            mturn(randint(-90, 90))

def color_sensor_one():
    while True: 
        ev3.screen.print(color_sensor.ambient())
        if color_sensor.ambient() < 3:
            ev3.speaker.say("the world has gone dark, my time has come")
        time.sleep(.1)

def mode_switcher():
    while True: 
        ev3.screen.print("entering ambient\nmode")
        ev3.speaker.say("entering ambient mode")
        while True: 
            ev3.screen.print(color_sensor.ambient())
            if touch_sensor.pressed():
                break
        ev3.screen.print("entering reflective\nmode")
        ev3.speaker.say("entering reflective mode")
        while True:
            ev3.screen.print(color_sensor.reflection())
            if touch_sensor.pressed():
                break

def tape_sensor():
    while True: 
        color = color_sensor.color()
        if color == Color.BLUE:
            ev3.screen.print("Color is blue")
        elif color == Color.YELLOW:
            ev3.screen.print("Color is yellow")
        else:
            ev3.screen.print("Color not blue or yellow")

def count_blue():
    previous_color = color_sensor.color()
    count = 0

    while True: 
        current_color = color_sensor.color()
        over_blue = (current_color == Color.BLUE)

        if(previous_color != current_color and over_blue):
            count += 1
        ev3.screen.print("Count: " + str(count))
        previous_color = current_color
        return True

def blue_yellow():
    lm.run(100)
    rm.run(100)
    colors.add(color_sensor.color())
    count = 0

    while True:
        current_color = color_sensor.color()
        if current_color == Color.YELLOW:
            break
        
        if(colors.get_last_color() != current_color 
            and colors.sustained(Color.BLUE)):
            count += 1
        ev3.screen.print("Count: " + str(count))
        colors.add(current_color)
    
    ev3.screen.print("Final count: " + str(count))
    lm.hold()
    rm.hold()

def no_contact():
    lm.run(300)
    rm.run(300)

    while True:
        if us.distance() < 100:
            lm.stop()
            rm.stop()

            lm.run_time(-300, 1000, wait=False)
            rm.run_time(-300, 1000, wait=False)
            time.sleep(1)
            mturn(90)
            lm.run(300)
            rm.run(300)

# direction enum
class Direction:
    left = -1
    right = 1

def seek(direction, color):
    angle_seek_limit = 90
    gyro.reset_angle(0)

    # seek first direction
    lm.run(30*direction)
    rm.run(30*-direction)
    while abs(gyro.angle()) < angle_seek_limit:
        if cs.near_color(color):
            lm.stop()
            rm.stop()

            lm.run(200)
            rm.run(200)
            return direction

    # seek second direction
    gyro.reset_angle(0)
    lm.run(30*-direction)
    rm.run(30*direction)
    while abs(gyro.angle()) < 2*angle_seek_limit:
        if cs.near_color(color):
            lm.stop()
            rm.stop()

            lm.run(200)
            rm.run(200)
            return -direction
    return -direction

def follow_line():
    tape_color = wrapper.Color.BLUE
    drive = wrapper.Drive(lm, rm)
    direction = Direction.left
    drive.run(200)

    while True:
        if(cs.near_color(tape_color)):
            pass
        else:
            direction = seek(direction, tape_color)

follow_line()