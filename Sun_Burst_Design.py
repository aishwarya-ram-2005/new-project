import turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.speed(0)
turtle.tracer(4,0)

color=["#FFE0B2","#FFB74D","#FFA726","#FB8C00","#E65100"]

for i in range(360):
    t.color(color[i % 5])
    t.circle(140)
    t.left(1)

s.update()
turtle.done()