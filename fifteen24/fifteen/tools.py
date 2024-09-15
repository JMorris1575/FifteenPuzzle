import random

def generate_puzzle(size):
    grid = []
    for i in range(1, size * size):
        grid.append(i)
    grid.append(0)
    solution = grid.copy()      # create an independent copy of the original grid
    _scramble(grid, size, random.randint(100, 1000))      # scramble the grid through a random number of tile movements
    return grid, solution

def _scramble(grid, size, n):
    for i in range(n):
        blank_index = grid.index(0)
        movement = _get_movement(blank_index, size)              # get a random choice of possible motions for the blank
        _swap(grid, blank_index, movement)

def _get_movement(blank_index, size):
    """
    Determines possible one-tile "motions" of the blank and randomly selects one of them
    :param blank_index: The index position of the blank in the grid
    :return: a random choice of:
        +1 for moving the blank to the right
        -1 for moving the blank to the left
        -size for moving the blank upward
        +size for moving the blank downward
    """
    displacements = []
    if (blank_index + 1) % size != 0:
        displacements.append(1)
    if (blank_index - 1) % size != size - 1:
        displacements.append(-1)
    if (blank_index - size) >= 0:
        displacements.append(-size)
    if (blank_index + size) <= size * size - 1:
        displacements.append(size)
    return random.choice(displacements)

def _swap(grid, blank_index, disp):
    '''
    swaps the blank with the tile at the location specified by disp
    :param disp: an integer -1 and 1 for left and right, -4 and 4 for up and down
    :return: None
    '''
    new_loc = blank_index + disp
    temp = grid[new_loc]
    grid[blank_index] = temp
    grid[new_loc] = 0
