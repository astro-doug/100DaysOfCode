from turtle import Turtle, Screen

timmy: Turtle = Turtle()


def move_forwards() -> None:
    global timmy
    timmy.forward(10)


def move_backwards() -> None:
    global timmy
    timmy.back(10)


def rotate_left() -> None:
    global timmy
    timmy.left(10)


def rotate_right() -> None:
    global timmy
    timmy.right(10)


def reset() -> None:
    global timmy
    timmy.penup()
    timmy.home()
    timmy.clear()
    timmy.pendown()


def main() -> None:
    global timmy
    screen: Screen = Screen()
    screen.listen()
    screen.onkey(key="W", fun=move_forwards)
    screen.onkey(key="S", fun=move_backwards)
    screen.onkey(key="A", fun=rotate_left)
    screen.onkey(key="D", fun=rotate_right)
    screen.onkey(key="C", fun=reset)

    screen.exitonclick()


if __name__ == '__main__':
    main()
