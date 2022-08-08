from turtle import Turtle,Screen
import random

tlt = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



def draw_shapes(num_side):
    angle = 360/ num_side
    for _ in range(num_side):

        tlt.forward(100)
        tlt.right(angle)

for shapes_side in range(3,11):
    tlt.color(random.choice(colours))
    draw_shapes(shapes_side)



screen = Screen()
screen.exitonclick()