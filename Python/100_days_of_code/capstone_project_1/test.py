import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(2)

colurs = ["red", "orange", "yellow", "green", "blue", "purple"]

for colour in colurs:
    pen.color(colour)
    pen.forward(100)
    pen.right(60)

# your turtle code goes here

screen.exitonclick()  # This keeps the window open and waits for user events
