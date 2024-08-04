from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Terminal", 64, "bold")
GAME_OVER_FONT = ("Terminal", 64, "bold")
player_score: int = 0
computer_score: int = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 220)

    def score_point(self, player: str) -> None:
        global player_score, computer_score
        if player == 'left':
            player_score += 1
        elif player == 'right':
            computer_score += 1

    def get_score(self, player: str) -> int:
        global player_score, computer_score
        if player == 'left':
            return player_score
        elif player == 'right':
            return computer_score

    def update_scoreboard(self) -> None:
        global SCORE_FONT
        self.clear()
        self.write(f"{player_score}               {computer_score}", align=ALIGNMENT, font=SCORE_FONT)
        self.getscreen().update()

    def game_over(self) -> None:
        global GAME_OVER_FONT
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.getscreen().update()