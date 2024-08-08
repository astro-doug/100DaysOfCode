from turtle import Turtle
from typing import Final
import time

ALIGNMENT: Final[str] = "center"
FONT: Final[tuple[str, int, str]] = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    current_score: int = 0
    high_score: int = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

    def score_point(self) -> None:
        self.current_score += 1
        self.update_scoreboard()

    def get_score(self) -> int:
        return self.current_score

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(0, 375)
        self.write(f"Score: {self.current_score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.getscreen().update()

    def reset_game(self) -> None:
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(5)
        self.clear()
        self.goto(0, 0)
        self.write("Going again in 3", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.write("                    ...2", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.write("                            ...1", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.current_score = 0
        self.update_scoreboard()


