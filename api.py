import flask
from flask import request, jsonify
import numpy as np
from numpy.random import default_rng


app = flask.Flask(__name__)
app.config["DEBUG"] = True

matrix_size = 3
shipNum = 3

# generate 3 random numbers between 0 and 8 with no duplicates
ships = default_rng().choice(9, size=3, replace=False)

# which value goes into square i,j
# creates a grid where a set number of ships are placed randomly with the shipNum "1"s and the rest as "0"
matrix = [[int((matrix_size * j + i in ships) == True)
    for i in range(matrix_size)] for j in range(matrix_size)]

array_matrix = np.array(matrix)
print (array_matrix)

@app.route('/fire', methods=['POST'])
def fire():
    print(request.json)
    x = request.json["x"]
    y = request.json["y"]
    print(x)
    isHit = matrix[x][y]
    print(isHit)
    response = {
        "hit": bool(isHit),
        "coordinates": "{0}, {1}".format(x, y)
    }
    return response

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

app.run(host="0.0.0.0")