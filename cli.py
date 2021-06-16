import requests

# script for the CLI 

# start a cli
#(do this manually)

# wait for comamnds

menu_options = [
    'attack',
    'cheat',
]


def run_command(choice):
    if choice == 'attack':
        x, y = input('Enter coordinates to attack, separated by a space.').split(' ')
    
        url = 'http://0.0.0.0:6000/attack' #what's the container URL?
        json = {"x": x, "y": y}
    
    
        print(f"json: {json}")

        #FIXME: this request isn't quite right - API complains. Thought we solved this before? 
        response = requests.post(url, json=json).json()
        print(response)

        return response



while True:
    print(menu_options)
    choice = input("Choose your fighter")
    if choice in menu_options:
        run_command(choice)
    else:
        print('Command not recognized. Try again.')



# process commands

# commands themselves
