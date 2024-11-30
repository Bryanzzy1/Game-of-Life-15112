# The main file to run the entire game
# Press run file to play the game

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
from ButtonUI import ButtonUI
from gameObjective import GameObjective
from startScreen import StartScreen
from tutorial import Tutorial

# Colors
borderColor = rgb(204, 221, 230)
backgroundColor = rgb(58, 61, 66)

# Constants for grid configuration

zoomFactor = 1.1
minGridSize = 5
maxGridSize = 100
maxOffset = 10000


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


# Draw the red border overlay
def drawBorder(app):
    left = app.width // 2 + app.offsetX - app.boardLimitX * app.gridSize
    right = app.width // 2 + app.offsetX + app.boardLimitX * app.gridSize
    top = app.height // 2 + app.offsetY - app.boardLimitY * app.gridSize
    bottom = app.height // 2 + app.offsetY + app.boardLimitY * app.gridSize

    drawRect(
        left,
        top,
        right - left,
        bottom - top,
        fill=None,
        border="red",
        borderWidth=2,
    )


def redrawAll(app):
    if not app.startGame:
        if app.startScreen.activeScreen == "start":
            app.startScreen.drawStartScreen(app)
        elif app.startScreen.activeScreen == "settings":
            app.startScreen.drawSettingsScreen(app)
        elif app.beginTutorial:
            app.tutorial.drawTutorial(app)
        elif app.startScreen.activeScreen == "tutorial":
            app.startScreen.drawTutorialScreen(app)

    elif app.drawAllowed:
        # Draw the setting screen if that button is pressed
        if app.settingScreen:
            app.startScreen.drawSettingsScreen(app)
        else:
            drawBackground(app)
            app.lifeSim.draw(app)
            drawGreenSquare(app)
            drawGrid(app)
            app.objective.drawTargets(app)
            drawBorder(app)
            app.buttonUI.drawButtons()

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

                drawLabel(
                    f"Time Left: {app.countdownTimer}",
                    app.width // 2,
                    10,
                    fill="red",
                    size=25,
                    align="center",
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
    app.countdownTimer = 30 + app.difficulty * 10
    app.borderReached = False
    app.playerWins = False
    app.startOver = False
    app.stepTimer = 0
    app.animation = False
    app.backwardAnimation = False
    app.animationScale = 1
    app.beginTutorial = False

    # Reset player position and grid simulation
    resetPlayerPosition(app)
    app.lifeSim = GameOfLife(app.gridSize)

    # Reinitialize the game objective
    app.objective = GameObjective(app, app.difficulty)


# Draw the restart game labels
def drawGameOver(app):
    if app.playerWins:
        drawLabel(
            "You Win!",
            app.width // 2,
            app.height // 2,
            size=32,
            fill="lightGreen",
            bold=True,
        )
    else:
        drawLabel(
            "Game Over", app.width // 2, app.height // 2, size=32, fill="red", bold=True
        )
        drawLabel(
            "Avoid the white cells!",
            app.width // 2,
            app.height // 2 + 40,
            size=18,
            fill="red",
        )
    drawLabel(
        "Press 'R' to restart",
        app.width // 2,
        app.height // 2 + 70,
        size=18,
        fill="red",
    )


# Handle on mouse press events
def onMousePress(app, mouseX, mouseY):
    if not app.startGame:
        if app.beginTutorial:
            app.tutorial.handleMousePress(app, mouseX, mouseY)
        else:
            app.startScreen.handleMousePress(app, mouseX, mouseY)

        # Make sure the correct variable setting are passed
        app.borderWidth, app.difficulty = app.startScreen.getSettings()
        app.boardLimitX = app.borderWidth
        app.boardLimitY = app.borderWidth
        app.timer = 40 - app.difficulty * 6
        app.countdownTimer = 20 + app.difficulty * 10

    else:
        app.buttonUI.isClickOnButton(mouseX, mouseY)

        # Handles start Screen after the initial start screen
        if app.startScreen.activeScreen == "start":
            titleScreen(app)
        elif app.startScreen.activeScreen == "settings":
            app.settingScreen = True
            app.startScreen.handleMousePress(app, mouseX, mouseY)


# Handles the logic for player movement and some UI
def onKeyPress(app, key):
    if app.beginTutorial:
        app.tutorial.handleKeyPress(app, key)
    elif app.startGame and (app.playerWins or app.gameOver and key == "r"):
        restartGame(app)
    elif app.startGame and not app.gameOver:
        if key in ["+", "="]:
            adjustZoom(app, zoomFactor)
        elif key == "-":
            adjustZoom(app, 1 / zoomFactor)
        elif key == "space":
            app.running = not app.running
        if app.running:
            if key in ["left", "a"]:
                moveGreenSquare(app, app.greenSquareX - 1, app.greenSquareY)
            elif key in ["right", "d"]:
                moveGreenSquare(app, app.greenSquareX + 1, app.greenSquareY)
            elif key in ["up", "w"]:
                moveGreenSquare(app, app.greenSquareX, app.greenSquareY - 1)
            elif key in ["down", "s"]:
                moveGreenSquare(app, app.greenSquareX, app.greenSquareY + 1)


def onStep(app):
    if app.startGame:
        if not app.drawAllowed:
            initializeVariable(app)
        else:
            if app.startOver:
                restartGame(app)
            else:
                checkCollision(app)
                if not app.gameOver and app.objective.checkCompletion(app):
                    app.gameOver = True
                    app.playerWins = True

                if app.running:
                    # Controls how fast the cells are mutating/difficulty control
                    app.stepTimer += 1
                    if app.stepTimer % app.timer == 0:
                        # Countdown timer
                        if not app.gameOver and app.countdownTimer > 0:
                            app.countdownTimer -= 1
                        else:
                            app.gameOver = True
                        app.lifeSim.step()

                if app.animation:
                    animateGreenSquare(app)


def onAppStart(app):
    # Initial required variables
    app.drawAllowed = False
    app.startGame = False
    app.settingScreen = False
    app.futurePrediction = False
    app.beginTutorial = False
    app.tutorial = Tutorial()

    titleScreen(app)


def titleScreen(app):
    if not app.startGame:
        # Start Screen
        app.startScreen = StartScreen()


def initializeVariable(app):
    app.startOver = False
    app.borderWidth, app.difficulty = app.startScreen.getSettings()

    # Board Setup
    app.gridSize = 20
    app.boardLimitX = app.borderWidth
    app.boardLimitY = app.borderWidth
    app.borderReached = False
    app.lineThickness = 1.5

    # I start with -1,-1 here because that is the cell that is most centered
    app.greenSquareX, app.greenSquareY = -1, -1
    app.newGreenSquareX, app.newGreenSquareY = -1, -1

    # Difficulty
    app.timer = 40 - app.difficulty * 6
    app.countdownTimer = 20 + app.difficulty * 10
    app.objective = GameObjective(app, app.difficulty)

    # Simulation
    app.lifeSim = GameOfLife(app.gridSize)
    app.offsetX, app.offsetY = 0, 0
    app.gameOver = False
    app.playerWins = False

    # Animation
    app.animation = False
    app.backwardAnimation = False
    app.animationScale = 1
    app.running = False
    app.stepTimer = 0

    # Initialize the UI buttons with positions and sizes
    app.buttonUI = ButtonUI(app)
    app.drawAllowed = True


runApp(width=600, height=600)
