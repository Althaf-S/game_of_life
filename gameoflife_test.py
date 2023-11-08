import gameoflife

def test_none_alive():
  alive = [[]]
  size = [3,4]
  my_array = gameoflife.generate_grid(size,alive)
  assert my_array == [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]
  
def test_one_alive():
  alive = [[2,1]]
  size = [3,4]
  my_array = gameoflife.generate_grid(size,alive)
  assert my_array == [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', 'A', '*', '*']]
  
def test_more_than_one_alive():
  alive = [[2,1],[1,1],[0,2]]
  size = [3,4]
  my_array = gameoflife.generate_grid(size,alive)
  assert my_array == [['*', '*', 'A', '*'], ['*', 'A', '*', '*'], ['*', 'A', '*', '*']]
  
def test_count_neighbours():
  x, y = 1, 1
  grid = [["*", "A", "*"],
          ["*", "A", "*"],
          ["*", "A", "A"]]
    
  count = gameoflife.neighbour_count(grid, x, y)
  assert count == 3
  
def game_rules():
  
  

  

