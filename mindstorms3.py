import turtle

def draw_square(some_turtle):
    """ create square """
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    """ create screen, square and circle   """
    window = turtle.Screen()
    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed("2")
    draw_square(brad)
    # create square angie
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.speed(5)
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

draw_art()
