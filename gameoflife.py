import random
import copy
import time

def initialize_grid(rows, cols):
    return [[random.choice([0, 1]) for i in range(cols)] for j in range(rows)]

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
def update_grid(grid):
    new_grid =  copy.deepcopy(grid)
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j]:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def game_of_life(rows, cols, generations):
    grid = initialize_grid(rows, cols)
    for _ in range(generations):
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.7)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    generations = int(input("No. of generations : "))
    game_of_life(rows, cols, generations)




