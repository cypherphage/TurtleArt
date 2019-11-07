import turtle
import msvcrt

def move(yourTurtle):
    print("Use w a s d to move , e to exit")
    x = "w"
    while x != "e":
        x = msvcrt.getch().decode('utf-8')    
        if x=="w":
            yourTurtle.forward(20)        
        if x=="s":
            yourTurtle.backward(20)
        if x=="a":
            yourTurtle.left(90)
        if x=="d":
           yourTurtle.right(90)

wn = turtle.Screen()
wn.bgcolor("black")


shero = turtle.Turtle() # yes, I can name my turtle shero
shero.shape("turtle")   
shero.color("hotpink") 
shero.up()  # stops line from beign drawn, think as if the turtle's tail is like a pencil 

move(shero)



