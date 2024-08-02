from turtle import Turtle


class Paddle():
    PADDLE_SIZE: int = 5
    MOVE_DISTANCE: int = 10
    SNAKE_HEADINGS: tuple[str] = ("Up", "Down")
    LEFT_PADDLE_LANE = -350
    RIGHT_PADDLE_LANE = 350
    STARTING_LEFT_LOCATIONS: tuple[int, int] = [(LEFT_PADDLE_LANE, 20), (LEFT_PADDLE_LANE, 10), (LEFT_PADDLE_LANE, 0)
        , (LEFT_PADDLE_LANE, -10), (LEFT_PADDLE_LANE, -20)]
    heading: SNAKE_HEADINGS
    head: Turtle
    paddle_segments: list[Turtle] = []

    def init_segment(self) -> Turtle:
        segment: Turtle = Turtle()
        segment.color("white")
        segment.fillcolor("white")
        segment.shape("square")
        segment.pencolor("white")
        segment.pensize(10)
        segment.penup()
        segment.speed("fastest")
        return segment

    def move_up(self) -> None:
        self.change_heading("Up")
        self.move()

    def move_down(self) -> None:
        self.change_heading("Down")
        self.move()

    def change_heading(self, new_heading: SNAKE_HEADINGS) -> None:
        match new_heading:
            case "Up":
                if self.heading != "Up":
                    self.head.setheading(90)
                    self.heading = "Up"
            case "Down":
                if self.heading != "Down":
                    self.head.setheading(270)
                    self.heading = "Down"

    def move(self) -> None:
        for seq_num in range(len(self.paddle_segments) - 1, 0, -1):
            new_x = int(self.paddle_segments[seq_num - 1].xcor())
            new_y = int(self.paddle_segments[seq_num - 1].ycor())
            self.paddle_segments[seq_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def init_paddle(self) -> None:
        print("In Paddle.init_paddle")
        self.heading = "Up"
        for starting_location in self.STARTING_LEFT_LOCATIONS:
            segment: Turtle = self.init_segment()
            segment.goto(starting_location)
            self.paddle_segments.append(segment)
        self.head = self.paddle_segments[0]
        self.head.setheading(90)

    def __init__(self):
        self.init_paddle()

