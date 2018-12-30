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


board = LightsOutBoard(8, 4)

board.displayBoard()

board.toggleCell(0,0)
board.displayBoard()

board.toggleCell(1,1)
board.displayBoard()

board.generateRandomBoard()
board.displayBoard()

board.toggleCell(0,0)
board.displayBoard()

board.toggleCell(1,1)
board.displayBoard()


board = LightsOutBoard(8,4,1)
board.displayBoard()
print(board.hasWon(True))
