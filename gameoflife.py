import random

def initialize_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(' '.join(['*' if cell else ' ' for cell in row]))
    print('\n')
def count_neighbors(grid, x, y):
    neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1),
                 (x, y-1),             (x, y+1),
                 (x+1, y-1), (x+1, y), (x+1, y+1)]
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i, j in neighbors:
        if 0 <= i < rows and 0 <= j < cols:
            count += grid[i][j]
    return count









