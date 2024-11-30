# Predefined shapes in Conway's Game of Life
# I asked chatGPT to give me a few shapes that are well known and
# would last for a while before the cells become a dead state.

import random

# Block (Still Life)
block = {
    (0, 0): True,
    (0, 1): True,
    (1, 0): True,
    (1, 1): True,
}

# Beehive (Still Life)
beehive = {
    (1, 0): True,
    (2, 1): True,
    (2, 2): True,
    (1, 3): True,
    (0, 2): True,
    (0, 1): True,
}

# Loaf (Still Life)
loaf = {
    (1, 0): True,
    (2, 1): True,
    (2, 2): True,
    (1, 3): True,
    (0, 2): True,
    (0, 1): True,
    (3, 2): True,
}

# Boat (Still Life)
boat = {
    (0, 0): True,
    (0, 1): True,
    (1, 0): True,
    (1, 2): True,
    (2, 1): True,
}

# Tub (Still Life)
tub = {
    (1, 0): True,
    (0, 1): True,
    (2, 1): True,
    (1, 2): True,
}

# Blinker (Oscillator, Period 2)
blinker = {
    (0, 0): True,
    (1, 0): True,
    (2, 0): True,
}

# Toad (Oscillator, Period 2)
toad = {
    (0, 1): True,
    (0, 2): True,
    (1, 0): True,
    (1, 3): True,
    (2, 1): True,
    (2, 2): True,
}

# Beacon (Oscillator, Period 2)
beacon = {
    (0, 0): True,
    (0, 1): True,
    (1, 0): True,
    (1, 1): True,
    (2, 2): True,
    (2, 3): True,
    (3, 2): True,
    (3, 3): True,
}

# Pulsar (Oscillator, Period 3)
pulsar = {
    # Central block (with spacing)
    (2, 4): True,
    (3, 4): True,
    (4, 4): True,
    (2, 6): True,
    (3, 6): True,
    (4, 6): True,
    (2, 8): True,
    (3, 8): True,
    (4, 8): True,
    # Top arms
    (0, 5): True,
    (0, 6): True,
    (0, 7): True,
    (6, 5): True,
    (6, 6): True,
    (6, 7): True,
    # Bottom arms
    (8, 5): True,
    (8, 6): True,
    (8, 7): True,
    (14, 5): True,
    (14, 6): True,
    (14, 7): True,
}

# Glider (Spaceship)
glider = {
    (0, 2): True,
    (1, 0): True,
    (1, 2): True,
    (2, 1): True,
    (2, 2): True,
}

# Lightweight Spaceship (LWSS)
lwss = {
    (0, 1): True,
    (0, 4): True,
    (1, 0): True,
    (1, 4): True,
    (2, 4): True,
    (3, 0): True,
    (3, 1): True,
    (3, 2): True,
    (3, 3): True,
}

# Middleweight Spaceship (MWSS)
mwss = {
    (0, 1): True,
    (0, 5): True,
    (1, 0): True,
    (1, 5): True,
    (2, 5): True,
    (3, 0): True,
    (3, 1): True,
    (3, 2): True,
    (3, 3): True,
    (3, 4): True,
}

# Heavyweight Spaceship (HWSS)
hwss = {
    (0, 1): True,
    (0, 6): True,
    (1, 0): True,
    (1, 6): True,
    (2, 6): True,
    (3, 0): True,
    (3, 1): True,
    (3, 2): True,
    (3, 3): True,
    (3, 4): True,
    (3, 5): True,
}

# Pentadecathlon (Oscillator, Period 15)
pentadecathlon = {
    (1, 0): True,
    (1, 1): True,
    (1, 2): True,
    (1, 4): True,
    (1, 5): True,
    (1, 6): True,
    (0, 3): True,
    (2, 3): True,
}


# List of all shapes
shapes = [
    block,
    beehive,
    loaf,
    boat,
    tub,  # Still Lifes
    blinker,
    toad,
    beacon,
    pulsar,
    pentadecathlon,  # Oscillators
    glider,
    lwss,
    mwss,
    hwss,  # Spaceships
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
