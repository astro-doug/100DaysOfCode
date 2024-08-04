from turtle import Turtle


class Paddle(Turtle):
    PADDLE_WIDTH: int = 20
    PADDLE_HEIGHT: int = 100
    MOVE_DISTANCE: int = 20
    SNAKE_HEADINGS: tuple[str] = ("Up", "Down")
    paddle_lane: int
    starting_location: tuple[int, int]
    current_heading: SNAKE_HEADINGS
    player: str

    def move_up(self) -> None:
        self.change_heading("Up")
        self.move()

    def move_down(self) -> None:
        self.change_heading("Down")
        self.move()

    def change_heading(self, new_heading: SNAKE_HEADINGS) -> None:
        match new_heading:
            case "Up":
                if self.current_heading != "Up":
                    self.setheading(90)
                    self.current_heading = "Up"
            case "Down":
                if self.current_heading != "Down":
                    self.setheading(270)
                    self.current_heading = "Down"

    def move(self) -> None:
        self.forward(self.MOVE_DISTANCE)

    def init_paddle(self) -> None:
        self.current_heading = "Down"
        self.color("white")
        self.fillcolor("white")
        self.shape("square")
        self.pencolor("white")
        self.pensize(self.PADDLE_WIDTH)
        self.shapesize(stretch_wid=1, stretch_len=self.PADDLE_HEIGHT / self.PADDLE_WIDTH)
        self.setheading(270)
        self.speed("fastest")
        self.penup()
        self.starting_location: tuple[int, int] = [(self.paddle_lane, 0)]
        self.goto(self.starting_location[0])

    def __init__(self, player: str, paddle_lane: int):
        super().__init__()
        self.player = player
        self.paddle_lane = paddle_lane
        self.init_paddle()

