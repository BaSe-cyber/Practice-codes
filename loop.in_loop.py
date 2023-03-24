import turtle

tl = turtle.Turtle()

tl.color("blue")
tl.width(4)

big_side = [1,2,3,4]
small_side = [1,2,3,4]

tl.penup()
tl.back(-140) # move the diagram to extreme right
tl.pendown()

for side in big_side: # drawa a big triangle
    tl.forward(100)
    tl.right(90)
    for side in small_side: #draws small triangle at each angle of the big triangle
        tl.forward(10)
        tl.right(90)



chain = [1,2,3,4,5,6,7,8]
sides = [1,2,3,4,5,6]
tl.penup()
tl.back(200)
tl.pendown()

for side in chain: # states how many times the hexagon will be drawn
    for side in sides: # draw hexagon
        tl.forward(10)
        tl.right(60)
    tl.penup() # pick pen up but no drawing as it moves
    tl.forward(20) # move forward by 20 without drawing
    tl.pendown() # draw as it moves

tl.hideturtle()

