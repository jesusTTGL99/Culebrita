import turtle

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("culebrita")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.direction = "stop"
serpiente.color("red")

turtle.done()
