from turtle import Turtle


class Scoreboard(Turtle):
    FONT: tuple[str, int, str] = ("Courier", 20, "Normal")

    def __init__(self):
        super().__init__()