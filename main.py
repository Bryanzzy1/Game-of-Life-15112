from cmu_graphics import *
from gameOfLife import GameOfLife


# Initialize the app state.
def onAppStart(app):
    app.gameOfLife = GameOfLife()  # Game of Life simulation instance
    app.gridSize = 20  # Size of each grid cell
    app.paused = True  # Initial paused state of the simulation
    app.width, app.height = 600, 600  # App dimensions


# Draw the grid and all active cells.
def drawGrid(app):

    # Draw the grid lines
    for row in range(
        -app.height // (2 * app.gridSize), app.height // (2 * app.gridSize) + 1
    ):
        for col in range(
            -app.width // (2 * app.gridSize), app.width // (2 * app.gridSize) + 1
        ):
            xPos = app.width // 2 + col * app.gridSize
            yPos = app.height // 2 + row * app.gridSize
            drawRect(xPos, yPos, app.gridSize, app.gridSize, border="gray", fill=None)

    # Draw active cells
    for x, y in app.gameOfLife.cells:
        xPos = app.width // 2 + x * app.gridSize
        yPos = app.height // 2 + y * app.gridSize
        drawRect(xPos, yPos, app.gridSize, app.gridSize, fill="white")


# Handle mouse clicks to toggle cells.
def onMousePress(app, mouseX, mouseY):

    gridX = (mouseX - app.width // 2) // app.gridSize
    gridY = (mouseY - app.height // 2) // app.gridSize
    app.gameOfLife.toggleCell(gridX, gridY)


# Handle key presses for controlling the simulation.
def onKeyPress(app, key):

    if key == "space":
        app.paused = not app.paused  # Toggle pause state
    elif key == "r":
        app.gameOfLife.clear()  # Clear the grid


def onStep(app):
    """Advance the game if not paused."""
    if not app.paused:
        app.gameOfLife.step()


def redrawAll(app):
    """Redraw the entire screen."""
    drawRect(0, 0, app.width, app.height, fill="black")  # Background
    drawGrid(app)

    # Display pause or running state
    if app.paused:
        drawLabel("Paused", app.width // 2, 20, size=20, fill="yellow", align="center")
    else:
        drawLabel("Running", app.width // 2, 20, size=20, fill="green", align="center")


# Run the app
runApp(width=600, height=600)
