#ohamilton79
#Curved Sierpinksi curve drawing
#22/05/2021
import turtle

def drawZig(t, size):
    t.right(45)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(45)
    t.forward(size)
    t.right(45)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(45)
    t.forward(size)

def drawZag(t, size):
    t.right(45)
    t.forward(size)
    t.right(45)
    t.forward(size)
    t.right(45)
    t.forward(size)
    t.right(45)
    t.forward(size)
    t.right(45)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.right(45)
    t.forward(size)
      
def zig(t, size, n):
    if n == 1:
        drawZig(t, size)

    else:
        zig(t, size, n-1)
        zag(t, size, n-1)
        zig(t, size, n-1)
        zag(t, size, n-1)

def zag(t, size, n):
    if n == 1:
        drawZag(t, size)

    else:
        zag(t, size, n-1)
        zag(t, size, n-1)
        zig(t, size, n-1)
        zag(t, size, n-1)

def sierpinski(t, size, n):
    zig(t, size, n)
    zig(t, size, n)

#Initialise
t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()
size = 20

#Test data
sierpinski(t, size, 3)
