#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# _cs = C

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
lm = Motor(Port.A)
rm = Motor(Port.B)
_cs = ColorSensor(Port.S4)
gs = GyroSensor(Port.S1)

import time
def color_test():
    cs = ColorWrapper(_cs, 8)
    while True:
        print(cs.color())
        print(cs.near_color(COLORS['BLUE']))
        time.sleep(.5)

import threading
def color_pass_counter(color):
    count = 0
    color_window = ColorWindow(10)
    # lm.run(300)
    # rm.run(300)

    while True:
        if (cs.color() != color and
        color_window.sustained(color, 5)):
            count += 1
            ev3.screen.print("color detected")
        color_window.add(cs.color())

        ev3.screen.print("count: " + str(count))

def accurate_color_test():
    color_wrapper = ColorWrapper(10)
    while True:
        color_window.add()
        ev3.screen.print(color_window.color())

import time
# Write your program here.
# color_pass_counter(Color.BLUE)
# ev3.screen.print(type(Color.BLACK))
accurate_color_test()
# ev3.screen.print(int(Color.BLUE))
# ev3.screen.print(int(Color.PURPLE))
time.sleep(5)
