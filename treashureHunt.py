print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You arrive at an abandoned island after a storm and you see the forest converging to 2 directions.where do you wanna go? left or right?\n")
if str.lower(direction) == "left":
    decision=input("You arrive at a river which seems to lead to some kind of a castle.what will you do swim across the river or wait for a boat? SWIM/WAIT\n")
    if str.upper(decision) == "WAIT":
        door=input("you arrive at a castle with 3 doors.Red,Yellow and Blue.which one do you choose?  red/yellow/blue\n")
        if str.upper(door) == "YELLOW":
            print("congrats u found the treasure!")
        elif str.upper(door)=="RED":
            print("you are burned by a room full of fire.GAME OVER")
        elif str.upper(door)=="BLUE":
            print("you are eaten by a wild beast inside the room.GAME OVER")
        else:
            print("you were overly confused and crocodiles crawled up the river banks and killed you.GAME OVER")
    else:
        print("you were attacked by a trout from the river.GAME OVER")
else:
    print("you fell into a deep pit.GAME OVER")
