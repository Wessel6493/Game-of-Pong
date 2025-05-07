# Ik heb de laatste optie gekozen dat de bal van kleur veranderd op basis van
# hoeveel punten je hebt
# Ik heb dit gemaakt doormiddel van een if else statement

import turtle
import time
spel_bezig = True
from click import clear
# Venster instellen
wn = turtle.Screen()
wn.title("Pong voor Wessel")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=6, stretch_len=1)
paddle.penup()
paddle.goto(-350, 0)
def paddle_up():
    y = paddle.ycor()
    if y < 250:
        y += 20
    paddle.sety(y)
def paddle_down():
    y = paddle.ycor()
    if y > -240:
        y -= 20
    paddle.sety(y)
# Toetsenbordbinding
wn.listen()
wn.onkeypress(paddle_up, "w")
wn.onkeypress(paddle_down, "s")
# Bal
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2
# Score variabele
score = 0
# levens variabele
levens = 3
# Pen om de score weer te geven
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Levens: 3", align="center", font=("Courier", 24, "normal"))
def update_score():
    pen.clear()
    pen.write("Score: {} Levens: {}".format(score, levens), align="center",font=("Courier", 24, "normal"))
def game_over():
    global spel_bezig  # Gebruik de globale variabele spel_bezig
    pen.clear()
    pen.goto(0, 0)
    pen.write("Game Over", align="center", font=("Courier", 36, "normal"))
    spel_bezig = False  # Stop het spel door spel_bezig op False te zetten
def update_ball_kleur():
    if score < 10:
        ball.color("blue")
    elif score < 20:
        ball.color("yellow")
    elif score < 30:
        ball.color("orange")
    else:
        ball.color("red")
while True:
    wn.update()
    update_score()
    # Beweeg de bal
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # detecteer randen van het scherm
    if ball.xcor() > 300:
        ball.dx *= -1
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.dy *= -1
    if ball.ycor() > 299 or ball.ycor() < -299:
        ball.dy *= -1
    # Detecteer botsing met paddle
    if ball.dx < 0 and ball.xcor() < -350:  # ball beweegt naar links en zit bij de linker zijkant.
        # print("ball dx: " + str(ball.dx) + " ball dy:" + str(ball.dy))
        if paddle.ycor() - 60 < ball.ycor() < paddle.ycor() + 60:  # bal 'raakt' de paddle
            # print("Bal raakt de paddle: ")
            # print(paddle)
            ball.dx *= -1  # beweeg de bal de andere kant uit (horizontaal)
            ball.dy *= -1  # beweeg de bal de andere kant uit (verticaal)
            score += 1
            update_ball_kleur()
        else:
            if  levens > 1:
                # print("Levens is: " + str(levens))
                levens = levens - 1
                time.sleep(3)
                spel_bezig = False
                # ball.goto(0, 0)
                ball.dx = ball.dx  * -1  # beweeg de bal de andere kant uit(horizontaal)
                ball.dy = ball.dy * -1  # beweeg de bal de andere kant uit(verticaal)
            else:
                # print("Game over")
                time.sleep(5)
                game_over()