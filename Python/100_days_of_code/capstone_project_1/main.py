import time
from turtle import Screen
from player import Player  # Ensure the Player class is correctly defined in player.py
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize screen
screen = Screen()
screen.title("Turtle Graphics")  # Set a title for the window
screen.setup(width=600, height=600, startx=100, starty=100)  # Position the window
screen.tracer(0)
scorecard = Scoreboard()
# Short delay to ensure the screen loads properly


# Initialize player
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Update screen
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scorecard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()
        scorecard.increase_level()

# Keep the window open until clicked
screen.exitonclick()
