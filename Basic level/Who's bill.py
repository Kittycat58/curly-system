import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
no_of_names=len(names)-1

num=random.randint(0, no_of_names)
print(names[num],"is going to buy the meal today!")