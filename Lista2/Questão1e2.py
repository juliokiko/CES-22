import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")

wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
  tess.pensize(3)
  tess.color("black", "darkgrey")
  tess.begin_fill()
  tess.forward(80)
  tess.left(90)
  tess.forward(200)
  tess.circle(40, 180)
  tess.forward(200)
  tess.left(90)
  tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
  global state_num
  if state_num == 0: # Transition from state 0 to state 1
    tess.forward(70)
    tess.fillcolor("orange")
    state_num = 1
  elif state_num == 1: # Transition from state 1 to state 2
    tess.forward(70)
    tess.fillcolor("red")
    state_num = 2
  else: # Transition from state 2 to state 0
    tess.back(140)
    tess.fillcolor("green")
    state_num = 0

  wn.ontimer(advance_state_machine, 1000)

def make_tess_red():
  tess.fillcolor("red")

def make_tess_green():
  tess.fillcolor("green")

def make_tess_blue():
  tess.fillcolor("blue")

def make_tess_bigger():
  if (tess.pensize() < 20):
    tess.pensize(tess.pensize() + 1)

def make_tess_smaller():
  if (tess.pensize() > 1):
    tess.pensize(tess.pensize() - 1)

def make_window_yellow():
  wn.bgcolor("yellow")

def make_window_purple():
  wn.bgcolor("purple")

def make_window_lightgreen():
  wn.bgcolor("lightgreen")

def tess_increase_outline():
  u = tess.shapesize()
  if (u[2] < 20):
    tess.shapesize(u[0], u[1], u[2] + 1)

def tess_decrease_outline():
  u = tess.shapesize()
  if (u[2] > 1):
    tess.shapesize(u[0], u[1], u[2] - 1)

# Bind the event handler to the space key.

wn.onkey(advance_state_machine, "space")
wn.onkey(make_tess_red, "r")
wn.onkey(make_tess_green, "g")
wn.onkey(make_tess_blue, "b")
wn.onkey(make_tess_bigger, "+")
wn.onkey(make_tess_smaller, "-")
wn.onkey(make_window_yellow, "y")
wn.onkey(make_window_purple, "p")
wn.onkey(make_window_lightgreen, "l")
wn.onkey(tess_increase_outline, "q")
wn.onkey(tess_decrease_outline, "w")

wn.ontimer(advance_state_machine, 1000)

wn.listen()
wn.mainloop()