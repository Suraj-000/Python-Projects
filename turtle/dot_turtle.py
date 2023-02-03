import colorgram
import turtle as t
import random

colors=colorgram.extract('download.jpeg',15)
color_list=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    color_list.append(new_color)
tim=t.Turtle()
t.colormode(255)
tim.speed(0)
tim.setheading(220)
tim.penup()
tim.forward(300)
tim.setheading(0)
for j in range(10):
    for i in range(10):

        tim.dot(20,random.choice(color_list))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    if j%2==0:
        tim.setheading(180)
    else:
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()