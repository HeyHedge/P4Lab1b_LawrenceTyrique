import turtle
t = turtle.Turtle()
# move the turtle to the starting point
t.penup()
t.goto (-30,50)
t.pendown()

# Draw top horizontal line
t.forward(200)
t.backward(100)

# Draw vertical
t.right(90)
t.forward(250)

# Move the turtle to the starting point
t.penup()
t.goto(150,100)
t.pendown()

# Draw bottom Horizontal line
t.forward(200)

# Draw Vertical line
t.setheading(5)
t.forward(150)
