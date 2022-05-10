from pybricks import parameters
import math, time

class ColorSensor:
 
    color_hex_map = {
        parameters.Color.BLUE: (0x00, 0x00, 0xff),
        parameters.Color.GREEN: (0x00, 0xff, 0x00),
        parameters.Color.YELLOW: (0xff, 0xff, 0x00),
        parameters.Color.BROWN: (0xff, 0x86, 0x00),
        parameters.Color.ORANGE: (0xff, 0x55, 0x00),
        parameters.Color.RED: (0xff, 0x00, 0x00),
        parameters.Color.BLACK: (0x00, 0x00, 0x00),
        parameters.Color.WHITE: (0xff, 0xff, 0xff),
    }

    def __init__(self, color_sensor, size=10):
        self.window = []
        self.cs = color_sensor
        if size <= 0:
            raise ValueError("size must be greater than zero")
        self.size = size 

    def _populate(self):
        self.window = []
        for i in range(self.size):
            color = self.cs.color()
            if color is not None:
                self.window.append(color)

    def color(self):
        self._populate()
        if not self.window:
            return None

        avg = [0, 0, 0]
        hex_colors = [self.color_hex_map[color] for color in self.window]

        for color in hex_colors:
            avg[0] += color[0]
            avg[1] += color[1]
            avg[2] += color[2]

        return [i/len(self.window) for i in avg]

    def near_color(self, c2, radius=30):
        c1 = self.color()
        if c1 is None:
            return False

        distance = math.sqrt( 
            (c2[0]-c1[0])**2 + 
            (c2[1]-c1[1])**2 + 
            (c2[2]-c1[2])**2 )
        return (distance <= radius)

class Color:
    PURPLE = (0xff, 0x00, 0xff)
    BLUE = (0x00, 0x00, 0xff)
    GREEN = (0x00, 0xff, 0x00)
    YELLOW = (0xff, 0xff, 0x00)
    BROWN = (0xff, 0x86, 0x00)
    ORANGE = (0xff, 0x55, 0x00)
    RED = (0xff, 0x00, 0x00)
    BLACK = (0x00, 0x00, 0x00)
    WHITE = (0xff, 0xff, 0xff)

class Drive:
    def __init__(
        self, left_motor, right_motor, 
        axle_length=115, wheel_diamter=55):
        self.lm = left_motor
        self.rm = right_motor
        self.axle_length = axle_length
        self.wheel_diamter = wheel_diamter
        self.wheel_circumference = math.pi * wheel_diamter

    def turn(self, theta_t: float):
        C_t = self.axle_length * math.pi
        C_w = self.wheel_circumference

        theta_w = (theta_t*C_t)/C_w 
        self.lm.run_angle(200, theta_w, wait=False)
        self.rm.run_angle(200, -theta_w, wait=False)

        time.sleep(1)

    def move_distance(self, mm: float):
        self.lm.reset_angle(0)
        theta_wheel = 360 * mm / self.wheel_circumference
        self.lm.run_angle(theta_wheel)
        self.rm.run_angle(theta_wheel)

        self.lm.hold()
        self.rm.hold()

    def run(self, speed):
        self.lm.run(speed)
        self.rm.run(speed)

    def stop(self):
        self.lm.stop()
        self.rm.stop()

    def halt(self):
        self.lm.hold()
        self.rm.hold()
