import random
from turtle import Turtle, Screen

import colorgram
from colorgram import Color

X_START: int = -500
Y_START: int = -500
CIRCLE_RADIUS: int = 25
CIRCLE_OFFSET: int = 100


def random_color(colors: list[Color]) -> tuple[int, int, int]:
    color: Color = random.choice(colors)

    rgb_color: tuple[int, int, int] = color.rgb
    return rgb_color


def draw_circle(timmy: Turtle, colors: list[Color]) -> None:
    color: tuple[int, int, int] = random_color(colors)
    timmy.pencolor(color)
    timmy.fillcolor(color)
    timmy.begin_fill()
    timmy.circle(CIRCLE_RADIUS)
    timmy.end_fill()


def main() -> None:
    colors: list[Color] = colorgram.extract("image.jpeg", 15)

    screen: Screen = Screen()
    screen.colormode(255)
    timmy: Turtle = Turtle()
    timmy.speed(0)
    timmy.hideturtle()

    for row in range(10):
        for column in range(10):
            timmy.penup()
            timmy.setpos(X_START + (column * CIRCLE_OFFSET), Y_START + (row * CIRCLE_OFFSET))
            timmy.pendown()
            draw_circle(timmy, colors)

    screen.exitonclick()


if __name__ == '__main__':
    main()
