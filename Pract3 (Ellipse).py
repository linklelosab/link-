#Draw the following basic shapes in the center of the screen :
#i. Circle ii. Rectangle iii. Square iv. Concentric Circles
#v. Ellipse vi. Line
# Draw ellipse
import turtle as t
t.speed(10)
t.fd(900)
t.back(1800)
t.home()
t.left(90)
t.fd(400)
t.back(800)
t.home()
t.penup()
t.goto(-70,-35)
t.pendown()
t.seth(-45)
for i in range(2):
    t.circle(100,90)
    t.circle(100//2,90)
