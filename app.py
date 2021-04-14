import numpy as np
from numpy.random import default_rng
from random import randint

matrix_size = 3
shipNum = 3

# generate 3 random numbers between 0 and 8 with no duplicates
ships = default_rng().choice(9, size=3, replace=False)
print(ships)
# which value goes into square i,j
matrix = [[int((matrix_size * i + j in ships) == True) for i in range(matrix_size)] for j in range(matrix_size)]
print(matrix)

# rng = default_rng()
# numbers = rng.choice(9, size=9, replace=False)
# print(numbers)
#
# matrix =[
#           ["-", "-", "-"]
#         , ["-", "-", "-"]
#         , ["-", "-", "-"]
# ];
#
# for ind, num in enumerate(numbers, start=0):
#     x_coord = ind % 3
#     y_coord = ind // 3
#     if num <= 2:
#         matrix[y_coord][x_coord] = "x"
#     else:
#         matrix[y_coord][x_coord] = "-"
#
array_matrix = np.array(matrix)

print(array_matrix)

hits = 0

while hits < 3:
    attack_coord = input("Which coord to attack?")
    x_attack_coord = int(attack_coord[0])
    y_attack_coord = int(attack_coord[1])
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
