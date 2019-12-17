import turtle
import random
myT = turtle.Turtle()
myW = turtle.Screen()
col = ["red","green","blue","yellow","black"]
def draw(myT, lineLen):
    if lineLen > 0:
        myT.forward(lineLen)
        myT.color(col[random.randint(0,4)])
        myT.right(45)
        myT.forward(lineLen)
        myT.color(col[random.randint(0,4)])
        myT.right(45)
        myT.forward(lineLen)
        myT.color(col[random.randint(0,4)])
        myT.right(45)
        myT.forward(lineLen)
        myT.color(col[random.randint(0,4)])
        myT.right(45)
        myT.color(col[random.randint(0,4)])
        myT.forward(lineLen)
        myT.color(col[random.randint(0,4)])
        myT.right(45)
        draw(myT, lineLen-5)

draw(myT, 100)
myW.exitonclick()