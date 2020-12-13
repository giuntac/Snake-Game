import argparse
import time
from turtle import Screen
from colorama import Fore, Style
import package_snake.dbmanager as db
from configurator import get_attributes
from package_snake.food import Food
from package_snake.results import check_score, max_score, print_all_users
from package_snake.scoreboard import Scoreboard
from package_snake.snake import Snake

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


def parse_args():
    """Parses the parameters inserted in the command line.
    ----------
    Parameters
    ----------
    -u : specify a username to play with
    -c : check for a user's score
    -m : look for max score
    - l : list all users and scores
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='add a username name', required=False)
    parser.add_argument('-c', help="check for a username and return the score",
                        required=False)  # optional
    parser.add_argument('-m', help="return max score", action='store_true',
                        required=False)  # optional
    parser.add_argument('-l', help="list all users and scores",
                        action='store_true',
                        required=False)  # optional
    args = parser.parse_args()
    return args


def main():
    """This function handles the arguments given by
    the user and accordingly launches the right respective
    functions inside external modules to play.
    """
    args = parse_args()
    exit = False
    # Checking optional arguments. If selected, show scores
    if args.c:
        check_score(args.c)
        exit = True
    if args.m:
        max_score()
        exit = True
    if args.l:
        print_all_users()
        exit = True
    if exit:
        return
    # If user setted -u play the game
    # open the connection and (if necessary) create the users table:
    db.open_and_create()

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


if __name__ == "__main__":
    main()
