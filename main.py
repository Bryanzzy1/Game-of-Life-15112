from cmu_graphics import *
from gameOfLife import GameOfLife
from playerSquare import (
    drawGreenSquare,
    animateGreenSquare,
    updateCamera,
    resetPlayerPosition,
    checkCollision,
    moveGreenSquare,
)

# Colors
borderColor = rgb(204, 221, 230)  # Light blue for the grid lines
backgroundColor = rgb(58, 61, 66)  # Dark grey for the background

# Constants for grid configuration
gridSize = 20
zoomFactor = 1.1
minGridSize = 5
maxGridSize = 100
maxOffset = 10000
app.lineThickness = 1.5


def drawGrid(app):
    cols = int(app.width // app.gridSize)
    rows = int(app.height // app.gridSize)

    # Adjust start and end columns/rows to center the grid
    startCol = -cols // 2 - int(app.offsetX / app.gridSize)
    endCol = cols // 2 - int(app.offsetX / app.gridSize)
    startRow = -rows // 2 - int(app.offsetY / app.gridSize)
    endRow = rows // 2 - int(app.offsetY / app.gridSize)

    # Draw vertical grid lines
    for col in range(startCol, endCol + 1):
        x = app.width // 2 + app.offsetX + col * app.gridSize
        drawLine(x, 0, x, app.height, fill=borderColor, lineWidth=app.lineThickness)

    # Draw horizontal grid lines
    for row in range(startRow, endRow + 1):
        y = app.height // 2 + app.offsetY + row * app.gridSize
        drawLine(0, y, app.width, y, fill=borderColor, lineWidth=app.lineThickness)


def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill=backgroundColor)


# Shift the entire grid so that the playerSquare stays center
def adjustZoom(app, factor):
    newGridSize = app.gridSize * factor
    if minGridSize <= newGridSize <= maxGridSize:
        app.offsetX = app.offsetX * factor
        app.offsetY = app.offsetY * factor
        app.gridSize = newGridSize
        updateCamera(app)


def redrawAll(app):
    drawBackground(app)
    drawGreenSquare(app)
    drawGrid(app)
    app.lifeSim.draw(app)

    if app.gameOver:
        drawGameOver(app)
    else:
        drawLabel(
            f"Live Cells: {app.lifeSim.liveCount()}",
            app.width - 100,
            10,
            fill="red",
            size=25,
        )

    # Display "border reached!" message if the player has reached the border
    if app.borderReached:
        drawLabel(
            "Border Reached!",
            app.width // 2,
            app.height // 2,
            size=40,
            fill="red",
            bold=True,
        )


# Restart the game
def restartGame(app):
    app.gameOver = False
    app.running = False
    resetPlayerPosition(app)
    app.lifeSim.reset()


# Draw the restart game labels
def drawGameOver(app):
    drawLabel(
        "Game Over", app.width // 2, app.height // 2, size=32, fill="red", bold=True
    )
    drawLabel(
        "Avoid the white cells!",
        app.width // 2,
        app.height // 2 + 40,
        size=18,
        fill="white",
    )
    drawLabel(
        "Press 'R' to restart",
        app.width // 2,
        app.height // 2 + 70,
        size=18,
        fill="white",
    )


# Handle on mouse press events
def onMousePress(app, mouseX, mouseY):
    if not app.userInputEnabled:
        return

    gridX = (mouseX - app.offsetX - app.width // 2) // app.gridSize
    gridY = (mouseY - app.offsetY - app.height // 2) // app.gridSize
    app.lifeSim.toggleCell(gridX, gridY)


# Handles the logic for player movement and some UI
def onKeyPress(app, key):
    if app.gameOver and key == "r":
        restartGame(app)
    elif not app.gameOver:
        if key in ["+", "="]:
            adjustZoom(app, zoomFactor)
        elif key == "-":
            adjustZoom(app, 1 / zoomFactor)
        elif key == "space":
            app.running = not app.running
        elif key in ["left", "a"]:
            moveGreenSquare(app, app.greenSquareX - 1, app.greenSquareY)
        elif key in ["right", "d"]:
            moveGreenSquare(app, app.greenSquareX + 1, app.greenSquareY)
        elif key in ["up", "w"]:
            moveGreenSquare(app, app.greenSquareX, app.greenSquareY - 1)
        elif key in ["down", "s"]:
            moveGreenSquare(app, app.greenSquareX, app.greenSquareY + 1)


def onStep(app):
    checkCollision(app)
    if app.running:
        # Controls how fast the cells are mutating/difficulty control
        app.stepTimer += 1
        if app.stepTimer % app.difficulty == 0:
            app.lifeSim.step()

    if app.animation:
        animateGreenSquare(app)


def onAppStart(app):
    # Board
    app.lifeSim = GameOfLife(gridSize)
    app.gridSize = gridSize
    app.offsetX, app.offsetY = 0, 0
    app.userInputEnabled = True
    app.gameOver = False
    # I start with -1,-1 here because that is the cell that is most centered
    app.greenSquareX, app.greenSquareY = -1, -1
    app.newGreenSquareX, app.newGreenSquareY = -1, -1

    # Animation
    app.animation = False
    app.backwardAnimation = False
    app.animationScale = 1
    app.running = False
    app.stepTimer = 0
    app.difficulty = 30
    app.borderReached = False


runApp(width=600, height=600)
