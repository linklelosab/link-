import turtle
import math
# Create our turtle
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(5)
# Define a function to draw and
# fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
# Define a function to draw and fill an equalateral right
# triangle with the given hypotenuse length and color. This
# is used to create a roof shape.
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
# Draw and fill the front of the house
t.penup()
t.goto(-150, -120)
t.pendown()
drawRectangle(t, 100, 110, "blue")# Draw and fill the front door
t.penup()
t.goto(-120, -120)
t.pendown()
drawRectangle(t, 40, 60, "lightgreen")# Front roof
t.penup()
t.goto(-150, -10)
t.pendown()
drawTriangle(t, 100, "magenta")
