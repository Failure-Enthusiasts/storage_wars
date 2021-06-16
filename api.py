import flask
from flask import request, jsonify
import numpy as np
from numpy.random import default_rng
import requests

# api.py creates the board and ship, and you can update the board and ships through the API. 

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

# array_matrix = np.array(matrix)
print (matrix)

@app.route('/attack', methods=['POST'])
def attack():
    print("IT WORKED")
    print(request.json)
    """
    curl --location --request POST '0.0.0.0:5000/fire' \
--header 'Content-Type: application/json' \
--data-raw '{
    "x": 0,
    "y": 0
}'

    """

    x = request.json["x"]
    y = request.json["y"]
    url = 'http://0.0.0.0:5000/fire'
    json = {"x": x, "y": y}
    
    print(f"json: {json}")
    response = requests.post(url, json=json).json()

    #FIXME: Add grid response - just misses, hits
    
    return response
    

@app.route('/fire', methods=['POST'])
def fire():
    # do we need this as an endpoint? Could it just be a fcn
    print(request.json)
    print("FIYAH")

    x = request.json["x"]
    y = request.json["y"]
    state = _isHit(x,y)

    #FIXME: Response type doesn't work, may need to be JSON? Unsure.
    response = {
        "state": state,
        "coordinates": "{0}, {1}".format(x, y)
    }
    
    return response


def _isHit(x,y):

    """
    Ship states
    0: Empty
    1: Ship
    2: Miss
    3: Hit

    If x,y is a Miss or Hit, just pass it back unchanged.
    """

    if matrix[y][x] == 0:
        matrix[y][x] = 2

    if matrix[y][x] == 1:
        matrix[y][x] = 3

    return matrix[y][x]

@app.route('/cheat', methods=['POST'])
def cheat():
    response = { 
        "grid": str(matrix)
    }
    return response

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

app.run(host="0.0.0.0")





