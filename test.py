from random import randint

N = 3
shipNum = 3
ships = set()

while len(ships) < shipNum:
    ships.add(randint(0, 8))

grid = [[int((N * i + j in ships) == True) for i in range(N)] for j in range(N)]

print(grid)