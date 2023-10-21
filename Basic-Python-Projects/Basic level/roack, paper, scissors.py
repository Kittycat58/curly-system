import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list=[rock,paper,scissors]

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    print("User chose\n",list[user_choice])
    comp_choice = random.randint(0, 2)
    print("\nComputer chose\n",list[comp_choice])
    if (user_choice>comp_choice and user_choice-comp_choice==1) or comp_choice-user_choice==2:
        print("You Win!")
    elif user_choice<comp_choice or user_choice-comp_choice==2:
        print("You Lose!")
    else:
        print("Match Draw!")
    choice=input("Want to play again? yes or no? ")
    if choice=="yes":
        continue
    else:
        break
