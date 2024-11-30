from cmu_graphics import *


# The button UI class that handles in game button events
class ButtonUI:
    def __init__(
        self,
        app,
        pauseX,
        pauseY,
        resumeX,
        resumeY,
        settingsX,
        settingsY,
        titleX,
        titleY,
        buttonWidth,
        buttonHeight,
    ):
        self.app = app
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.pauseX = pauseX
        self.pauseY = pauseY
        self.resumeX = resumeX
        self.resumeY = resumeY
        self.settingsX = settingsX
        self.settingsY = settingsY
        self.titleX = titleX
        self.titleY = titleY

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

        # Draw the "Title" button (for returning to the title screen)
        drawRect(
            self.titleX,
            self.titleY,
            self.buttonWidth,
            self.buttonHeight,
            fill="lightGreen",
        )
        drawLabel(
            "Title",
            self.titleX + self.buttonWidth / 2,
            self.titleY + self.buttonHeight / 2,
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
            self.app.activeScreen = "settings"  # Navigate to settings screen

        # Check for "Title" button
        elif (
            self.titleX <= mouseX <= self.titleX + self.buttonWidth
            and self.titleY <= mouseY <= self.titleY + self.buttonHeight
        ):
            self.app.activeScreen = "start"  # Navigate back to the title screen

        return None
