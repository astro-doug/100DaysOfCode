from turtle import Turtle


class Player(Turtle):
    STARTING_POSITION: tuple[int, int] = (0, -280)
    MOVE_DISTANCE: int = 10
    FINISH_LINE_Y: int = 280
    STRAIGHT_UP: int = 90

    def move_up(self) -> None:
        self.forward(Player.MOVE_DISTANCE)

    def init_player(self) -> None:
        self.penup()
        self.shape("turtle")
        self.setheading(Player.STRAIGHT_UP)
        self.color("green")
        self.start_turtle()

    def start_turtle(self) -> None:
        self.goto(Player.STARTING_POSITION)

    def check_reached_end(self) -> bool:
        return self.ycor() >= Player.FINISH_LINE_Y

    def __init__(self):
        super().__init__()
        self.init_player()
