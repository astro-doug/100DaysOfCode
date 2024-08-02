from turtle import Turtle


class Paddle(Turtle):
    PADDLE_SIZE: int = 20
    MOVE_DISTANCE: int = 20
    SNAKE_HEADINGS: tuple[str] = ("Up", "Down")
    LEFT_PADDLE_LANE = -350
    RIGHT_PADDLE_LANE = 350
    STARTING_LEFT_LOCATION: tuple[int, int] = [(LEFT_PADDLE_LANE, 0)]
    current_heading: SNAKE_HEADINGS

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
        self.pensize(self.PADDLE_SIZE)
        self.shapesize(stretch_wid=1, stretch_len=100 / self.PADDLE_SIZE)
        self.setheading(270)
        self.speed("fastest")
        self.penup()
        self.goto(self.STARTING_LEFT_LOCATION[0])

    def __init__(self):
        super().__init__()
        self.init_paddle()

