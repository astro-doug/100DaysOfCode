# Project split into 2 days - first day goals:
# Create the snake and display on the screen
# Make the snake move forward automatically
# Allow for control of the snake using the arrow keys
#
# Day 2 goals
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

from turtle import  Screen
from snake import Snake
import time

snake_head: Snake = Snake()


def move_north() -> None:
    global snake_head
    snake_head.change_heading("North")


def move_south() -> None:
    global snake_head
    snake_head.change_heading("South")


def move_east() -> None:
    global snake_head
    snake_head.change_heading("East")


def move_west() -> None:
    global snake_head
    snake_head.change_heading("West")


def setup_screen() -> Screen():
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.delay(0)
    screen.tracer(n=0)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.listen()
    screen.onkey(key="Up", fun=move_north)
    screen.onkey(key="Down", fun=move_south)
    screen.onkey(key="Right", fun=move_east)
    screen.onkey(key="Left", fun=move_west)
    return screen


def main() -> None:
    screen: Screen = setup_screen()

    still_playing: bool = True

    while still_playing:
        time.sleep(.15)
        snake_head.grow_snake()
        screen.update()

    screen.exitonclick()


if __name__ == '__main__':
    main()
