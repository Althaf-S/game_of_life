import gameoflife

def test_initialize_grid():
  rows = 10
  cols = 20

  grid = gameoflife.initialize_grid(rows, cols)

  assert len(grid) == rows
  assert len(grid[0]) == cols

  for row in grid:
    for cell in row:
      assert cell in [0, 1]

def test_count_neighbors():

  grid = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]

  assert gameoflife.count_neighbors(grid, 0, 0) == 1
  assert gameoflife.count_neighbors(grid, 0, 1) == 2
  assert gameoflife.count_neighbors(grid, 2, 2) == 1

def test_update_grid():

  grid = [[0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]]

  new_grid = gameoflife.update_grid(grid)

  expected_new_grid = [[0, 0, 0],
                       [1, 1, 1],
                       [0, 0, 0]]
  assert new_grid == expected_new_grid

