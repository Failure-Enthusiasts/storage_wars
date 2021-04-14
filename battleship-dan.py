import numpy as np;
import random;

grid_width = 3
grid_height = 3
bomb_number = 4
minesArray = np.zeros(shape=(grid_height,grid_width))

while bomb_number > 0:
  i = random.randint(0,grid_width-1)
  j = random.randint(0,grid_height-1)
  if (minesArray[j][i] == 0):
    minesArray[j][i] = 1
    bomb_number = bomb_number - 1

print(minesArray)