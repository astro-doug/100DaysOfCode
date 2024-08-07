from turtle import Turtle


class Scoreboard(Turtle):
    FONT: tuple[str, int, str] = ("Courier", 20, "normal")
    LEVEL_ALIGNMENT: str = "left"
    GAME_OVER_ALIGNMENT: str = "center"
    level: int = 1

    def increase_level(self) -> None:
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align=self.LEVEL_ALIGNMENT, font=self.FONT)
        self.getscreen().update()

    def crash(self) -> None:
        self.goto(x=0, y=0)
        self.write("Game Over!", align=self.GAME_OVER_ALIGNMENT, font=self.FONT)
        self.getscreen().update()

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.pencolor("black")
        self.goto(x=-280, y=270)