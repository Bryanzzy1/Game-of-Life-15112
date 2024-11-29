# gameOfLife.py
# Some inspiration from:
# -Code Noodle: https://www.youtube.com/watch?v=jGTCwCLRCrE
# -The Coding Train: https://www.youtube.com/watch?v=FWSR_7kZuYg
from cmu_graphics import *


class GameOfLife:
    def __init__(self, cellSize):
        self.cellSize = cellSize
        self.cells = {}
        self.borderX = 10  # Default horizontal border limit
        self.borderY = 10  # Default vertical border limit

    # Check if a cell is within the border limits
    def isWithinBorder(self, x, y):
        return -self.borderX <= x <= self.borderX and -self.borderY <= y <= self.borderY

    # Adds cells if clicked and removes cells if there is already a cell, only within the border
    def toggleCell(self, x, y):
        if self.isWithinBorder(x, y):  # Only toggle if within the border
            if (x, y) in self.cells:
                del self.cells[(x, y)]
            else:
                self.cells[(x, y)] = True

    # Draws the grid and the cells
    def draw(self, app):
        for x, y in self.cells:
            xPos = app.offsetX + app.width // 2 + x * app.gridSize
            yPos = app.offsetY + app.height // 2 + y * app.gridSize
            drawRect(xPos, yPos, app.gridSize, app.gridSize, fill="white")

    # Logic for the Game of Life mutations
    def step(self):
        newCells = {}
        neighborCounts = {}

        # Count neighbors for each live cell and their neighbors
        for x, y in self.cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx, dy) != (0, 0):  # Skip the cell itself
                        neighborX, neighborY = x + dx, y + dy
                        if self.isWithinBorder(neighborX, neighborY):  # Check border
                            neighborCounts[(neighborX, neighborY)] = (
                                neighborCounts.get((neighborX, neighborY), 0) + 1
                            )

        # Apply the rules of the Game of Life
        for position, count in neighborCounts.items():
            if self.isWithinBorder(*position):  # Only consider cells within the border
                if count == 3 or (count == 2 and position in self.cells):
                    newCells[position] = True
            else:
                del self.cells[(x, y)]

        self.cells = newCells

    # Get the total count of alive cells
    def liveCount(self):
        return len(self.cells)

    # Returns True if the cell at (x, y) is alive (white), False otherwise
    def getCell(self, x, y):
        return self.cells.get((x, y), False)

    # Clears all cells, effectively resetting the game state
    def reset(self):
        self.cells = {}
