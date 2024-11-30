from cmu_graphics import *
import random


# Game objective files
class GameObjective:
    def __init__(self, app, difficulty):
        self.difficulty = difficulty
        self.targetSquares = []
        self.generateTargets(app)

    # Generates random yellow squares within the grid
    def generateTargets(self, app):
        self.targetSquares = []
        numTargets = self.difficulty * 2

        for _ in range(numTargets):
            placed = False
            while not placed:
                # Generate a random position within the grid's borders
                x = random.randint(-app.boardLimitX + 1, app.boardLimitX - 1)
                y = random.randint(-app.boardLimitY + 1, app.boardLimitY - 1)

                # Ensure the square is not overlapping an existing target or the player's start
                if (x, y) not in self.targetSquares and (x, y) != (
                    app.greenSquareX,
                    app.greenSquareY,
                ):
                    self.targetSquares.append((x, y))
                    placed = True

    # Draws the yellow squares on the grid.
    def drawTargets(self, app):
        for x, y in self.targetSquares:
            screenX = app.width // 2 + app.offsetX + x * app.gridSize
            screenY = app.height // 2 + app.offsetY + y * app.gridSize
            drawRect(
                screenX,
                screenY,
                app.gridSize,
                app.gridSize,
                fill=None,
                border="yellow",
                borderWidth=2,
            )

    # Checks if the player has visited all the target squares.
    def checkCompletion(self, app):
        playerPos = (app.greenSquareX, app.greenSquareY)
        if playerPos in self.targetSquares:
            # Mark this square as visited
            self.targetSquares.remove(playerPos)

        # If all targets are cleared, the player wins
        return len(self.targetSquares) == 0
