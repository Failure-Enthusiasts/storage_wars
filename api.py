import flask
# from flask import session

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# # Duncan's 
# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# Brad's
f = open("my_hp.dat", "w")
f.write("10")
f.close()

@app.route('/', methods=['GET'])
def home():
    f = open("my_hp.dat", "r")
    my_hp = int(f.read())
    f.close()

    f = open("my_hp.dat", "w")
    f.write(str(my_hp - 1))
    f.close()
    
    # return "<h1> Distant Reading Archive</h1><p> my_hp = "+ str(my_hp) +" This site is a prototype API for distant reading of science fiction novels.</p>"
    return 'Hellllllo!'
app.run()