# gameOfLife.py
from cmu_graphics import *


class GameOfLife:
    def __init__(self, cellSize):
        self.cellSize = cellSize
        self.cells = {}

    # Adds cells if clicked and remove cells if there is already a cell
    def toggleCell(self, x, y):
        if (x, y) in self.cells:
            del self.cells[(x, y)]
        else:
            self.cells[(x, y)] = True

    # Draws the grid and the cells here instead of the main python for better debug
    def draw(self, app):
        for x, y in self.cells:
            xPos = app.offsetX + app.width // 2 + x * app.gridSize
            yPos = app.offsetY + app.height // 2 + y * app.gridSize
            drawRect(xPos, yPos, app.gridSize, app.gridSize, fill="white")

    def step(self):
        newCells = {}
        neighborCounts = {}

        # Count neighbors for each live cell and their neighbors
        for x, y in self.cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx, dy) != (0, 0):  # Skip the cell itself
                        neighborX, neighborY = x + dx, y + dy
                        neighborCounts[(neighborX, neighborY)] = (
                            neighborCounts.get((neighborX, neighborY), 0) + 1
                        )

        # Apply the rules and logic of the Game of Life
        for position, count in neighborCounts.items():
            if count == 3 or (count == 2 and position in self.cells):
                newCells[position] = True

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
