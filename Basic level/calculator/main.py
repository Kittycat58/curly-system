from art import logo
from replit import clear
print(logo)

def calculator(first_num,sec_num,operator):
    """func to add,subtract,multiply,divide numbers"""
    if operator == "+":
        result = first_num + sec_num
    elif operator == "-":
        result = first_num - sec_num
    elif operator == "*":
        result = first_num * sec_num
    else:
        result = first_num / sec_num
    return result

first_num = float(input("What's the first number?: "))
while True:
    print("+\n-\n*\n/")
    operator = input("Pick an operator: ")
    sec_num = float(input("What's the next number?: "))
    result = calculator(first_num, sec_num, operator)
    print(f"{first_num} {operator} {sec_num} = {result}")
    choice = input(f"Type 'y' to continue with {result}, type 'n' to start a new calculation, or type anything else to exit: ")
    if choice == "y":
        first_num = result
        continue
    elif choice == "n":
        clear()
        print(logo)
        first_num = float(input("What's the first number?: "))
        continue
    else:
        break