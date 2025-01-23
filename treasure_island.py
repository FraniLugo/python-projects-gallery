print('''
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
choice1=input("You are stuck on an island, where do you want to go? Type 'left' or 'right'").lower()
if choice1=="right":
    print("You walk right and trip! Breaking your head on a coconut!")
if choice1=="left":
    Choice2=input("You encounter a large body of water, what do you want to do? Type 'swim' or 'wait'.").lower()
    if Choice2=="swim":
        print("You were attacked by a GIANT trout!!! GAME OVER... ")
    if Choice2=="wait":
        choice3=input(
            'long after waiting a submarine emerges from the water. The door opens, you walk inside and discover that there are three doors.What color do you choose? Type \'Red\' \'Yellow\' or \'Blue\'').lower()
        if choice3=='red':
            print("The red door swings open and you are pushed into open flames...GAME OVER")
        if choice3=='blue':
            print("The door swings open and you are pushed in. You find yourself falling out of the submarine and into the ocean")
        if choice3=='yellow':
            print("The door opens slowly, you peak inside but its too bright to see... scared you take a step in and find a treasure!!! CONGRATULATIONS - YOU WIN!")
        else:
            print("This is not an option.... GAME OVER")
        print("THANK YOU FOR PLAYING")

#Treasure island - first code 
# Treasure Island
#This is a simple text-based adventure game written in Python. The user navigates through choices to find a hidden treasure.
