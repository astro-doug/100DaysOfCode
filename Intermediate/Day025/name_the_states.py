from turtle import Screen, Turtle
from typing import Final, TypedDict
import pandas
from pandas import DataFrame

SCREEN_WIDTH: Final[int] = 725
SCREEN_HEIGHT: Final[int] = 491
SCREEN_TITLE: Final[str] = "U.S. States Guessing Game"
BG_IMAGE_FILE_NAME: Final[str] = "blank_states_img.gif"
STATES_DATA_FILE_NAME: Final[str] = "50_states.csv"
ALIGNMENT: Final[str] = "center"
FONT: Final[tuple[str, int, str]] = ("Courier", 8, "normal")

state_data_type = TypedDict('state_data_type', {'state': dict[int, str], 'x': dict[int, int], 'y': dict[int, int]
    , 'found': dict[int, bool]})


def setup_screen() -> Screen:
    screen: Screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.delay(0)
    screen.tracer(n=0)
    screen.title(SCREEN_TITLE)
    screen.bgcolor("black")
    screen.bgpic(BG_IMAGE_FILE_NAME)
    screen.update()
    return screen


def load_state_data() -> state_data_type:
    data: DataFrame = pandas.read_csv(STATES_DATA_FILE_NAME)
    data["found"] = False
    state_data: state_data_type = data.to_dict()
    return state_data


def get_id_of_guessed_state(state_data: state_data_type, state_guess: str) -> int:
    found_id: int = 0
    for keys in state_data["state"].keys():
        if state_data["state"][keys].title() == state_guess.strip().title():
            found_id = keys
            break
    print(state_data["state"][found_id])
    print(state_data["x"][found_id])
    print(state_data["y"][found_id])
    return found_id


def main() -> None:
    score: int = 0
    still_playing: bool = True
    screen: Screen = setup_screen()
    turtle: Turtle = Turtle()
    turtle.penup()
    turtle.pencolor("black")
    turtle.clear()

    state_data: state_data_type = load_state_data()
    while still_playing:
        guess = screen.textinput(title=f"Guess the State {score}/50", prompt="Enter a State Name:")
        found_id = get_id_of_guessed_state(state_data, guess)
        if found_id > 0 and state_data["found"][found_id] is not True:
            state_data["found"][found_id] = True
            turtle.goto(x=state_data["x"][found_id], y=state_data["y"][found_id])
            turtle.write(state_data["state"][found_id], align=ALIGNMENT, font=FONT)
            score += 1
            if score == 50:
                still_playing = False

    screen.mainloop()


if __name__ == '__main__':
    main()
