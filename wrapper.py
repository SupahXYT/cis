from enum import Enum

def _sqrt(n):
    return n**1/2

class ColorSensor:
 
    color_hex_map = {
        Color.PURPLE: (0xff, 0x00, 0xff),
        Color.BLUE: (0x00, 0x00, 0xff),
        Color.GREEN: (0x00, 0xff, 0x00),
        Color.YELLOW: (0xff, 0xff, 0x00),
        Color.BROWN: (0xff, 0x86, 0x00),
        Color.ORANGE: (0xff, 0x55, 0x00),
        Color.RED: (0xff, 0x00, 0x00),
        Color.BLACK: (0x00, 0x00, 0x00),
        Color.WHITE: (0xff, 0xff, 0xff),
    }

    def __init__(self, color_sensor, size):
        self.window = []
        self.cs = color_sensor
        if max <= 0:
            raise ValueError("max must be greater than zero")
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

        distance = sqrt( 
            (c2[0]-c1[0])**2 + 
            (c2[1]-c1[1])**2 + 
            (c2[2]-c1[2])**2 )
        return (distance <= radius)

class Color(Enum):

    PURPLE = (0xff, 0x00, 0xff)
    BLUE = (0x00, 0x00, 0xff)
    GREEN = (0x00, 0xff, 0x00)
    YELLOW = (0xff, 0xff, 0x00)
    BROWN = (0xff, 0x86, 0x00)
    ORANGE = (0xff, 0x55, 0x00)
    RED = (0xff, 0x00, 0x00)
    BLACK = (0x00, 0x00, 0x00)
    WHITE = (0xff, 0xff, 0xff)