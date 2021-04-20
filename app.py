import numpy as np
from numpy.random import default_rng
from random import randint

matrix_size = 3
shipNum = 3

# generate 3 random numbers between 0 and 8 with no duplicates
ships = default_rng().choice(9, size=3, replace=False)
# which value goes into square i,j
# creates a grid where a set number of ships are placed randomly with the shipNum "1"s and the rest as "0"
matrix = [[int((matrix_size * j + i in ships) == True) for i in range(matrix_size)] for j in range(matrix_size)]
# turn matrix into an array
array_matrix = np.array(matrix)
print (array_matrix)
# print(array_matrix)

hits = 0

while hits < 3:
    attack_coord = input("Which coord to attack?")
    y_attack_coord = int(attack_coord[0])
    x_attack_coord = int(attack_coord[1])
    if matrix[y_attack_coord][x_attack_coord] == 1:
        msg = "IT'S A HIT"
        matrix[y_attack_coord][x_attack_coord] = "x"
        hits += 1
        if hits == 3:
            msg = "YOU WIN!"
    else:
        msg = "Try again"

    print(msg)
    array_matrix = np.array(matrix)
    print(array_matrix)
