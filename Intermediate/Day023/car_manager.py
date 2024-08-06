from turtle import Turtle
import random

current_move_speed: int
car_list: list[Turtle] = []


class CarManager:
    CAR_COLORS: tuple[str] = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    STARTING_MOVE_DISTANCE: int = 5
    MOVE_SPEED_INCREMENT: int = 10
    X_STARTING: int = 280
    LEFT_EDGE: int = -300

    def move_cars(self) -> None:
        global car_list
        global current_move_speed
        for car in car_list:
            car.forward(current_move_speed)
            if car.xcor() < self.LEFT_EDGE:
                print("destroying car")
                car_list.remove(car)
                car.hideturtle()
                car.clear()

    def increase_speed(self) -> None:
        global current_move_speed
        current_move_speed += CarManager.MOVE_SPEED_INCREMENT

    def check_car_overlap(self, new_car: Turtle) -> bool:
        for car in car_list:
            if new_car.xcor() - 40 <= car.xcor() <= new_car.xcor() + 40:
                return True
        return False

    def create_new_car(self, random_x: bool) -> None:
        global car_list
        car: Turtle = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        if random_x:
            car.setx(random.randint(-200, 280))
        else:
            car.setx(CarManager.X_STARTING)
        car.sety(int(random.randrange(-240, 280, 40)))
        car.setheading(180)
        car.color(random.choice(CarManager.CAR_COLORS))
        if not self.check_car_overlap(car):
            print("new car ok")
            car_list.append(car)
        else:
            print("new car not ok")
            car.clear()
            car.hideturtle()

    def print_cars(self) -> None:
        print(f"{len(car_list)} cars")

    def __init__(self):
        global current_move_speed
        current_move_speed = CarManager.STARTING_MOVE_DISTANCE
        #pass