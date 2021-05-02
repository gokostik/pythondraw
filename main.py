from turtle import Turtle, Screen

is_drawing = True
is_eraising = False
timmy = Turtle()
screen = Screen()
screen.colormode(255)

def eraiser():
    global is_eraising
    if is_eraising:
        timmy.pencolor((0,0,0))
    else:
        timmy.pencolor((255,255,255))
    is_eraising = not is_eraising


def up_and_down():
    global is_drawing
    if is_drawing:
        timmy.up()
    else:
        timmy.down()
    is_drawing = not is_drawing


def go_left():
    timmy.setheading(0)
    timmy.forward(10)


def go_right():
    timmy.setheading(180)
    timmy.forward(10)


def go_up():
    timmy.setheading(90)
    timmy.forward(10)


def go_down():
    timmy.setheading(270)
    timmy.forward(10)


screen.onkeypress(up_and_down, "space")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "a")
screen.onkeypress(go_left, "d")
screen.onkeypress(eraiser, "e")
screen.listen()
screen.mainloop()
