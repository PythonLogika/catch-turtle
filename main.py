from turtle import *
from random import randint
from time import sleep  

def catch(x, y):
    t.points += 1
    t.write("A!")
    t.goto(randint(-200, 200), randint(-200, 200))

t = Turtle()
t.points = 0
t.shape("turtle")
t.color("red")
t.penup()

t.onclick(catch)

while t.points < 5:
    sleep(1)
    t.goto(randint(-200, 200), randint(-200, 200))

t.write("WOW!")
t.hideturtle()