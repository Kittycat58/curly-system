print("Welcome to love calculator!")
name1=input("What is your name? ")
name2=input("What is their name? ")
name=name1.lower()+name2.lower()
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
count_true=t+r+u+e
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
count_love=l+o+v+e
love_percent=count_true*10+count_love
if love_percent<10 or love_percent>90:
    print("Your score is",love_percent,", you go together like coke and mentos.")
elif 40<love_percent<50:
    print("Your score is",love_percent,", you are alright together.")
else:
    print("Your score is",love_percent)