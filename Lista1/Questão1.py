import turtle

def draw_square(t, sz):
  for i in range(4):
    t.pencolor("fuchsia")
    t.forward(sz)
    t.left(90)

wn = turtle.Screen()

wn.bgcolor("lightgreen")

alex = turtle.Turtle()

alex.pensize(3)

for i in range(5):
  draw_square(alex, 20*(i+1))
  alex.pencolor("lightgreen")
  alex.penup()
  alex.setpos(-10*(i+1),-10*(i+1))
  alex.pendown()

wn.mainloop()