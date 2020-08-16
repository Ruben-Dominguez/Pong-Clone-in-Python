import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by me! but again")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


# Functions
def move_w():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)


def move_s():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)


def move_up():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)


def move_down():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)


def move_up_w():
    move_up()
    move_w()


def move_up_s():
    move_up()
    move_s()


def move_down_w():
    move_down()
    move_w()


def move_down_s():
    move_down()
    move_s()


# keyboard bindings
def process_events():
    events = tuple(sorted(key_events))

    if events and events in key_event_handlers:
        (key_event_handlers[events])()

    wn.ontimer(process_events, 30)


def up():
    key_events.add('Up')


def down():
    key_events.add('Down')


def w():
    key_events.add('w')


def s():
    key_events.add('s')


def r_up():
    key_events.remove('Up')


def r_down():
    key_events.remove('Down')


def r_w():
    key_events.remove('w')


def r_s():
    key_events.remove('s')


key_event_handlers = {
    ("Up",): move_up,
    ("Down",): move_down,
    ("w",): move_w,
    ("s",): move_s,
    ("Up", "w"): move_up_w,
    ("Up", "s"): move_up_s,
    ("Down", "w"): move_down_w,
    ("Down", "s"): move_down_s,
}

key_events = set()

wn.listen()
wn.onkeypress(w, "w")
wn.onkeypress(s, "s")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")

wn.onkeyrelease(r_w, "w")
wn.onkeyrelease(r_s, "s")
wn.onkeyrelease(r_up, "Up")
wn.onkeyrelease(r_down, "Down")


process_events()

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("wall_hit.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wall_hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.dx = .2
        ball.dy = .2
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.dx = .2
        ball.dy = .2
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 70 > ball.ycor() > paddle_b.ycor() - 70):
        ball.setx(340)
        ball.dx *= -1.15
        winsound.PlaySound("paddle_hit.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 70 > ball.ycor() > paddle_a.ycor() - 70):
        ball.setx(-340)
        ball.dx *= -1.15
        winsound.PlaySound("paddle_hit.wav", winsound.SND_ASYNC)

    paddle_a.sety(min(paddle_a.ycor(), 250))
    paddle_a.sety(max(paddle_a.ycor(), -250))
    paddle_b.sety(min(paddle_b.ycor(), 250))
    paddle_b.sety(max(paddle_b.ycor(), -250))
