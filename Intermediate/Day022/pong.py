from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from paddle import Paddle
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
player_paddle: Paddle


def draw_net(screen: Screen) -> None:
    turtle: Turtle = Turtle()
    turtle.penup()
    turtle.shape("square")
    turtle.color("white")
    turtle.pencolor("white")
    turtle.width(10)
    turtle.goto(x=-5, y=SCREEN_HEIGHT / 2)
    turtle.setheading(270)
    for _ in range(8):
        turtle.pendown()
        turtle.forward(50)
        turtle.penup()
        turtle.forward(50)


def move_up() -> None:
    global player_paddle
    player_paddle.move_up()


def move_down() -> None:
    global player_paddle
    player_paddle.move_down()


def setup_screen() -> Screen:
    screen: Screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.delay(0)
    screen.tracer(n=0)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.listen()
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    draw_net(screen)
    return screen


def main() -> None:
    global player_paddle
    screen: Screen = setup_screen()
    scoreboard: ScoreBoard = ScoreBoard()

    player_paddle = Paddle()
    still_playing: bool = True
    while still_playing:
        scoreboard.update_scoreboard()
        time.sleep(.15)
        screen.update()


    screen.exitonclick()


if __name__ == '__main__':
    main()
