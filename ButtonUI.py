from cmu_graphics import *


# The button UI class that handles in game button events
class ButtonUI:
    def __init__(self, app):
        self.pauseX = 20
        self.pauseY = 20
        self.resumeX = 20
        self.resumeY = 60
        self.buttonWidth = 80
        self.buttonHeight = 30
        self.settingsX = 20
        self.settingsY = 100
        self.titleX = 20
        self.titleY = 140
        self.app = app

    def drawButtons(self):
        # Draw the "Pause" button
        drawRect(
            self.pauseX,
            self.pauseY,
            self.buttonWidth,
            self.buttonHeight,
            fill="gray",
        )
        drawLabel(
            "Pause",
            self.pauseX + self.buttonWidth / 2,
            self.pauseY + self.buttonHeight / 2,
            size=12,
            align="center",
            fill="white",
        )

        # Draw the "Resume" button
        drawRect(
            self.resumeX,
            self.resumeY,
            self.buttonWidth,
            self.buttonHeight,
            fill="gray",
        )
        drawLabel(
            "Resume",
            self.resumeX + self.buttonWidth / 2,
            self.resumeY + self.buttonHeight / 2,
            size=12,
            align="center",
            fill="white",
        )

        # Draw the "Settings" button
        drawRect(
            self.settingsX,
            self.settingsY,
            self.buttonWidth,
            self.buttonHeight,
            fill="lightblue",
        )
        drawLabel(
            "Settings",
            self.settingsX + self.buttonWidth / 2,
            self.settingsY + self.buttonHeight / 2,
            size=12,
            align="center",
            fill="black",
        )

    def isClickOnButton(self, mouseX, mouseY):
        # Check for "Pause" button
        if (
            self.pauseX <= mouseX <= self.pauseX + self.buttonWidth
            and self.pauseY <= mouseY <= self.pauseY + self.buttonHeight
        ):
            self.app.running = False

        # Check for "Resume" button
        elif (
            self.resumeX <= mouseX <= self.resumeX + self.buttonWidth
            and self.resumeY <= mouseY <= self.resumeY + self.buttonHeight
        ):
            self.app.running = True

        # Check for "Settings" button
        elif (
            self.settingsX <= mouseX <= self.settingsX + self.buttonWidth
            and self.settingsY <= mouseY <= self.settingsY + self.buttonHeight
        ):
            self.app.startScreen.activeScreen = "settings"

        return None
