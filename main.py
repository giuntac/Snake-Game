'''This is our main working file'''

import time
import argparse
import dbmanager as db
from colorama import Fore
from colorama import Style
from turtle import Screen
from package_snake.food import Food
from package_snake.snake import Snake
from package_snake.scoreboard import Scoreboard
from package_snake.configurator import get_attributes

attributes = get_attributes('config.csv')
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(attributes[0])
screen.title("Snake Game")
screen.tracer(0)

# The Snake class creates and moves the snake body, allowing for keys control
snake = Snake()
# The Food class creates and reallocates the food when the snake eats it
food = Food()
# The Scoreboard class maintains the score and creates the scoreboard
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()  # Making the screen to not disappear straight away


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='add a username name', required=False)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    # open the connection and (if necessary) create the users table:
    db.open_and_create()

    if not args.u:
        # the username is missing
        print("Your score cannot be saved.\
                Please enter your username after -u.")
    elif args.u and scoreboard.get_score() != 0:
        # add username and score to scoreboard.db
        db.save_new_username(args.u, scoreboard.get_score())
        print(f"Well done {args.u}!",
              f"Your score is: {Fore.GREEN}\
              {scoreboard.get_score()}{Style.RESET_ALL}!")
        # the player scored zero
    else:
        print(f"Ouch {Fore.MAGENTA}{args.u}{Style.RESET_ALL}!\
              This is the lowest possible score!\n",
              "Score at least 1 to be classified among other players.")
