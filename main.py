import turtle
import random

#A general function to draw any polygon and using different bolds or pen shapes
def polygon(numberOfSides,sideLong,x,y,color="black",shape="turtle",bold=1,text=' '):

    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.shape(shape)
    turtle.pensize(bold)
    turtle.write(text)
    turtle.color(color)
    turtle.begin_fill()

    for i in range(numberOfSides):
        turtle.forward(sideLong)
        turtle.left(360//numberOfSides)

    turtle.end_fill()
    
polygon(6,50,-120,40,"orange","turtle",2)
polygon(6,50,-45,-5,"yellow","turtle",2)
polygon(6,50,30,-50,"orange","turtle",2)
polygon(6,50,-45,84,"silver","turtle",2)
polygon(6,50,30,39,"gold","turtle",2)
polygon(6,50,106,-6,"silver","turtle",2)
polygon(6,50,-120,-49,"gold","turtle",2)
polygon(6,50,-45,-93,"silver","turtle",2)
polygon(3,1,-150,-100,"white")
polygon(0,0,-60,100,"white","turtle",2,"...Reyhan Genç")