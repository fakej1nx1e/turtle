import time
import turtle
import random
import math

t = turtle.Turtle()
t.speed(20)
t.pensize(2)

def zeichne_titel():
    t.penup()
    t.goto(0, 260)
    t.color("black")
    t.write("Turtlegrafik Konzeptprogrammierung", align="center", font=("Arial", 20, "bold"))
    t.penup()
    t.goto(0, 0)
    t.pendown()

def sternenmuster():
    positions = [(-250, 150), (-220, 180), (-280, 170)]
    t.color("yellow")
    for pos in positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        for _ in range(8):
            t.forward(50)
            t.backward(50)
            t.right(45)
    t.penup()
    t.goto(-250, 220)
    t.color("black")
    t.pendown()
    t.write("1. Sternemuster", align="center", font=("Arial", 10, "normal"))

def regenbogen_hexagon():
    t.penup()
    t.goto(-50, 235)
    t.pendown()
    t.color("black")
    t.write("2. Farbe verwenden", align="center", font=("Arial", 10, "normal"))
    t.penup()
    t.goto(-80, 150)
    t.pendown()
    # Verwende hier 6 Farben für die 6 Seiten des Hexagons
    farben = ["red", "orange", "yellow", "green", "blue", "indigo"]
    seitenlaenge = 40  # Kleinere Seitenlänge
    for farbe in farben:
        t.color(farbe)
        t.forward(seitenlaenge)
        t.left(60)

def blume():
    t.penup()
    t.goto(140, 220)
    t.pendown()
    t.color("black")
    t.write("3. Wiederholung", align="center", font=("Arial", 10, "normal"))
    t.penup()
    t.goto(150, 150)
    t.pendown()
    t.color("pink")
    for _ in range(36):
        t.forward(60)
        t.backward(60)
        t.right(10)
    t.penup()
    t.goto(150, 140)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def bunte_quadrate():
    t.penup()
    t.goto(320, 170)
    t.pendown()
    t.color("black")
    t.write("4. Figuren füllen", align="center", font=("Arial", 10, "normal"))
    farben = ["red", "blue", "green", "yellow"]
    size = 30
    for i in range(4):
        t.penup()
        t.goto(300 + i*25, 150 - i*25)
        t.pendown()
        t.fillcolor(farben[i])
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()

def zeichne_haus(x, y, groesse, dachfarbe, hausfarbe):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(hausfarbe)
    t.begin_fill()
    for _ in range(4):
        t.forward(groesse)
        t.left(90)
    t.end_fill()
    t.fillcolor(dachfarbe)
    t.begin_fill()
    t.left(45)
    t.forward(groesse / 1.414)
    t.left(90)
    t.forward(groesse / 1.414)
    t.left(90)
    t.end_fill()
    t.left(45)

def haeuser():
    t.penup()
    t.goto(-250, 50)
    t.pendown()
    t.color("black")
    t.write("5. Funktionen", align="center", font=("Arial", 10, "normal"))
    zeichne_haus(-280, 0, 40, "red", "blue")
    zeichne_haus(-200, 0, 40, "green", "yellow")

def wachsende_spirale():
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.color("black")
    t.write("6. Variablen", align="center", font=("Arial", 10, "normal"))
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    laenge = 0.1
    for _ in range(30):
        t.color("cyan")
        t.forward(laenge)
        t.right(20)
        laenge += 1

def zeichne_kreis(x, y, radius, farbe, gefuellt=False):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(farbe)
    if gefuellt:
        t.begin_fill()
    t.circle(radius)
    if gefuellt:
        t.end_fill()

def kreise_mit_parametern():
    t.penup()
    t.goto(170, 50)
    t.pendown()
    t.color("black")
    t.write("7. Parameter", align="center", font=("Arial", 10, "normal"))
    zeichne_kreis(150, 0, 20, "red", True)
    zeichne_kreis(150, 0, 30, "green", False)
    zeichne_kreis(150, 0, 40, "blue", False)

def zufaellige_punkte():
    t.penup()
    t.goto(300, 50)
    t.pendown()
    t.color("black")
    t.write("8. Zufallszahlen", align="center", font=("Arial", 10, "normal"))
    for _ in range(50):
        x = random.randint(250, 350)
        y = random.randint(-50, 30)
        groesse = random.randint(2, 6)
        r = random.random()
        g = random.random()
        b = random.random()
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(r, g, b)
        t.dot(groesse)

def if_else_muster():
    t.penup()
    t.goto(-50, -100)
    t.pendown()
    t.color("black")
    t.write("9. If-else", align="center", font=("Arial", 10, "normal"))
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    for i in range(20):
        if i % 3 == 0:
            t.color("red")
            t.forward(30)
        elif i % 3 == 1:
            t.color("green")
            t.left(120)
            t.forward(30)
        else:
            t.color("blue")
            t.right(120)
            t.forward(30)

def random_walk():
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.color("black")
    t.write("10. Random Walk", align="center", font=("Arial", 30, "normal"))
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    for _ in range(500):
        t.setheading(random.randint(0, 360))
        t.forward(40)

        x, y = t.xcor(), t.ycor()
        dist = math.hypot(x, y)
        if dist > 200:
            t.setheading(t.towards(0, 0))
            t.forward(40)

def zeichne_titel2():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("black")
    t.write("Danke für eure Aufmerksamkeit", align="center", font=("Arial", 30, "normal"))

def hauptprogramm():
    zeichne_titel()
    sternenmuster()
    regenbogen_hexagon() 
    blume()
    bunte_quadrate()
    haeuser()
    wachsende_spirale()
    kreise_mit_parametern()
    zufaellige_punkte()
    if_else_muster()
    time.sleep(5)
    t.clear()
    random_walk()
    t.clear()
    zeichne_titel2()
    t.hideturtle()
    time.sleep(10)
    
hauptprogramm()