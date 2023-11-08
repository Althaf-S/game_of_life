def display_grid(size,alive):
  #alive_row,alive_column = alive
  #print(alive_row,alive_column) 
  rows , columns = size
  positions = []
  for i in range(rows):
    for j in range(columns):
      positions.append([i,j])
      #print(positions)
  my_grid = [["*" for j in range (columns)]  for i in range (rows)]
  for i in alive:
    if i in positions:
      #print(i)
      alive_row,alive_column = i 
      my_grid[alive_row][alive_column] = "A"
  return str(my_grid).replace("[","").replace("]","").replace("'","").replace(",","")
#print(display_grid())
