import numpy as np;
import random;

grid_width = 3
grid_height = 3
ships_placed = 4
array = np.zeros(shape=(grid_height,grid_width))

while ships_placed > 0:
  i = random.randint(0,grid_width-1)
  j = random.randint(0,grid_height-1)
  if (array[j][i] == 0):
    array[j][i] = 1
    ships_placed = ships_placed - 1

print(array)