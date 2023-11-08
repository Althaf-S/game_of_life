def display_grid(size,alive):
  alive_row,alive_column = alive
  #print(alive_row,alive_column) 
  rows , columns = size
  positions = []
  for i in range(rows):
    for j in range(columns):
      positions.append([i,j])
  my_grid = [["*" for j in range (columns)]  for i in range (rows)]
  if alive in positions:
     my_grid[alive_row][alive_column] = "A"
  return str(my_grid).replace("[","").replace("]","").replace("'","").replace(",","")
#print(display_grid())
