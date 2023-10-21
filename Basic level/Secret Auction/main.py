from replit import clear
from art import logo

print(logo)

bidding_dict = {}
while True:
    bidder_name = input("What's your name: ")
    bid = float(input("What's your bid? Rs"))
    bidding_dict[bidder_name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if choice == "yes":
        clear()
        continue
    elif choice == "no":
        break
    else:
        print("Please enter the right option\n")

highest_bidder = ""
highest_bid = 0
for bidder in bidding_dict:
    if bidding_dict[bidder] > highest_bid:
        highest_bidder = bidder
        highest_bid = bidding_dict[bidder]

clear()
print(f"The winner is {highest_bidder} with a bid of Rs{highest_bid}")