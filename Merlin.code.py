import math
import time
import array
import board
import busio
import audioio
import adafruit_trellis_express
import adafruit_adxl34x

time.sleep(10.0)

trellis = adafruit_trellis_express.TrellisM4Express(rotation=90)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

print('Starting up...')

# Clear all pixels
trellis.pixels._neopixel.fill((0, 0, 0))
trellis.pixels._neopixel.show()

import random

class LightsOutBoard:
    lightOffColor = (0, 0, 0)
    lighOnColor = (255, 255, 255)

    def __init__(self, xSize, ySize, initialValue = False):
        self.xSize = xSize
        self.ySize = ySize
        self.Board = [ [ initialValue for y in range(ySize) ] for x in range(xSize) ]

    def displayBoard(self):
        print("Board: %s" % ("Won" if self.hasWon() else "!Won"))
        for y in range(self.ySize):
            line = "%d: " % y
            for x in range(self.xSize):
                if self.Board[x][y]:
                    line = line + "X"
                else:
                    line = line + " "
            print(line)

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

    def hasWon(self, allSet = False):
        count = self.countOfSetCells()
        if count == 0 and allSet == False:
            return True
        if count == (self.xSize * self.ySize) and allSet == True:
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
                trellis.pixels._neopixel.pixels((y, x)) = lightOnColor if self.Board[x][y] else lightOffColor
        trellis.pixels._neopixel.show()

board = LightsOutBoard(8, 4)
board.displayBoard()

while True:
    print('In loop')
    stamp = time.monotonic()

    board.updateTrellis(trellis)
    board.generateRandomBoard()
    board.displayBoard()

    while time.monotonic() - stamp < 1.0:
        time.sleep(0.01)  # a little delay here helps avoid debounce annoyances

