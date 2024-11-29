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
        self.futurePrediction = False  # Toggle for future prediction feature

    # Check if a cell is within the border limits
    def isWithinBorder(self, x, y):
        return (
            -self.borderX <= x <= self.borderX - 1
            and -self.borderY <= y <= self.borderY - 1
        )

    # Adds cells if clicked and removes cells if there is already a cell, only within the border
    def toggleCell(self, x, y):
        if self.isWithinBorder(x, y):  # Only toggle if within the border
            if (x, y) in self.cells:
                del self.cells[(x, y)]
            else:
                self.cells[(x, y)] = True

    # Toggle the future prediction feature on or off
    def togglePrediction(self):
        self.futurePrediction = not self.futurePrediction

    # Count neighbors for all cells
    def countNeighbors(self):
        neighborCounts = {}
        for x, y in self.cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx, dy) != (0, 0):  # Skip the cell itself
                        neighborX, neighborY = x + dx, y + dy
                        if self.isWithinBorder(neighborX, neighborY):  # Check border
                            neighborCounts[(neighborX, neighborY)] = (
                                neighborCounts.get((neighborX, neighborY), 0) + 1
                            )
        return neighborCounts

    # Apply the Game of Life rules to decide the next state
    def applyRules(self, neighborCounts):
        newCells = {}
        for position in neighborCounts:
            count = neighborCounts[position]
            if (
                count == 3
                or (count == 2 and position in self.cells)
                and self.isWithinBorder(*position)
            ):
                newCells[position] = True
        return newCells

    # Draws the grid and the cells
    def draw(self, app):
        # If future prediction is enabled, visualize future states first
        if self.futurePrediction:
            self.drawFutureStates(app)

        # Draw current cells after predictions
        for x, y in self.cells:
            xPos = app.offsetX + app.width // 2 + x * app.gridSize
            yPos = app.offsetY + app.height // 2 + y * app.gridSize
            drawRect(xPos, yPos, app.gridSize, app.gridSize, fill="white")

    # Predicts and visualizes the future state of the cells
    def drawFutureStates(self, app):
        neighborCounts = self.countNeighbors()
        newCells = self.applyRules(neighborCounts)

        # Determine the radar's range
        startX = max(app.greenSquareX - 4, -self.borderX)
        endX = min(app.greenSquareX + 4, self.borderX - 1)
        startY = max(app.greenSquareY - 4, -self.borderY)
        endY = min(app.greenSquareY + 4, self.borderY - 1)

        # Draw the future states of the cells
        for x in range(startX, endX + 1):
            for y in range(startY, endY + 1):
                if (x, y) not in self.cells and (x, y) not in newCells:
                    # Future empty cells (green)
                    xPos = app.offsetX + app.width // 2 + x * app.gridSize
                    yPos = app.offsetY + app.height // 2 + y * app.gridSize
                    drawRect(xPos, yPos, app.gridSize, app.gridSize, fill="green")
                elif (x, y) in newCells:
                    # Future alive cells (red)
                    xPos = app.offsetX + app.width // 2 + x * app.gridSize
                    yPos = app.offsetY + app.height // 2 + y * app.gridSize
                    drawRect(xPos, yPos, app.gridSize, app.gridSize, fill="red")

    # Logic for the Game of Life mutations
    def step(self):
        neighborCounts = self.countNeighbors()
        newCells = self.applyRules(neighborCounts)
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
