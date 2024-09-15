from random import choice

grid = None

def set_grid():
    global grid
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def display_grid():
    for y in range(4):
        row = ''
        for x in range(4):
            if grid[4 * y + x] == 0:
                row += '    '
            else:
                row += '{0:4}'.format(grid[4 * y + x])
        print(row)
    print()

def get_zero_displacement(loc):
    displacements = []
    if (loc + 1) % 4 != 0:
        displacements.append(1)
    if (loc - 1) % 4 != 3:
        displacements.append(-1)
    if (loc - 4) >= 0:
        displacements.append(-4)
    if (loc + 4) <= 15:
        displacements.append(4)
    return choice(displacements)

def swap(zero_loc, disp):
    '''
    swaps the zero with the item at the location specified by disp
    :param disp: an integer -1 and 1 for left and right, -4 and 4 for up and down
    :return: None
    '''
    new_loc = zero_loc + disp
    temp = grid[new_loc]
    grid[zero_loc] = temp
    grid[new_loc] = 0

def scramble_grid(n):
    for i in range(n):
        zero_loc = grid.index(0)
        zero_disp = get_zero_displacement(zero_loc)
        swap(zero_loc, zero_disp)

def solved():
    for i in range(15):
        if grid[i] != i + 1:
            return False
    return True

def move(dir):
    zero_loc = grid.index(0)
    # the user enters the direction for a tile to move, this translates that to the "motion" of the blank
    if dir == 'w' and (zero_loc + 4) <= 15:
        swap(zero_loc, 4)
    elif dir == 's' and (zero_loc - 4) >= 0:
        swap(zero_loc, -4)
    elif dir == 'a' and (zero_loc + 1) % 4 != 0:
        swap(zero_loc, 1)
    elif dir == 'd' and (zero_loc - 1) % 4 != 3:
        swap(zero_loc, -1)
    else:
        print("That won't work.")


set_grid()
scramble_grid(500)
display_grid()

while not solved():
    dir = 'x'
    while dir not in ('wsad'):
        dir = input("Up (w), Down (s), Left (a) or Right (d)? ")
        if dir == '':
            dir = 'x'
    move(dir)
    display_grid()
print('\nYou got it!')