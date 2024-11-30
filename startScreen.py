# Start Screen UIs
from cmu_graphics import *


class StartScreen:
    def __init__(self):
        self.activeScreen = "start"
        self.borderWidth = 10
        self.count = 0
        self.difficulty = 1
        self.difficultyOptions = [1, 2, 3, 4, 5]
        self.selectedDifficulty = 1
        self.showDropdown = False

    # Draws the initial start menu with options to begin the game or go to settings
    def drawStartScreen(self, app):
        drawLabel(
            "The Game of LIFE",
            app.width // 2,
            app.height // 4,
            size=40,
            bold=True,
            fill="Black",
            font="orbitron",
        )
        drawRect(
            app.width // 2 - 100,
            app.height // 2 - 50,
            200,
            40,
            fill="lightblue",
            border="black",
        )
        drawLabel(
            "Begin Game",
            app.width // 2,
            app.height // 2 - 30,
            font="orbitron",
            size=20,
            fill="black",
        )
        drawRect(
            app.width // 2 - 100,
            app.height // 2 + 10,
            200,
            40,
            fill="lightGreen",
            border="black",
        )
        drawLabel(
            "Settings",
            app.width // 2,
            app.height // 2 + 30,
            size=20,
            fill="black",
            font="orbitron",
        )

    # Draws the settings menu, allowing the player to adjust border width and difficulty
    def drawSettingsScreen(self, app):
        drawLabel(
            "Settings",
            app.width // 2,
            app.height // 4,
            size=40,
            bold=True,
            fill="white",
            font="orbitron",
        )

        # Input for border width
        drawLabel(
            "Border Width:",
            app.width // 2 - 100,
            app.height // 2 - 50,
            size=20,
            fill="black",
            align="right",
            font="orbitron",
        )
        drawRect(
            app.width // 2 + 10,
            app.height // 2 - 65,
            100,
            30,
            fill="white",
            border="black",
        )
        drawLabel(
            str(self.borderWidth),
            app.width // 2 + 60,
            app.height // 2 - 50,
            size=20,
            fill="black",
            font="orbitron",
        )

        # Dropdown for difficulty
        drawLabel(
            "Difficulty:",
            app.width // 2 - 100,
            app.height // 2 + 10,
            size=20,
            fill="black",
            align="right",
            font="orbitron",
        )
        drawRect(
            app.width // 2 + 10,
            app.height // 2 - 5,
            100,
            30,
            fill="white",
            border="black",
        )
        drawLabel(
            str(self.selectedDifficulty),
            app.width // 2 + 60,
            app.height // 2 + 10,
            size=20,
            fill="black",
            font="orbitron",
        )

        # Dropdown options
        if self.showDropdown:
            yOffset = 35
            for i in range(len(self.difficultyOptions)):
                optionY = app.height // 2 - 5 + yOffset * (i + 1)
                drawRect(
                    app.width // 2 + 10,
                    optionY,
                    100,
                    30,
                    fill="lightGray",
                    border="black",
                )
                drawLabel(
                    str(self.difficultyOptions[i]),
                    app.width // 2 + 60,
                    optionY + 15,
                    size=20,
                    fill="black",
                    font="orbitron",
                )

        # Have an option to go back to the game screen if needed
        if app.settingScreen:
            drawRect(
                app.width // 2 - 260,
                app.height - 80,
                100,
                40,
                fill="lightGreen",
                border="black",
            )
            drawLabel(
                "Back",
                app.width // 2 - 210,
                app.height - 60,
                size=20,
                fill="black",
                font="orbitron",
            )

        # Title button to go back to the start screen
        drawRect(
            app.width // 2 - 100,
            app.height - 80,
            200,
            40,
            fill="lightCoral",
            border="black",
        )
        drawLabel(
            "Title",
            app.width // 2,
            app.height - 60,
            size=20,
            fill="black",
            font="orbitron",
        )

    # Handles mouse presses for navigating the start and settings screens
    def handleMousePress(self, app, mouseX, mouseY):
        if self.activeScreen == "start":
            # Check for "Begin Game" button
            if (
                app.width // 2 - 100 <= mouseX <= app.width // 2 + 100
                and app.height // 2 - 50 <= mouseY <= app.height // 2 - 10
            ):
                self.activeScreen = "game"
                app.startOver = True
                app.startGame = True
                app.settingScreen = False

            # Check for "Settings" button
            elif (
                app.width // 2 - 100 <= mouseX <= app.width // 2 + 100
                and app.height // 2 + 10 <= mouseY <= app.height // 2 + 50
            ):
                self.activeScreen = "settings"

        elif self.activeScreen == "settings":
            # Check for border width input
            if (
                app.width // 2 + 10 <= mouseX <= app.width // 2 + 110
                and app.height // 2 - 65 <= mouseY <= app.height // 2 - 35
            ):
                self.count += 2
                self.borderWidth = (self.count) % 12 + 10

            # Check for dropdown toggle
            if (
                app.width // 2 + 10 <= mouseX <= app.width // 2 + 110
                and app.height // 2 - 5 <= mouseY <= app.height // 2 + 25
            ):
                self.showDropdown = not self.showDropdown

            # Check for dropdown options
            if self.showDropdown:
                yOffset = 35
                for i in range(len(self.difficultyOptions)):
                    optionY = app.height // 2 - 5 + yOffset * (i + 1)
                    if (
                        app.width // 2 + 10 <= mouseX <= app.width // 2 + 110
                        and optionY <= mouseY <= optionY + 30
                    ):
                        self.selectedDifficulty = self.difficultyOptions[i]
                        self.showDropdown = False

            # Check for "Back" button
            if (
                app.settingScreen
                and app.width // 2 - 260 <= mouseX <= app.width // 2 - 160
                and app.height - 80 <= mouseY <= app.height - 40
            ):
                self.activeScreen = "settings"
                app.startGame = True
                app.settingScreen = False

            # Check for "Title" button
            if (
                app.width // 2 - 100 <= mouseX <= app.width // 2 + 100
                and app.height - 80 <= mouseY <= app.height - 40
            ):
                self.activeScreen = "start"
                app.startGame = False

    # Returns the current settings
    def getSettings(self):
        return self.borderWidth, self.selectedDifficulty
