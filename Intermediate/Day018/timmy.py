from turtle import Turtle, Screen
import random
from time import sleep


def main() -> None:
    timmy: Turtle = Turtle()
    # timmy.shape("turtle")
    timmy.color("dark orchid")
    sleep(5)
    screen: Screen = Screen()
    screen.colormode(255)

    # draw_square(timmy)
    # draw_dashed_line(timmy)
    # draw_all_shapes(timmy)
    # random_walk(timmy)
    draw_spirograph(timmy, 5)

    screen.exitonclick()


def draw_square(timmy: Turtle) -> None:
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def draw_dashed_line(timmy: Turtle) -> None:
    for _ in range(20):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def random_color() -> tuple[int, int, int]:
    r: int = random.randint(0, 255)
    g: int = random.randint(0, 255)
    b: int = random.randint(0, 255)
    rgb_color: tuple[int, int, int] = (r, g, b)
    return rgb_color


def draw_all_shapes(timmy: Turtle) -> None:
    for sides in range (3, 11):
        angle: int = int(360 / sides)

        timmy.pencolor(random_color())
        for _ in range(sides):
            timmy.forward(100)
            timmy.right(angle)


def random_walk(timmy: Turtle) -> None:
    timmy.pensize(15)
    timmy.speed(8)

    for _ in range(100):
        timmy.pencolor(random_color())
        timmy.forward(25)
        angle: int = random.choice([0, 90, 180, 270])
        timmy.setheading(angle)


def draw_spirograph(timmy: Turtle, gap_size: int) -> None:
    timmy.speed(0)
    for _ in range(int(360 / gap_size)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.left(gap_size)


if __name__ == '__main__':
    main()
