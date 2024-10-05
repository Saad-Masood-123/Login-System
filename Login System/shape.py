

import turtle
 


def parallelogram():
    # Initialize the turtle
    t = turtle.Turtle()
    
    # Set the turtle's speed
    t.speed(1)
    
    # Draw the parallelogram
    for i in range(2):
        t.forward(100)
        t.left(60)
        t.forward(50)
        t.left(120)
 

def circle():
    # Set up the turtle screen and set the background color to white
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Create a new turtle and set its speed to the fastest possible
    pen = turtle.Turtle()
    pen.speed(1)
    
    # # Set the fill color to red
    pen.fillcolor("red")
    pen.begin_fill()
    
    # # Draw the circle with a radius of 100 pixels
    pen.circle(100)
    
    # # End the fill and stop drawing
    pen.end_fill()
    pen.hideturtle()
    
    # Keep the turtle window open until it is manually closed
    turtle.done()

parallelogram()
circle()