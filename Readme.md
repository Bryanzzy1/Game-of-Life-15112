# Survive: Game of LIFE
## Description
The project is an interactive simulation based on cellular automata, focusing on Conway’s Game of Life. In this simulation, the user interacts with a grid of cells that evolve according to simple rules. The player controls a “green square” that can move within the grid, with the objective of avoiding cell interactions that lead to its death. The game includes basic features such as zooming, pausing, and restarting the simulation.

The project adds a difficulty system that adjusts the speed at which the cells evolve, creating a more challenging experience as the player progresses. In addition, future cell states are indicated by highlighting cells in red based on the user’s choice and progression, showing where they will move or evolve next. This allows the player to strategize their movement. To further assist the player, there will be options where all valid movement areas are displayed in blue, indicating where the player can move safely. Lastly, game levels will be random. There will be a level design system where the cells will be placed at random based on a rule set that will allow the player to have fun and be challenged. The player will win if all cells reach a dead state or if the timer ends when they are alive. 

## Similar Projects
**Conway's Game of Life (Web-based)**: A web version of Conway's Game of Life that provides a basic implementation with step-by-step evolution. Inspiration: The game's ability to adjust simulation speed and display future states can inform the difficulty system and visualizations in the current project.

**Auto Cell: Game of Life (App)**:
This app provides a visually appealing and intuitive simulation of Conway's Game of Life. This app introduces several interesting features such as randomized start state, 3d stack view and intuitive user interface. Inspiration: The interface’s fluid design and easy-to-navigate grid inspired the project’s user interface and movement mechanics, the randomized start state provided the inspiration to add a player square in a grid of randomized cells.

## Run Instructions
Run the main.py file and make sure all files are in the same folder. No extra library beside cmu graphics need to be installed. To install cmu graphics please follow the instruction on the official CMU Computer Science Academy website: https://academy.cs.cmu.edu/desktop.

## Shortcut Commands
There are only one short cut command. When the user presses the 'Begin' button during the title screen and is loaded up in to a level, the can press 'space' instead of pressing the 'start' button. 
