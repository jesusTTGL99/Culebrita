import turtle
import time
import random

def arriba() :
    serpiente.direction = "up"

def abajo() :
    serpiente.direction = "down"

def derecha() :
    serpiente.direction = "right"

def izquierda() :
    serpiente.direction = "left"

def movimiento() :
    if serpiente.direction == "up" :
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down" :
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == "right" :
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == "left" :
        x = serpiente.xcor()
        serpiente.setx(x - 20)

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("black")
s.title("culebrita")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.direction = "stop"
serpiente.color("red")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(100,100)
comida.speed(0)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

while True :
    s.update()
    if serpiente.distance(comida) < 20 :
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x, y)
    movimiento()
    time.sleep(0.2)

turtle.done()
