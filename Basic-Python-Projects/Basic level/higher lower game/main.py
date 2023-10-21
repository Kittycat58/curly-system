import random
import art
from game_data import data
from replit import clear

choice1 = random.randint(0, len(data)-1)
choice2 = random.randint(0, len(data)-1)
while choice1 == choice2:
    choice2 = random.randint(0, len(data)-1)

def compare(choice1,choice2):
    print(f"Compare A: {data[choice1]['name']}, {data[choice1]['description']}, {data[choice1]['country']}.")
    print(art.vs)
    print(f"Compare B: {data[choice2]['name']}, {data[choice2]['description']}, {data[choice2]['country']}.")

def start_game(choice1, choice2):
    print(art.logo)
    ans = 0
    compare(choice1, choice2)
    while True:
        choice = input("Who has more follower? 'A' or 'B' ")
        if choice == "A":
            if data[choice1]['follower_count'] > data[choice2]['follower_count']:
                clear()
                print(art.logo)
                ans+=1
                print(f"You're right! Current score: {ans}")
                choice1 = choice2
                choice2 = random.randint(0, len(data)-1)
                while choice1 == choice2:
                    choice2 = random.randint(0, len(data)-1)
                compare(choice1, choice2)
            else:
                clear()
                print(art.logo)
                print("Sorry, that's wrong, Final score: ",ans)
                break
        else:
            if data[choice2]['follower_count'] > data[choice1]['follower_count']:
                clear()
                print(art.logo)
                ans+=1
                print(f"You're right! Current score: {ans}")
                choice1 = choice2
                choice2 = random.randint(0, len(data)-1)
                while choice1 == choice2:
                    choice2 = random.randint(0, len(data)-1)
                compare(choice1, choice2)
            else:
                clear()
                print(art.logo)
                print("Sorry, that's wrong, Final score: ",ans)
                break

start_game(choice1, choice2)