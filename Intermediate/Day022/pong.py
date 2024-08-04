from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
LEFT_PADDLE_LANE: int = -350
RIGHT_PADDLE_LANE:int = 350
WINNING_SCORE: int = 5
right_player_paddle: Paddle
left_player_paddle: Paddle


def draw_net() -> None:
    global SCREEN_HEIGHT
    turtle: Turtle = Turtle()
    turtle.penup()
    turtle.shape("square")
    turtle.color("white")
    turtle.pencolor("white")
    turtle.width(8)
    turtle.goto(x=-4, y=SCREEN_HEIGHT / 2)
    turtle.setheading(270)
    for _ in range(int(SCREEN_HEIGHT / 100)):
        turtle.pendown()
        turtle.forward(50)
        turtle.penup()
        turtle.forward(50)


def left_move_up() -> None:
    global left_player_paddle
    left_player_paddle.move_up()


def left_move_down() -> None:
    global left_player_paddle
    left_player_paddle.move_down()


def right_move_up() -> None:
    global right_player_paddle
    right_player_paddle.move_up()


def right_move_down() -> None:
    global right_player_paddle
    right_player_paddle.move_down()


def setup_screen() -> Screen:
    screen: Screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.delay(0)
    screen.tracer(n=0)
    screen.title("TurtlePyPong")
    screen.bgcolor("black")
    screen.listen()
    screen.onkey(key="w", fun=left_move_up)
    screen.onkey(key="s", fun=left_move_down)
    screen.onkey(key="Up", fun=right_move_up)
    screen.onkey(key="Down", fun=right_move_down)
    draw_net()
    return screen


def main() -> None:
    global left_player_paddle, right_player_paddle
    screen: Screen = setup_screen()
    scoreboard: ScoreBoard = ScoreBoard()
    scoreboard.update_scoreboard()
    left_player_paddle = Paddle(player='left', paddle_lane=-350)
    right_player_paddle = Paddle(player='right', paddle_lane=350)

    ball: Ball = Ball()

    still_playing: bool = True
    while still_playing:
        ball.move()
        ball.detect_wall_collision(SCREEN_HEIGHT)
        ball.detect_paddle_collision(left_player_paddle)
        ball.detect_paddle_collision(right_player_paddle)
        screen.update()
        if ball.detect_out_of_bounds(LEFT_PADDLE_LANE):
            scoreboard.score_point('right')
            if scoreboard.get_score('right') == WINNING_SCORE:
                scoreboard.game_over()
                still_playing = False
            else:
                ball = reset_ball(ball, scoreboard, screen)
        elif ball.detect_out_of_bounds(RIGHT_PADDLE_LANE):
            scoreboard.score_point('left')
            if scoreboard.get_score('left') == WINNING_SCORE:
                scoreboard.game_over()
                still_playing = False
            else:
                ball = reset_ball(ball, scoreboard, screen)

        time.sleep(.1)

    screen.exitonclick()


def reset_ball(old_ball: Ball, scoreboard: ScoreBoard, screen: Screen()) -> Ball:
    old_ball.hideturtle()
    ball: Ball = Ball()
    scoreboard.update_scoreboard()
    screen.update()
    time.sleep(3)
    return ball


if __name__ == '__main__':
    main()
