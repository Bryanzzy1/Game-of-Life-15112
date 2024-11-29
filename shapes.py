# Predefined shapes in Conway's Game of Life
# I asked chatGPT to give me a few shapes that are well known and
# would last for a while before the cells become a dead state.

import random

# Glider
glider = {
    (0, 0): True,
    (1, 0): True,
    (2, 0): True,
    (2, 1): True,
    (1, 2): True,
}

# Blinker (Oscillator)
blinker = {
    (0, 0): True,
    (1, 0): True,
    (2, 0): True,
}

# Toad (Oscillator)
toad = {
    (0, 1): True,
    (1, 0): True,
    (1, 1): True,
    (2, 0): True,
    (2, 1): True,
    (3, 0): True,
}

# Pulsar (Oscillator)
pulsar = {
    (5, 3): True,
    (5, 4): True,
    (5, 5): True,
    (5, 6): True,
    (5, 7): True,
    (3, 5): True,
    (4, 5): True,
    (6, 5): True,
    (7, 5): True,
    (3, 9): True,
    (4, 9): True,
    (6, 9): True,
    (7, 9): True,
    (5, 11): True,
    (5, 12): True,
    (5, 13): True,
    (5, 14): True,
    (5, 15): True,
    (9, 5): True,
    (9, 6): True,
    (9, 7): True,
    (9, 8): True,
    (9, 9): True,
}

# Lightweight spaceship
lws = {
    (1, 0): True,
    (2, 0): True,
    (0, 1): True,
    (0, 2): True,
    (2, 3): True,
}

# Diehard
dieHard = {
    (0, 0): True,
    (0, 1): True,
    (1, 1): True,
    (2, 1): True,
    (2, 2): True,
}

# Acorn
acorn = {
    (1, 1): True,
    (2, 1): True,
    (2, 2): True,
    (2, 3): True,
    (3, 0): True,
    (3, 1): True,
}

# Beacon
beacon = {
    (1, 0): True,
    (2, 0): True,
    (1, 1): True,
    (2, 1): True,
    (4, 2): True,
    (5, 2): True,
    (4, 3): True,
    (5, 3): True,
}

# R-pentomino
rPentomino = {
    (0, 0): True,
    (0, 1): True,
    (1, 0): True,
    (1, 2): True,
    (2, 1): True,
}

# Glider Gun
gliderGun = {
    (1, 0): True,
    (2, 0): True,
    (1, 1): True,
    (2, 1): True,
    (11, 0): True,
    (11, 1): True,
    (12, 0): True,
    (12, 1): True,
    (9, 2): True,
    (10, 2): True,
    (8, 3): True,
    (11, 4): True,
    (9, 5): True,
    (10, 5): True,
    (8, 6): True,
    (11, 7): True,
    (9, 8): True,
    (10, 8): True,
    (9, 10): True,
    (10, 10): True,
    (7, 11): True,
    (12, 11): True,
    (13, 12): True,
    (7, 13): True,
    (12, 13): True,
    (6, 14): True,
    (14, 14): True,
    (6, 15): True,
    (7, 16): True,
    (8, 16): True,
}

# List of all shapes
shapes = [
    glider,
    blinker,
    toad,
    pulsar,
    lws,
    dieHard,
    acorn,
    beacon,
    rPentomino,
    gliderGun,
]


# Randomize shape's position within the grid
def randomizeShape(shape, borderX, borderY):
    randomizedShape = {}
    # Randomly shift the shape within the given borders
    offsetX = random.randint(-borderX, borderX)
    offsetY = random.randint(-borderY, borderY)

    # Add shifted shape cells to the new grid position
    for (x, y), alive in shape.items():
        newX, newY = x + offsetX, y + offsetY
        if -borderX <= newX <= borderX - 1 and -borderY <= newY <= borderY - 1:
            randomizedShape[(newX, newY)] = alive

    return randomizedShape
