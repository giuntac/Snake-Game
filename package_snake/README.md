# Snake Game 🐍

Feeling nostalgic for retro games? No worries, in this repository you will find a `main.py` file that allows you to dive into your childhood memories and play the most famous video games of all times: the Snake Game 🐍 <br/>But don't leave me yet because there are many more things you need to know and discover and you will be required to give some specific parameters to the program.

If you run the program, executing the main file with: `$ python main.py -u playername` a window with a small cubic segment moving around appears on your screen, and that's your time to play! 

![](snake_game.gif)

> Note: the project requires the following modules to run: Turtle, argparse, sqlite3, unittest2, colorama, random, os, csv

You can use the arrow keys of your computer keyboard to move the snake around and try to eat the pieces of food in its path so it can grow in length. For each piece of food the snake eats, and additional point is added to your score but as in the real game, every time the snake collides with the walls of the window or its own tail, then it's GAME OVER 👾❌ 

Don't worry, you can play as many times as you want and your score will be saved together with your competitors' ones so you can always check your ranking and try to beat their score! We have also provided you with the possibility to personalise your game, choosing the colour of the backgorund or the snake, and even the shape of the food, but don't worry I will exlpain you everything step by step!

## Command Line Parameters
As previously explained in the introduction, some command are required in order to run our main script.
When we run python3 main.py we can play but without savings our score and username.

On the other have two possibilities:
1. insert the username and store our username and score;
2. see the statistics of the scoreboard.

These two possibilities are possible thanks to the following commands:

1. Positional arguments
   * -u: adds the username 

2. Optional arguments
   * -c: checks for the username and return the score 
   * -m: returns max score 
   * -l: prints all users and their related scores

## How to Change Usability Features 💻
If you want to change the usability features you have to execute `$ python configurator.py`. 
After that you will be asked to choose between:
1. `y` (yes) you will be able to change background color, snake color, food color, and food shape;
2. `N` (no) you will exit from this command. 

Accordingly with your choices you can now start `$ python main.py -u playername` with the new features (if you chose y), on the other hand you will play with default features.

## Testing ❌ ✅
Tests of the configurator.py file are here: package_name/tests/ .
You will find one module test_configurator.py .
To run them from the main folder use: python3 -m unittest2 -v -b package_snake/tests/test_configurator.py .

