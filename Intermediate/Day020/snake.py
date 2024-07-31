from turtle import Turtle


class Snake:
    snake_headings: tuple[str] = ("North", "South", "East", "West")

    snake: Turtle
    heading: snake_headings
    length: int = 1

    def change_heading(self, new_heading: snake_headings) -> None:
        match new_heading:
            case "North":
                if self.heading != "South":
                    self.snake.setheading(90)
                    self.heading = "North"
            case "South":
                if self.heading != "North":
                    self.snake.setheading(270)
                    self.heading = "South"
            case "East":
                if self.heading != "West":
                    self.snake.setheading(0)
                    self.heading = "East"
            case "West":
                if self.heading != "East":
                    self.snake.setheading(180)
                    self.heading = "West"

    def grow_snake(self) -> None:
        print("growing snake")
        self.snake.forward(10)
        self.snake.stamp()
        self.length += 1

    def init_turtle(self) -> None:
        self.snake = Turtle(shape="square")
        self.snake.color("grey")
        self.snake.fillcolor("grey")
        self.snake.pencolor("grey")
        self.snake.shapesize(stretch_wid=.5, stretch_len=.5)
        self.snake.penup()
        for _ in range(3):
            self.grow_snake()

    def __init__(self):
        self.init_turtle()

        self.heading = "East"
