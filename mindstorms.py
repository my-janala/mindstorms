import turtle

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    angie.speed("3")

def draw_triangle():
    tracey = turtle.Turtle()
    tracey.color("red")
    tracey.shape("turtle")

    for i in [0,1,2]:
        tracey.left(120)
        tracey.forward(175)

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed("10")


    for t in [0,1,2,3]
        brad.forward(100)
        brad.right(90)
        draw_circle()
        draw_triangle()

    window.exitonclick()

def main():
    draw_square()

main()
