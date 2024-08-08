from turtle import Turtle
from typing import Final


class Snake:
    SNAKE_HEADINGS: Final[tuple[str]] = ("North", "South", "East", "West")
    STARTING_LOCATIONS: Final[tuple[int, int]] = [(0, 0), (-10, 0), (-20, 0)]
    MOVE_DISTANCE: Final[int] = 20
    snake_segments: list[Turtle] = []
    heading: SNAKE_HEADINGS
    head: Turtle

    def change_heading(self, new_heading: SNAKE_HEADINGS) -> None:
        match new_heading:
            case "North":
                if self.heading != "South":
                    self.head.setheading(90)
                    self.heading = "North"
            case "South":
                if self.heading != "North":
                    self.head.setheading(270)
                    self.heading = "South"
            case "East":
                if self.heading != "West":
                    self.head.setheading(0)
                    self.heading = "East"
            case "West":
                if self.heading != "East":
                    self.head.setheading(180)
                    self.heading = "West"

    def move(self) -> None:
        for seq_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = int(self.snake_segments[seq_num - 1].xcor())
            new_y = int(self.snake_segments[seq_num - 1].ycor())
            self.snake_segments[seq_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def grow(self) -> None:
        segment: Turtle = self.make_new_segment()
        segment.forward(self.MOVE_DISTANCE)
        self.snake_segments.append(segment)
        # for x in self.snake_segments:
        #    print(f"({x.xcor()}, {x.ycor()})")

    def make_new_segment(self) -> Turtle:
        segment: Turtle = Turtle(shape="square")
        segment.color("green")
        segment.fillcolor("green")
        segment.pencolor("green")
        segment.penup()

        return segment

    def init_snake(self) -> None:
        for starting_location in self.STARTING_LOCATIONS:
            segment: Turtle = self.make_new_segment()
            segment.goto(starting_location)
            self.snake_segments.append(segment)
        self.head = self.snake_segments[0]

    def detect_tail_collision(self) -> bool:
        # slicing - will grab segments in list from position 1 through end
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def reset_snake(self) -> None:
        for segment in self.snake_segments:
            segment.hideturtle()
        self.snake_segments = []
        self.init_snake()
        self.heading = "East"

    def __init__(self):
        self.init_snake()
        self.heading = "East"
