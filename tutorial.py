# Tutorial File

from cmu_graphics import *


class Tutorial:

    # Initialize variables
    def __init__(self):
        self.currentSlide = 0
        self.timeLimit = 30
        self.gridSize = 20
        self.difficulty = 1
        self.futurePredictionEnabled = False
        self.borderWidth = 5
        self.player = None

    # Next slide
    def nextSlide(self, app):
        self.currentSlide += 1
        if self.currentSlide > 3:
            self.currentSlide = 3

    # Previous Slide
    def prevSlide(self, app):
        self.currentSlide -= 1
        if self.currentSlide < 0:
            self.currentSlide = 0

    # Handles the key press
    def handleKeyPress(self, app, key):
        if key == "right":
            self.nextSlide(app)
        elif key == "left":
            self.prevSlide(app)

    # Handles mouse Press for back button
    def handleMousePress(self, app, mouseX, mouseY):
        if (
            app.width // 2 - 100 <= mouseX <= app.width // 2 + 100
            and app.height - 80 <= mouseY <= app.height - 40
        ):
            app.startScreen.activeScreen = "start"
            app.startGame = False
            app.settingScreen = False
            app.beginTutorial = False
            self.currentSlide = 0

    # Back to Start Button
    def drawBack(self):
        drawRect(
            app.width // 2 - 100,
            app.height - 80,
            200,
            40,
            fill="lightCoral",
            border="black",
        )
        drawLabel(
            "Back",
            app.width // 2,
            app.height - 60,
            size=20,
            fill="black",
        )

    def drawRulesVisualization(self, app):
        drawRect(0, 0, app.width, app.height, fill="lightGray")
        self.drawBack()
        drawLabel("Game of Life Rules", app.width // 2, 30, size=30, align="center")

        # Draw the upper grids
        self.drawGrid(app, app.width // 2 - 150, app.height // 2 - 200, 3, 3, 20)
        self.drawGrid(app, app.width // 2 + 100, app.height // 2 - 200, 3, 3, 20)

        # Dead to Alive
        # Right
        drawLabel(
            "Center Cell is dead",
            app.width // 2 - 120,
            app.height // 2 - 210,
            size=20,
        )
        drawRect(app.width // 2 - 130, app.height // 2 - 200, 20, 20)
        drawRect(app.width // 2 - 130, app.height // 2 - 160, 20, 20)
        drawRect(app.width // 2 - 110, app.height // 2 - 180, 20, 20)
        drawRect(app.width // 2 - 130, app.height // 2 - 180, 20, 20, fill="red")

        # Left
        drawLabel(
            "Alive",
            app.width // 2 + 130,
            app.height // 2 - 210,
            size=20,
        )
        drawRect(app.width // 2 + 120, app.height // 2 - 200, 20, 20)
        drawRect(app.width // 2 + 120, app.height // 2 - 160, 20, 20)
        drawRect(app.width // 2 + 140, app.height // 2 - 180, 20, 20)
        drawRect(app.width // 2 + 120, app.height // 2 - 180, 20, 20, fill="green")

        # Draw the lower grids
        self.drawGrid(app, app.width // 2 - 150, app.height // 2 - 100, 3, 3, 20)
        self.drawGrid(app, app.width // 2 + 100, app.height // 2 - 100, 3, 3, 20)

        # Alive to dead
        # Right
        drawLabel(
            "Alive",
            app.width // 2 - 120,
            app.height // 2 - 110,
            size=20,
        )
        drawRect(app.width // 2 - 150, app.height // 2 - 100, 20, 20)
        drawRect(app.width // 2 - 110, app.height // 2 - 100, 20, 20)
        drawRect(app.width // 2 - 150, app.height // 2 - 60, 20, 20)
        drawRect(app.width // 2 - 110, app.height // 2 - 60, 20, 20)
        drawRect(app.width // 2 - 130, app.height // 2 - 80, 20, 20, fill="green")

        # Left
        drawLabel(
            "Dead",
            app.width // 2 + 130,
            app.height // 2 - 110,
            size=20,
        )
        drawRect(app.width // 2 + 100, app.height // 2 - 100, 20, 20)
        drawRect(app.width // 2 + 140, app.height // 2 - 100, 20, 20)
        drawRect(app.width // 2 + 100, app.height // 2 - 60, 20, 20)
        drawRect(app.width // 2 + 140, app.height // 2 - 60, 20, 20)
        drawRect(app.width // 2 + 120, app.height // 2 - 80, 20, 20, fill="red")

        # Draw arrows
        self.drawArrow(
            app,
            app.width // 2 - 50,
            app.height // 2 - 170,
            app.width // 2 + 50,
            app.height // 2 - 170,
        )
        self.drawArrow(
            app,
            app.width // 2 - 50,
            app.height // 2 - 70,
            app.width // 2 + 50,
            app.height // 2 - 70,
        )

        # Draw the explanatory text
        drawLabel(
            "Each cell can be alive or dead.",
            app.width // 2,
            app.height // 2 + 40,
            size=18,
        )
        drawLabel(
            "A live cell survives to the next generation if it has 2 or 3 neighbors.",
            app.width // 2,
            app.height // 2 + 70,
            size=18,
        )
        drawLabel(
            "A dead cell becomes alive if it has exactly 3 neighbors.",
            app.width // 2,
            app.height // 2 + 100,
            size=18,
        )

    def drawArrow(self, app, startX, startY, endX, endY):
        drawLine(startX, startY, endX, endY, fill="black", width=2)
        arrowSize = 10

        # Define the points for the arrowhead triangle (always left to right)
        arrowPoint1 = (endX, endY)  # Tip of the arrow
        arrowPoint2 = (endX - arrowSize, endY - arrowSize / 2)  # Top corner
        arrowPoint3 = (endX - arrowSize, endY + arrowSize / 2)  # Bottom corner

        drawPolygon(
            arrowPoint1[0],
            arrowPoint1[1],
            arrowPoint2[0],
            arrowPoint2[1],
            arrowPoint3[0],
            arrowPoint3[1],
            fill="black",
        )

    def drawGrid(self, app, startX, startY, rows, cols, cellSize):
        for row in range(rows):
            for col in range(cols):
                x = startX + col * cellSize
                y = startY + row * cellSize
                drawRect(
                    x,
                    y,
                    cellSize,
                    cellSize,
                    fill="lightGray",
                    border="black",
                    borderWidth=1,
                )

    def drawArrow(self, app, startX, startY, endX, endY):
        drawLine(startX, startY, endX, endY, fill="black")
        arrowSize = 5
        drawPolygon(
            endX,
            endY,
            endX - arrowSize,
            endY - arrowSize,
            endX - arrowSize,
            endY + arrowSize,
            fill="black",
        )

    def drawPlayerIntroduction(self, app):
        drawRect(0, 0, app.width, app.height, fill="lightGray")
        self.drawBack()
        drawLabel("Player Introduction", app.width // 2, 30, size=30)
        drawLabel(
            "Your player is represented as a green square.",
            app.width // 2,
            100,
            size=18,
        )
        drawLabel(
            "You cannot touch the cells.",
            app.width // 2,
            140,
            size=18,
        )
        drawLabel(
            "Control with 'WASD' or the arrow keys",
            app.width // 2,
            180,
            size=18,
        )
        drawRect(app.width // 2 - 20, app.height // 2 - 20, 40, 40, fill="green")
        drawRect(
            app.width // 2 - 80,
            app.height // 2 - 80,
            40,
            40,
            fill="white",
            border="black",
        )
        drawRect(
            app.width // 2 - 140,
            app.height // 2 - 100,
            40,
            40,
            fill="white",
            border="black",
        )
        drawRect(
            app.width // 2 - 60,
            app.height // 2 + 40,
            40,
            40,
            fill="white",
            border="black",
        )
        drawRect(
            app.width // 2 + 20,
            app.height // 2 + 80,
            40,
            40,
            fill="white",
            border="black",
        )
        drawRect(
            app.width // 2 + 80,
            app.height // 2 - 20,
            40,
            40,
            fill="white",
            border="black",
        )

    def drawPlayerObjective(self, app):
        drawRect(0, 0, app.width, app.height, fill="lightGray")
        self.drawBack()
        drawLabel("Player's Objective", app.width // 2, 30, size=30)
        drawLabel(
            "Your objective is to visit all cells with a yellow border.",
            app.width // 2,
            100,
            size=18,
        )
        drawLabel(
            "You have limited time to complete the objective, so hurry up!",
            app.width // 2,
            140,
            size=18,
        )
        drawLabel(
            f"Time left: {self.timeLimit}", app.width // 2, 180, size=18, fill="red"
        )
        drawRect(app.width // 2 - 20, app.height // 2 - 20, 40, 40, fill="green")
        drawRect(
            app.width // 2 - 80,
            app.height // 2 + 20,
            40,
            40,
            fill=None,
            border="yellow",
        )
        drawRect(
            app.width // 2 - 100,
            app.height // 2 - 80,
            40,
            40,
            fill=None,
            border="yellow",
        )
        drawRect(
            app.width // 2 + 140,
            app.height // 2 - 20,
            40,
            40,
            fill=None,
            border="yellow",
        )
        drawRect(
            app.width // 2 - 120,
            app.height // 2 + 140,
            40,
            40,
            fill=None,
            border="yellow",
        )

    def drawSettingsSlide(self, app):
        drawRect(0, 0, app.width, app.height, fill="lightGray")
        self.drawBack()
        drawLabel("Settings", app.width // 2, 30, size=30)
        drawLabel(
            "You can explore the following settings:", app.width // 2, 100, size=18
        )
        drawLabel(f"Difficulty: {self.difficulty}", app.width // 2, 150, size=18)
        drawLabel(
            f"Future Prediction: {'Enabled' if self.futurePredictionEnabled else 'Disabled'}",
            app.width // 2,
            200,
            size=18,
        )
        drawLabel(f"Border Width: {self.borderWidth}", app.width // 2, 250, size=18)

    def drawTutorial(self, app):
        if self.currentSlide == 0:
            self.drawRulesVisualization(app)
        elif self.currentSlide == 1:
            self.drawPlayerIntroduction(app)
        elif self.currentSlide == 2:
            self.drawPlayerObjective(app)
        elif self.currentSlide == 3:
            self.drawSettingsSlide(app)
