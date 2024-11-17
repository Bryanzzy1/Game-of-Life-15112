class GameOfLife:
    def __init__(self):
        self.cells = {}  # Dictionary to store active cells

    # Toggle a cell on or off.
    def toggleCell(self, x, y):

        if (x, y) in self.cells:
            del self.cells[(x, y)]  # Turn off the cell
        else:
            self.cells[(x, y)] = True  # Turn on the cell

    # Advance the Game of Life by one step.
    def step(self):

        newCells = {}
        neighborCounts = {}

        # Count neighbors for each active cell and their neighbors
        for x, y in self.cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx, dy) != (0, 0):
                        nx, ny = x + dx, y + dy
                        neighborCounts[(nx, ny)] = neighborCounts.get((nx, ny), 0) + 1

        # Apply the Game of Life rules
        for (x, y), count in neighborCounts.items():
            if count == 3 or (count == 2 and (x, y) in self.cells):
                newCells[(x, y)] = True

        self.cells = newCells

    # Clear all cells
    def clear(self):
        self.cells = {}
