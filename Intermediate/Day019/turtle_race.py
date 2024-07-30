from turtle import Turtle, Screen
import random

PEN_COLORS: tuple = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
TURTLE_SPACING: int = 50


def init_turtles(size: int) -> dict[str, Turtle]:
    holder: dict[str, Turtle] = {}
    for id in range(size):
        turtle: Turtle = Turtle(shape="turtle")
        turtle.pencolor(PEN_COLORS[id])
        turtle.color(PEN_COLORS[id])
        turtle.penup()
        y_coord: int = -125 + (TURTLE_SPACING * id)
        turtle.goto(x=-250, y=y_coord)
        holder[PEN_COLORS[id]] = turtle

    return holder


def race(racers: dict[str, Turtle]) -> tuple[bool, str]:
    for turtle_name in racers:
        turtle: Turtle = racers[turtle_name]
        distance: int = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            winner = turtle_name
            return True, winner
    return False, ""


def main() -> None:
    screen: Screen = Screen()
    screen.setup(width=550, height=400)
    winner_guess: str = screen.textinput(title="Make your Bet!", prompt="Which color turtle will win the race?")
    turtles: dict[str, Turtle] = init_turtles(6)
    reached_end: bool = False
    winner: str = ""
    while not reached_end:
        reached_end, winner = race(turtles)

    if winner == winner_guess:
        print(f"{winner.title()} crossed the finish line first. You guessed correctly!")
    else:
        print(f"{winner.title()} crossed the finish line first. Your guess of {winner_guess.title()} was incorrect!")

    screen.exitonclick()


if __name__ == '__main__':
    main()
