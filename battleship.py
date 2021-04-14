# grid = [
# [0,0,1],
# [1, 0, 0],
# [0,1,0]
# ]

# for row in grid: print(row.index(grid), row)

# x, y = input("Enter two coordinates? (Separate with a space!)").split()
# x = int(x) - 1
# y = int(y) - 1
# print([x, y])
# if y in range(0,len(grid)):
#     if x in range(0, len(grid[y])):
#         if grid[y][x] == 1:
#             print("YOU SUNK MY BATTLESHIP")
#         else:
#             print("HAH HAH!")
#     else:
#         print("X out of range")
# else: 
#     print("Y out of range")

import random

grid_size = 3
ship_count = 3
grid_pool = [0] * ((grid_size * grid_size) - ship_count) + [1] * ship_count
print(grid_pool)
random.shuffle(grid_pool)

print(grid_pool)
grid = [[grid_pool.pop() for i in range(grid_size)] for j in range(grid_size)]

for row in grid: print(row)