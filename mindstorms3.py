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
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    window.exitonclick()

draw_art()
