#Program to divide screen into four region, draw circle,
#rectangle, ellipse and half ellipse in each region with appropriate message
import turtle as T
#import random

T.forward(800)
T.backward(1600)
T.home()
T.left(90)
T.forward(600)
T.backward(1200)
T.home()

T.penup()

T.goto(150,150)
T.pendown()
T.circle(50)
T.write("Circle",font=("Arial",12,"normal"))

#Draw Rectangle
T.penup()
x=-125
y=125
T.goto(x,y)
#T.dot()
T.pendown()
T.forward(100)#forward turtle by length by 1 units
T.left(90)#turn turtle by 90 degree
#drawing second side
T.forward(120)#forward turtle by width
T.left(90)#turn turtle by 90 degree
#drawing third side
T.forward(100)#forward turtle by length by 1 units
T.left(90)#turn turtle by 90 degree
#drawing fourth side
T.forward(120)#forward turtle by length by 1 units
T.left(90)#turn turtle by 90 degree
T.write("Rectangle",font=("Arial",12,"normal"))

#drawing Ellipse
T.penup()
x=-170
y=-125
T.goto(x,y)
T.pendown()
T.seth(-45)#used to set the orientation of the turtle to to_angle. 
for i in range(2):
    #two arcs
    T.circle(100,90)
    T.circle(100//2,90)
T.write("Ellipse",font=("Arial",12,"normal"))

#drawing Half Ellipse
T.penup()
x=125
y=-125
T.goto(x,y)
T.pendown()

for x in range(180):
    T.forward(1)
    T.right(1)
T.write("Arc",font=("Arial",12,"normal"))
 
