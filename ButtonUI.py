from cmu_graphics import *


class ButtonUI:
    def __init__(
        self, app, pauseX, pauseY, resumeX, resumeY, buttonWidth, buttonHeight
    ):
        self.app = app
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.pauseX = pauseX
        self.pauseY = pauseY
        self.resumeX = resumeX
        self.resumeY = resumeY

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

    def isClickOnButton(self, mouseX, mouseY):
        # Check if the click is within any button boundaries
        if (
            self.pauseX <= mouseX <= self.pauseX + self.buttonWidth
            and self.pauseY <= mouseY <= self.pauseY + self.buttonHeight
        ):
            return "pause"
        elif (
            self.resumeX <= mouseX <= self.resumeX + self.buttonWidth
            and self.resumeY <= mouseY <= self.resumeY + self.buttonHeight
        ):
            return "resume"
        return None

    def handleClick(self, mouseX, mouseY):
        # Check which button is clicked
        buttonClicked = self.isClickOnButton(mouseX, mouseY)
        if buttonClicked == "pause":
            self.app.running = False
        elif buttonClicked == "resume":
            self.app.running = True
