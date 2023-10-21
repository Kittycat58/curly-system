import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r,g,b)
    return colors

tim.speed(0)
for i in range(0,360,3):
    tim.color(random_color())
    tim.circle(200)
    current_heading = tim.heading()
    tim.setheading(current_heading + 3)
    
screen = t.Screen()
screen.exitonclick()
