import turtle
tl = turtle.Turtle()
tl.speed(5)
tl.color("blue")
tl.width(4)
sides = [ 1, 2, 3, 4, 5, 6,]
length = [1, 2, 3, 4, 5, 6, 7, 8]

# Move back so the chain is centered.
tl.penup()
tl.back(80)
tl.pendown()


for link in length:
  # draw hexagon
  for side in sides:
    tl.forward(10)
    tl.right(60)
    
    
    #move to the next line
  tl.penup()
  tl.forward(20)
  tl.pendown()
  
tl.hideturtle()
  
