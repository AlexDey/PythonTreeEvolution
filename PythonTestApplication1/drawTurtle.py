import turtle

from settings import rows, columns, row_start, column_start

def addCorn(row, column):
    """Create turtle and add to massive"""

    x_pos = column*rect_size - width/2
    y_pos = row*rect_size - height/2
    corn_new = turtle.Turtle()
    corn_new.speed(0)
    corn_new.shape("square")
    corn_new.color("white")
    corn_new.penup()
    corn_new.goto(x_pos, y_pos)
    corn_new.shapesize(scale, scale)
    corn_turtle.append(corn_new)

def update():
    wn.update()

def cornToTree():
    """fill corn like tree and clear 'corn_turtle' matrix"""
    [corn_one.color("green") for corn_one in corn_turtle]
    #tree_turtle.extend(corn_turtle)
    corn_turtle[:] = []

# start data for draw window with turtle
#scale = .4
constant_size = 24 # = rows * scale
scale = constant_size / rows
rect_size = 21 * scale
width = rect_size*columns*2
height = rect_size*rows*2

# screen
wn = turtle.Screen()
wn.title("Tree evolution")
wn.bgcolor("black")
wn.setup(width, height, startx=-1, starty=0)
wn.tracer(0) # Turns off the screen updates

# corn
corn_turtle = []
x_pos_start = column_start*rect_size - width/2
y_pos_start = row_start*rect_size - height/2
corn_start = turtle.Turtle()
corn_start.speed(0)
corn_start.shape("square")
corn_start.color("white")
corn_start.penup()
corn_start.goto(x_pos_start, y_pos_start)
corn_start.shapesize(scale, scale)
corn_turtle.append(corn_start)