# Import the time module to create a delay effect for a better user experience.
import time

# ASCII art intro
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

while True:
    # User chooses a direction
    direction = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ")
    
    if direction == "left":
        # User encounters a lake
        water = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ")

        if water == "wait":
            # User reaches the island safely
            door = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? ")

            if door == "red":
                print("It's a room full of fire. Game Over.")
            elif door == "yellow":
                # User finds the treasure and wins
                print("Congratulations! You found the treasure. You Win!")
                break
            elif door == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")

    # Ask the user if they want to play again
    choice = input("Do you want to play again? Type 'yes' or 'no': ")
    if choice.lower() != "yes":
        print("Thanks for playing. Goodbye!")
        break
