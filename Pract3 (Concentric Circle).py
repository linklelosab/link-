#Draw the following basic shapes in the center of the screen :
#i. Circle ii. Rectangle iii. Square iv. Concentric Circles
#v. Ellipse vi. Line
#draw concentric circle
import turtle as t
r = 10
for i in range(10):
    t.speed(10)
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.down()
