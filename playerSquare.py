from cmu_graphics import *
from gameOfLife import GameOfLife

greenSquareColor = rgb(0, 255, 0)


# Draw the green square based on the values of app
def drawGreenSquare(app):
    if not app.gameOver:
        squareX = app.width // 2 + app.offsetX + app.greenSquareX * app.gridSize
        squareY = app.height // 2 + app.offsetY + app.greenSquareY * app.gridSize
        size = app.gridSize * app.animationScale
        drawRect(
            squareX + (app.gridSize - size) / 2,
            squareY + (app.gridSize - size) / 2,
            size,
            size,
            fill=greenSquareColor,
        )


# Animation the green square by making it shrink and enlarge in the new square
def animateGreenSquare(app):
    if app.animationScale > 0.3 and not app.backwardAnimation:
        app.animationScale -= 0.2
    else:
        app.greenSquareX = app.newGreenSquareX
        app.greenSquareY = app.newGreenSquareY
        app.backwardAnimation = True
        if app.animationScale < 0.8:
            app.animationScale += 0.2
        else:
            app.animationScale = 1
            app.animation = False
            app.backwardAnimation = False
            updateCamera(app)
            checkCollision(app)


# Handle pressing of the keys/movement
def keyPress(app, key):
    if key in ["left", "a"]:
        app.newGreenSquareX = app.greenSquareX - 1
        app.animation = True
    elif key in ["right", "d"]:
        app.newGreenSquareX = app.greenSquareX + 1
        app.animation = True
    elif key in ["up", "w"]:
        app.newGreenSquareY = app.greenSquareY - 1
        app.animation = True
    elif key in ["down", "s"]:
        app.newGreenSquareY = app.greenSquareY + 1
        app.animation = True


def moveGreenSquare(app, newX, newY):
    # Define grid boundaries (adjust as needed)
    gridLimitX = 10
    gridLimitY = 10

    # Check if the new position is within the allowed boundaries
    if -gridLimitX <= newX <= gridLimitX and -gridLimitY <= newY <= gridLimitY:
        app.newGreenSquareX = newX
        app.newGreenSquareY = newY
        app.animation = True

        # Check if the player is at the border
        if (
            newX >= gridLimitX - 1
            or newX <= -gridLimitX + 1
            or newY >= gridLimitY - 1
            or newY <= -gridLimitY + 1
        ):
            app.borderReached = True
        else:
            app.borderReached = False


# "update" the camera by shifting the grid opposite to the player's movement
def updateCamera(app):
    app.offsetX = (-app.greenSquareX - 1) * app.gridSize
    app.offsetY = (-app.greenSquareY - 1) * app.gridSize


# Check if the player square is on a cell that is alive
def checkCollision(app):
    if app.lifeSim.getCell(app.greenSquareX, app.greenSquareY):
        app.gameOver = True  # Set game over status


# Resets the player's position
def resetPlayerPosition(app):
    app.greenSquareX, app.greenSquareY = -1, -1  # Reset to starting position
    app.newGreenSquareX, app.newGreenSquareY = -1, -1
    app.offsetX, app.offsetY = 0, 0
    app.animationScale = 1
    app.animation = False
    app.backwardAnimation = False
