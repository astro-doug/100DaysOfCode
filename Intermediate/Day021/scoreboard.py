from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
current_score: int = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 375)

    def score_point(self) -> None:
        global current_score
        current_score += 1

    def get_score(self) -> int:
        return current_score

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {current_score} ", align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)