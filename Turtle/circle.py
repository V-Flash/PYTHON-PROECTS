import turtle as t
import random

tlt = t.Turtle()

t.colormode(255)


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colours = (r,g,b)
    return random_colours


def draw_gap(gap_size):

    for _ in range(int(360/gap_size)):
        tlt.color(random_color())
        tlt.circle(100)
        tlt.setheading(tlt.heading() + gap_size)
draw_gap(5)



screen = t.Screen()
screen.exitonclick()