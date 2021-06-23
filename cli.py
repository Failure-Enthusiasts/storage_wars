import requests
import json as jdump

# script for the CLI 

# start a cli
#(do this manually)

# wait for comamnds

menu_options = [
    'attack',
    'cheat',
    'hello'
]


def run_command(choice):
    if choice == 'attack':
        x, y = input('Enter coordinates to attack, separated by a space.').split(' ')
        print(f"x: {x}")
        print(f"y: {y}")
        url = 'http://0.0.0.0:6000/attack' #what's the container URL?
        json = {"x": x, "y": y}
        headers = {'Content-Type': 'application/json'}

        print(f"json: {json}")

        #FIXME: this request isn't quite right - API complains. Thought we solved this before? 
        response = requests.post(url, data=json, headers=headers)
        # print(response.raw)
        print(type(response))
        print(response.json)
        

        return response


    elif choice == 'hello':
        print('hello there')
        # curl --location --request GET '127.0.0.1:6000/'   
        url = 'http://0.0.0.0:6000/'
        response = requests.get(url)
        status = response.status_code
        text = response.text
        print(f"response{response} status:{status} text:{text}")

        return text


while True:
    print(menu_options)
    choice = input("Choose your fighter")
    if choice in menu_options:
        run_command(choice)
    else:
        print('Command not recognized. Try again.')



# process commands

# commands themselves
