import math
import time
import array
#import board
#import busio
#import audioio
import adafruit_trellis_express
import random

time.sleep(10.0) # Delay on startup...

trellis = adafruit_trellis_express.TrellisM4Express(rotation=90)

# Clear all pixels
fillTrellis(trellis, (0, 0, 0))

def fillTrellis(trellis,fillColor):
    trellis.pixels._neopixel.fill(fillColor)
    trellis.pixels._neopixel.show()

class LightsOutBoard:
    def __init__(self, xSize, ySize, initialValue = False):
        self.xSize = xSize
        self.ySize = ySize
        self.Board = [ [ initialValue for y in range(ySize) ] for x in range(xSize) ]
        self.lightOffColor = (0, 0, 0)
        self.lightOnColor = (255, 255, 255)

    def generateRandomBoard(self):
        for x in range(self.xSize):
            for y in range(self.ySize):
                self.Board[x][y] = random.choice([True, False])

    def countOfSetCells(self):
        count = 0
        for x in range(self.xSize):
            for y in range(self.ySize):
                if self.Board[x][y]:
                    count = count + 1
        return count

    def hasWon(self):
        if self.countOfSetCells() == 0:
            return True
        return False

    def toggleCell(self, x, y, toggleSurrounding = True):
        if x in range(self.xSize) and y in range(self.ySize):
            self.Board[x][y] = False if self.Board[x][y] else True
            if toggleSurrounding:
                self.toggleCell(x, y-1, False)
                self.toggleCell(x, y+1, False)
                self.toggleCell(x-1, y, False)
                self.toggleCell(x+1, y, False)

    def updateTrellis(self, trellis):
        for x in range(self.xSize):
            for y in range(self.ySize):
                trellis.pixels[(y, x)] = self.lightOnColor if self.Board[x][y] else self.lightOffColor

board = LightsOutBoard(8, 4)

while True:
    board.generateRandomBoard()         # Setup board
    board.updateTrellis(trellis)

    last_pressed = set()

    while board.hasWon() == False:
        stamp = time.monotonic()
        pressed = set(trellis.pressed_keys)

        for down in pressed - last_pressed:
            board.toggleCell(down[1], down[0])
            board.updateTrellis(trellis)

        last_pressed = pressed

        while time.monotonic() - stamp < 0.1:
            time.sleep(0.01)  # a little delay here helps avoid debounce annoyances

    # Player has won!!!
    for count in range(5):
        fillTrellis(trellis, (255, 0, 0))
        time.sleep(0.5)

        fillTrellis(trellis, (0, 0, 0))
        time.sleep(0.5)