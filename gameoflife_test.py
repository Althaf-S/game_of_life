import gameoflife

def test_none_alive():
  alive = [6,6]
  size = [3,4]
  my_array = gameoflife.display_grid(size,alive)
  assert my_array == "* * * * * * * * * * * *"
  
def test_one_alive():
  alive = [2,1]
  size = [3,4]
  my_array = gameoflife.display_grid(size,alive)
  assert my_array == "* * * * * * * * * A * *"
  

