#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""


#import module 
from gameData import rooms


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      read [item]
      use [item]
      open [item]

    To Win: You must excape out the Garden gate!  Avoid the ghoul  and don't take too long, after 60 moves you're dead!!!!
    ''')
   


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')

    if currentRoom == 'Garden Gate':
        print("You are at the Garden Gate")
    else:    
        print('You are in the ' + currentRoom)
    # print room description- in kitchen and the ghoul exists decrease health by 10 each move
  
    if currentRoom == 'Garden Gate' and gate_open == True:
        print(rooms[currentRoom]['description2'])
    else: 
        print(rooms[currentRoom]['description'])  #if the ghoul is in the kitchen, print this
        if currentRoom == 'Kitchen' and 'ghoul' in rooms[currentRoom]['item']:
            print("ouch a ghoul smacked you and decreased your health by 10!")
    # print what the player is carrying
    print('Inventory: ', inventory)
    print('Health: ', health)
    print('Move Count: ', moves)
    print('Commands: go [direction], get, read, use, or open [item]')
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        #join items array
                if len(rooms[currentRoom]['item']) == 0:
                    print(" ")
                elif len(rooms[currentRoom]['item']) == 1:
                    print ('You see a ' + rooms[currentRoom]['item'][0])
                else:
                    items = ", ".join(rooms[currentRoom]['item'])
                    print('You see ' + items)
    print("---------------------------")
# initial health
health = 80

# an inventory, which is initially empty
inventory = []

#boolean to toggle off once key is used
gate_open = False

#total moves
moves = 0

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()
    moves += 1
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        # don't let them get the ghoul
        if move[1] == 'ghoul':
            print("You can't get the ghoul!!!")
        elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            rooms[currentRoom]['item'].remove(move[1])
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
   
   #if they type 'read' first, only the note in the bathroom can be read
    if move[0] == 'read':
        if move[1] not in inventory:
            print("Items not in your inventory can't be read")
        elif move[1] == 'note' and 'note' in inventory:
            print(rooms["Bathroom"]['message'])
        else:
            print(move[1] + "  can't be read")

    #use functionality. If they are at the garden gate with the key, they can see a secret message revealed and must answer correctly to win
    if move[0] == 'use':
        if move[1] == 'key' and currentRoom == 'Garden Gate' and move[1] in inventory:
            gate_open = True
            print("You opened the gate!")
        elif move[1] == 'potion' and move[1] in inventory:
            inventory.remove(move[1])
            health += 20
            print('You drank the potion and gained 20 health points!!!')
        elif move[1] == 'twinkie' and move[1] in inventory:
            inventory.remove(move[1])
            health+=10
            print("You ate the twinkie and gained 10 health points!!!!!")
        elif move[1] == 'muscle man' and currentRoom == 'Kitchen' and rooms[currentRoom]['item']:
            rooms[currentRoom]['item'].remove('ghoul')
            print("You used your muscle man on the ghoul and scared him away!!!!")
        elif move[1] == 'comb' and move[1] in inventory:
            print("You combed your hair.")
        elif move[1] == 'pet rock' and move[1] in inventory:
            print("You looked at  your pet rock and were filled with courage!")
        elif move[1] not in inventory:
            print("You can't use items not in your inventory")
        elif move[1] == 'muscle man' and 'muscle man' in inventory and currentRoom != 'Kitchen':
            print("You used your muscle man, but nothing happened")
        else:
            print(move[1], " can't be used.")
#open functionality - when boxes are opened remove them from inventory and replace them with key and pet rock
    if move[0] == 'open':
        if move[1] == 'mystery box 2' and move[1] in inventory:
            inventory.append('key')
            inventory.remove('mystery box 2')
            print('You opened mystery box 2 and found a key!!!')
        elif move[1] == 'mystery box 1' and move[1] in inventory:
            inventory.append('pet rock')
            inventory.remove('mystery box 1')
            print('You opened mystery box 1 and found a pet rock!!!')
        elif move[1] not in inventory:
            print('You can\'t open items not in your inventory')
        else:
            print(move[1], " can't be opened")
# decrease health by 10 for every move you make in the kitchen if the ghoul is present
    if currentRoom == 'Kitchen' and 'ghoul' in rooms[currentRoom]['item']:
        health -= 10
# die if health reaches 0 - game over
    if health == 0:
        print("Your health is zero, you died!  Game Over!!!!")
        break

# die if moves reach 60
    if moves == 60:
        print("You took too long to escape, you lose!!! Game Over!!!!")
        break

# final test- answer a riddle, if you answer wrong you die
    if gate_open == True and currentRoom == 'Garden Gate':
        riddleAnswer = input("Out of nowhere a muscular squirrel jumped in front of the gate and said 'If you want to leave this place alive, you must answer my riddle correctly.  What has five fingers and isn't alive?  ")
        if riddleAnswer.lower() == 'glove' or riddleAnswer.lower() == 'a glove':
            print("Correct, you escaped through the gate!!! You win!!")
            break
        else: 
            print("Wrong answer!!! The muscular squirrel gouges both of your eyes out with two especially sharp pecans!! Game over!!!")
            break
