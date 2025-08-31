from turtle import Turtle, Screen
import random

timi = Turtle()
timi.speed(0)
timi.hideturtle()

colors = [(144, 81, 56), (195, 154, 132), (181, 162, 167), (16, 26, 65), (41, 102, 160), (128, 167, 194), (238, 219, 89), (69, 17, 35), (63, 25, 13), (156, 63, 97), (27, 47, 129), (120, 187, 153), (130, 27, 49), (226, 80, 50), (201, 77, 110), (54, 121, 56), (153, 27, 13), (10, 65, 26), (19, 89, 45), (247, 216, 0), (65, 124, 206), (179, 162, 46), (211, 179, 187), (6, 88, 107), (228, 175, 166), (71, 169, 103)]
screen = Screen()
screen.colormode(255)

timi.penup()
timi.setheading(225)
timi.forward(300)
timi.setheading(0)

def turn_left():
    timi.setheading(90)
    timi.forward(50)
    timi.setheading(180)
    timi.forward(50)
    

def turn_right():
    timi.setheading(90)
    timi.forward(50)
    timi.setheading(0)
    timi.forward(50)
    timi.setheading(0)


dots_number = 10

for line in range(1, dots_number+1):
    for dot_count in range(1, dots_number + 1):
        timi.dot(20, random.choice(colors))
        timi.forward(50)

    if line % 2:
        turn_left()
    else:
        turn_right()
        

 


screen.exitonclick()