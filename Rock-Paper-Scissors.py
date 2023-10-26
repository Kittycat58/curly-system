'''
1 -> Rock
2 -> Papers
3 -> Scissors

'''
import random
system = random.randint(1,3)
print("Welcome to the Rock Paper Scissors Game")
while (1) :
    print("\n1. Rock\n2. Papers\n3. Scissors\n4. Exit")
    choise = int(input("Enter your choise:"))
    match choise:
        case 1:
            if system == 1:
                print("Computer: Rock\nPerson: Rock")
                print("Draw!!!")
            if system == 2:
                print("Computer: Paper\nPerson: Rock")
                print("You have lost...")
            if system == 3:
                print("Computer: Scissors\nPerson: Rock")
                print("You Won!!!")
        case 2:
            if system == 1:
                print("Computer: Rock\nPerson: Paper")
                print("You Won!!!")
            if system == 2:
                print("Computer: Paper\nPerson: Paper")
                print("Draw!!!")
            if system == 3:
                print("Computer: Scissors\nPerson: Paper")
                print("You have lost...")
        case 3:
            if system == 1:
                print("Computer: Rock\nPerson: Scissors")
                print("You have lost...")
            if system == 2:
                print("Computer: Paper\nPerson: Scissors")
                print("You Won!!!")
            if system == 3:
                print("Computer: Scissors\nPerson: Scissors")
                print("Draw!!!")
        case 4:
            break
        case _:
            print("Invalid Choise...")
    choise1 = int(input("Enter 1 to exit and enter any number to play again."))
    if choise == 1:
        break
    else :
        print("Playing again...")
    

    