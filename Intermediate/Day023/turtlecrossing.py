from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time
import random

player: Player

def init_screen(screen: Screen) -> None:
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("PyTurtle Crossing")
    screen.bgcolor("white")


def move() -> None:
    global player
    player.move_up()


def main() -> None:
    global player
    still_playing: bool = True
    screen: Screen() = Screen()
    init_screen(screen)
    player = Player()
    scoreboard: Scoreboard = Scoreboard()
    scoreboard.update_scoreboard()
    screen.listen()
    screen.onkey(fun=move, key="Up")
    car_manager: CarManager = CarManager()
    for _ in range(10):
        car_manager.create_new_car(random_x=True)

    while still_playing:
        car_manager.move_cars()
        if car_manager.check_collision(player):
            still_playing = False
            scoreboard.crash()
        else:
            create_new_car: bool = random.choice((True, False, False, False, False))
            if create_new_car:
                car_manager.create_new_car(random_x=False)
            car_manager.print_cars()
            if player.check_reached_end():
                scoreboard.increase_level()
                player.start_turtle()
                car_manager.increase_speed()
            screen.update()
            time.sleep(.1)

    screen.exitonclick()


if __name__ == '__main__':
    main()
