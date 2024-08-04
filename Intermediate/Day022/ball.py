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
        #rint(f"Current direction: {self.current_direction}")
        self.setheading(self.current_direction)
        self.forward(self.BALL_SPEED)

    def init_ball(self) -> None:
        self.shape("circle")
        self.setpos(x=0, y=0)
        self.pensize(width=self.BALL_WIDTH)
        self.pencolor("red")
        self.fillcolor("red")
        self.penup()

    def bounce_off_wall(self) -> None:
        self.current_direction = self.CIRCLE_DEGREES - self.current_direction

    def bounce_off_paddle(self) -> None:
        self.current_direction = int(self.CIRCLE_DEGREES / 2) - self.current_direction
        self.move()

    def detect_wall_collision(self, screen_height: int) -> None:
        if self.ycor() >= screen_height / 2 - self.BALL_WIDTH:
            self.bounce_off_wall()
        elif self.ycor() <= -screen_height / 2 + self.BALL_WIDTH:
            self.bounce_off_wall()

    def detect_paddle_collision(self, paddle: Paddle) -> None:
        upper_y_cord: float = paddle.ycor() - int(paddle.PADDLE_HEIGHT / 2)
        lower_y_cord: float = paddle.ycor() + int(paddle.PADDLE_HEIGHT / 2)
        if paddle.player == 'left':
            if self.xcor() <= paddle.paddle_lane + self.BALL_WIDTH:
                if self.distance(paddle.xcor(), upper_y_cord) <= 50 or self.distance(paddle.xcor(), lower_y_cord) <= 50:
                    self.bounce_off_paddle()
        elif paddle.player == 'right':
            if self.xcor() >= paddle.paddle_lane - self.BALL_WIDTH:
                if self.distance(paddle.xcor(), upper_y_cord) <= 50 or self.distance(self.xcor(), lower_y_cord) <= 50:
                    self.bounce_off_paddle()

    def detect_out_of_bounds(self) -> str:
        # if self.xcor() > PADDLE_LANE + self.BALL_WIDTH
        #     return "right"
        pass

    def __init__(self):
        super().__init__()
        self.init_ball()
        self.current_direction = random.choice(self.DIRECTIONS)

