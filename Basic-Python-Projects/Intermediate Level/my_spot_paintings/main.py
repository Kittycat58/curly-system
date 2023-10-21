# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

tim = t.Turtle()
tim.hideturtle()  
tim.penup()          
tim.goto(-200, 200)  
tim.showturtle()
tim.pendown()
t.colormode(255)
tim.speed(0)

colors_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 
67, 40)]

for i in range(10):
    tim.dot(20)
    for j in range(9):
        tim.up()
        tim.fd(50)
        tim.down()
        tim.dot(20, random.choice(colors_list))
    if i%2!=0:
        tim.up()
        tim.left(90)
        tim.fd(50)
        tim.left(90) 
        tim.down()
    else:
        tim.up()
        tim.right(90)
        tim.fd(50)
        tim.right(90) 
        tim.down()

tim.hideturtle()
screen = t.Screen()
screen.exitonclick()
