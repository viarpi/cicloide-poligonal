import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import turtle
import math
caneta = turtle.Turtle()
caneta2 = turtle.Turtle()
caneta3 = turtle.Turtle()
caneta4 = turtle.Turtle()
turtle.setup(1920, 1080, 0, 0)
turtle.tracer(0,0)
caneta.goto(-250,0)
caneta.color("grey")
caneta2.goto(-250,0)
caneta2.clear()
caneta2.width(5)
caneta2.setheading(-90)
caneta2.penup()
caneta3.width(3)
caneta4.goto(-250,0)
caneta4.width(3)
lados = int(turtle.numinput("determine o número","de lados"))
caneta3.goto(-250,0)
caneta3.forward(500/lados)
def desenhar_poligono(x,y):
    for i in range(lados):
        caneta.forward(500/lados)
        caneta.left(360/lados)
    caneta.forward(500/lados)
def desenhar_arcos(x,y):
    caneta2.circle(raio,-360/lados)
    caneta2.left(180/lados)
    caneta4.goto(caneta2.xcor(),caneta2.ycor())
    if i < lados-2:
        caneta4.goto(caneta3.xcor(),caneta3.ycor())
        caneta4.goto(caneta2.xcor(),caneta2.ycor())
    if i < lados-1:
        caneta3.forward(500/lados)
    caneta4.goto(caneta3.xcor(),caneta3.ycor())
    caneta4.goto(caneta2.xcor(),caneta2.ycor())

for i in range (lados):
    desenhar_poligono(caneta.xcor(),caneta.ycor())
for i in range (lados):
    raio = (500*math.sin((i+1)*math.pi/lados))/(lados*math.sin(math.pi/lados))
    desenhar_arcos(caneta2.xcor(),caneta2.ycor())
def reiniciar(x,y):
    caneta.goto(-250,0)
    caneta2.goto(-250,0)
    caneta3.goto(-250,0)
    caneta3.setheading(0)
    caneta4.goto(-250,0)
    caneta.clear()
    caneta2.clear()
    caneta3.clear()
    caneta4.clear()
    caneta2.setheading(-90)
    lados2 = int(turtle.numinput("determine o número","de lados"))
    caneta3.forward(500/lados2)
    for i in range (lados2):
        for i in range(lados2):
            caneta.forward(500/lados2)
            caneta.left(360/lados2)
        caneta.forward(500/lados2)                    
    for i in range (lados2):
        caneta2.circle((500*math.sin((i+1)*math.pi/lados2))/(lados2*math.sin(math.pi/lados2)),-360/lados2)
        caneta2.left(180/lados2)
        caneta4.goto(caneta2.xcor(),caneta2.ycor())
        if i < lados2-2:
            caneta4.goto(caneta3.xcor(),caneta3.ycor())
            caneta4.goto(caneta2.xcor(),caneta2.ycor())
        if i < lados2-1:
            caneta3.forward(500/lados2)
        caneta4.goto(caneta3.xcor(),caneta3.ycor())
        caneta4.goto(caneta2.xcor(),caneta2.ycor())
    turtle.update()
turtle.listen
turtle.onscreenclick(reiniciar)
turtle.update()
turtle.done()