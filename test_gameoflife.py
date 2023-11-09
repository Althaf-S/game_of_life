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



