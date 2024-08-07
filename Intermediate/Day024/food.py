from turtle import Turtle
import random


class Food:
    x_pos: int = 0
    y_pos: int = 0
    food_item: Turtle
    x_screen_size: int = 0
    y_screen_size: int = 0

    def set_food_bounds(self, x_size: int, y_size: int) -> None:
        self.x_screen_size = x_size
        self.y_screen_size = y_size

    def add_food(self) -> None:
        self.x_pos = int(random.randint(int(-self.x_screen_size/2), int(self.x_screen_size/2)) * 10 / 10)
        self.y_pos = int(random.randint(int(-self.y_screen_size/2), int(self.y_screen_size/2)) * 10 / 10)
        self.food_item.goto(self.x_pos, self.y_pos)

    def move_food(self) -> None:
        self.add_food()

    def __init__(self,):
        self.food_item: Turtle = Turtle("circle")
        self.food_item.color("blue")
        self.food_item.speed("fastest")
        self.food_item.penup()
        self.food_item.shapesize(stretch_wid=.5, stretch_len=.5)