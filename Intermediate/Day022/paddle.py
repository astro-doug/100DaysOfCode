from turtle import Turtle


class Paddle(Turtle):
    PADDLE_WIDTH: int = 20
    PADDLE_HEIGHT: int = 100
    MOVE_DISTANCE: int = 20
    SNAKE_HEADINGS: tuple[str] = ("Up", "Down")
    LEFT_PADDLE_LANE = -350
    RIGHT_PADDLE_LANE = 350
    STARTING_LEFT_LOCATION: tuple[int, int] = [(LEFT_PADDLE_LANE, 0)]
    STARTING_RIGHT_LOCATION:tuple[int, int] = [(RIGHT_PADDLE_LANE, 0)]
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
        if self.player == 'left':
            self.goto(self.STARTING_LEFT_LOCATION[0])
        elif self.player == 'right':
            self.goto(self.STARTING_RIGHT_LOCATION[0])

    def __init__(self, player: str):
        super().__init__()
        self.player = player
        self.init_paddle()

