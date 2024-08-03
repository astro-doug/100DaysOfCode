from turtle import Turtle
from paddle import Paddle
import random


class Ball(Turtle):
    DIRECTIONS: tuple[int] = [45, 135, 225, 315]
    BALL_SPEED: int = 15
    BALL_WIDTH: int = 20
    CIRCLE_DEGREES: int = 360
    current_direction: DIRECTIONS

    def move(self) -> None:
        print(f"Current direction: {self.current_direction}")
        self.setheading(self.current_direction)
        self.forward(self.BALL_SPEED)

    def init_ball(self) -> None:
        self.shape("circle")
        self.setpos(x=0, y=0)
        self.pensize(width=self.BALL_WIDTH)
        self.pencolor("red")
        self.fillcolor("red")
        self.penup()

    def detect_wall_collision(self, screen_height: int) -> None:
        if self.ycor() >= screen_height / 2 - self.BALL_WIDTH:
            self.current_direction = self.CIRCLE_DEGREES - self.current_direction
        elif self.ycor() <= -screen_height / 2 + self.BALL_WIDTH:
            self.current_direction = self.CIRCLE_DEGREES - self.current_direction

    def detect_paddle_collision(self, paddle: Paddle) -> None:
        upper_y_cord: float = paddle.ycor() - int(paddle.PADDLE_HEIGHT / 2)
        lower_y_cord: float = paddle.ycor() + int(paddle.PADDLE_HEIGHT / 2)
        if paddle.player == 'left':
            if self.xcor() <= paddle.LEFT_PADDLE_LANE:
                print("Checking left paddle collision")
                print(paddle.xcor())
                print(paddle.ycor())
                print(self.pos())
                print(self.distance(paddle.xcor(), upper_y_cord))
                print(self.distance(paddle.xcor(), lower_y_cord))

                if self.distance(paddle.xcor(), upper_y_cord) <= 50 or self.distance(paddle.xcor(), lower_y_cord) <= 50:
                    # left collision
                    print("left collision")
                    self.current_direction = abs(int(self.CIRCLE_DEGREES / 4) - self.current_direction)
                    self.move()
        elif paddle.player == 'right':
            if self.xcor() >= paddle.RIGHT_PADDLE_LANE:
                print("Checking right paddle collision")
                print(paddle.xcor())
                print(paddle.ycor())
                print(self.pos())
                print(self.distance(paddle.xcor(), upper_y_cord))
                print(self.distance(paddle.xcor(), lower_y_cord))

                if self.distance(paddle.xcor(), upper_y_cord) <= 50 or self.distance(self.xcor(), lower_y_cord) <= 50:
                    # left collision
                    print("right collision")
                    self.current_direction = abs(int(self.CIRCLE_DEGREES / 4) - self.current_direction)
                    self.move()

    def __init__(self):
        super().__init__()
        self.init_ball()
        self.current_direction = random.choice(self.DIRECTIONS)

