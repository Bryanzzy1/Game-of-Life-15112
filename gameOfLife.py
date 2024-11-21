# game_of_life.py
from cmu_graphics import *


class GameOfLife:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.cells = {}

    def toggle_cell(self, x, y):
        if (x, y) in self.cells:
            del self.cells[(x, y)]
        else:
            self.cells[(x, y)] = True

    def draw(self, app):
        for x, y in self.cells:
            x_pos = app.offset_x + app.width // 2 + x * app.grid_size
            y_pos = app.offset_y + app.height // 2 + y * app.grid_size
            drawRect(x_pos, y_pos, app.grid_size, app.grid_size, fill="white")

    def step(self):
        new_cells = {}
        neighbor_counts = {}

        # Step 1: Count neighbors for each live cell and their neighbors
        for x, y in self.cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx, dy) != (0, 0):  # Skip the cell itself
                        nx, ny = x + dx, y + dy
                        neighbor_counts[(nx, ny)] = neighbor_counts.get((nx, ny), 0) + 1

        # Step 2: Apply the rules of the Game of Life
        for position, count in neighbor_counts.items():
            if count == 3 or (count == 2 and position in self.cells):
                new_cells[position] = True

        self.cells = new_cells

    def live_count(self):
        return len(self.cells)

    def get_cell(self, x, y):
        # Returns True if the cell at (x, y) is alive (white), False otherwise
        return self.cells.get((x, y), False)

    def reset(self):
        # Clears all cells, effectively resetting the game state
        self.cells = {}
