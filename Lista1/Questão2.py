import turtle

def draw_poly(t, n, sz):
  for i in range(n):
    t.pencolor("fuchsia")
    t.forward(sz)
    t.left(360/n)

wn = turtle.Screen()

wn.bgcolor("lightgreen")

alex = turtle.Turtle()

alex.pensize(3)

draw_poly(alex, 8, 50)

wn.mainloop()