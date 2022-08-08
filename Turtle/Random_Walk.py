import turtle as t
import random

tlt = t.Turtle()

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.colormode(255)

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colours = (r,g,b)
    return random_colours

dir = [0,90,180,270]
tlt.pensize(15)

for _ in range(200):
    tlt.color(random_color())
    tlt.forward(15)
    tlt.setheading(random.choice(dir))



screen = t.Screen()
screen.exitonclick()