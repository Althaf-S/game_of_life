def generate_grid(size = [3,4],alive = [[1,1]]):
  rows , columns = size
  positions = []
  for i in range(rows):
    for j in range(columns):
      positions.append([i,j])
  my_grid = [["*" for j in range (columns)]  for i in range (rows)]
  for i in alive:
    if i in positions:
      alive_row,alive_column = i 
      my_grid[alive_row][alive_column] = "A"
  return my_grid#str(my_grid).replace("[","").replace("]","").replace("'","").replace(",","")
print(generate_grid())


def display_grid():
  display_grid = generate_grid(size=[3,4],alive=[[1,1]])
  for i in display_grid:
    print(" ".join(i))
#display_grid() 

  
#print(display_grid())

#def game_rule():
#  my_grid = generate_grid() 
#  for i,j in enumerate(my_grid):
#    if "A" in j:
#       x,y = [i, j.index("A")]
       #if 
#print(game_rule())

def neighbour_count(grid,x,y):
  rows, columns = len(grid), len(grid[0])
  neighbours = [(x-1, y-1), (x-1, y), (x-1, y+1),(x, y-1),(x, y+1),(x+1, y-1), (x+1, y), (x+1, y+1)]
  count = 0
  for i, j in neighbours:
     if grid[i][j] == "A":#if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
           count += 1
  return count
    
  
         
