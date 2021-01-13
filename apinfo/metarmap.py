import ap


class Map:
    def __init__(self, airports):
        import board
        import neopixel
        import time

        brightness = 0.1
        np = neopixel.NeoPixel(board.D18, len(airports), brightness=brightness,
                               auto_write=True, pixel_order=neopixel.GRB)
        for i in range(0, len(airports), 1):
            np[i] = (235, 52, 214)
            time.sleep(.0001)
        for i in range(len(airports), 0, -1):
            np[i] = (52, 235, 220)
            time.sleep(.0001)
        for i in range(len(airports)):
            np[i] = ap.wx(airports[i]).color
        return

    def __repr__(self):
        return str('Setting Colors')
