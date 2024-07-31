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

#TODO: Rewrite to use PyGame instead of Python Turtle

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake_head: Snake = Snake()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


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
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
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


def check_food_collision(food: Food) -> bool:
    global snake_head
    if snake_head.snake_segments[0].distance(food.x_pos, food.y_pos) < 15:
        return True
    else:
        return False


def check_edge_collision() -> bool:
    global snake_head

    if (snake_head.snake_segments[0].xcor() <= -SCREEN_WIDTH/2 - 20
            or snake_head.snake_segments[0].xcor() >= SCREEN_WIDTH/2 - 20
            or snake_head.snake_segments[0].ycor() <= -SCREEN_HEIGHT/2 - 20
            or snake_head.snake_segments[0].ycor() >= SCREEN_HEIGHT/2 - 20):
        return True
    else:
        return False


def main() -> None:
    global snake_head
    screen: Screen = setup_screen()
    scoreboard: Scoreboard = Scoreboard()
    scoreboard.update_scoreboard()

    still_playing: bool = True
    food: Food = Food()
    food.set_food_bounds(x_size=SCREEN_WIDTH - 10, y_size=SCREEN_HEIGHT - 10)
    food.add_food()

    while still_playing:
        time.sleep(.15)
        snake_head.move()
        screen.update()
        if check_food_collision(food):
            snake_head.grow()
            scoreboard.score_point()
            scoreboard.update_scoreboard()
            food.move_food()
        if check_edge_collision():
            still_playing = False
            scoreboard.game_over()
        if snake_head.detect_tail_collision():
            still_playing = False
            scoreboard.game_over()
    screen.exitonclick()


if __name__ == '__main__':
    main()
