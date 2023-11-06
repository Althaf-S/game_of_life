import gameoflife
import numpy as np

def test_show_grid_in_terminal():
  row_size = 3
  column_size = 3
  my_array = gameoflife.show_grid_in_terminal(row_size,column_size)
  assert my_array == "* * *\n* * *\n* * *"
