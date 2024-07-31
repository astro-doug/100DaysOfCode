from turtle import Turtle


class Snake:
    SNAKE_HEADINGS: tuple[str] = ("North", "South", "East", "West")
    STARTING_LOCATIONS: tuple[float, float] = [(0, 0), (-10, 0), (-20, 0)]
    MOVE_DISTANCE: int = 10
    snake_segments: list[Turtle] = []
    heading: SNAKE_HEADINGS
    snake_length: int = 1

    def change_heading(self, new_heading: SNAKE_HEADINGS) -> None:
        match new_heading:
            case "North":
                if self.heading != "South":
                    self.snake_segments[0].setheading(90)
                    self.heading = "North"
            case "South":
                if self.heading != "North":
                    self.snake_segments[0].setheading(270)
                    self.heading = "South"
            case "East":
                if self.heading != "West":
                    self.snake_segments[0].setheading(0)
                    self.heading = "East"
            case "West":
                if self.heading != "East":
                    self.snake_segments[0].setheading(180)
                    self.heading = "West"

    def grow_snake(self) -> None:
        for seq_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seq_num - 1].xcor()
            new_y = self.snake_segments[seq_num - 1].ycor()
            self.snake_segments[seq_num].goto(new_x, new_y)
        self.snake_segments[0].forward(self.MOVE_DISTANCE)

        self.snake_length += 1

    def init_snake(self) -> None:
        for starting_location in self.STARTING_LOCATIONS:
            segment: Turtle = Turtle(shape="square")
            segment.color("grey")
            segment.fillcolor("grey")
            segment.pencolor("grey")
            segment.shapesize(stretch_wid=.5, stretch_len=.5)
            segment.penup()
            segment.goto(starting_location)
            self.snake_segments.append(segment)

    def __init__(self):
        self.init_snake()
        self.heading = "East"
