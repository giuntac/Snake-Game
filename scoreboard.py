from turtle import Turtle


class Scoreboard(Turtle):
    """The Scoreboard class helps keep track of the user's score.

    Turtle subclass.

    The score is written at the top of the screen.
    When the snake collides with a piece of food the score is updated.
    At the end, the user's score is fetched to be stored in the database.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()  # Remove white arrows
        self.goto(0, 270)
        self.hideturtle()  # Remove the arrow
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the score on the screen.

        When the snake collides with a piece of food the score is
        increased with increase_score() and the latest number is written
        at the top of the screen.
        """
        self.write(f"Score: {self.score}", align="center",
                   font=("Courier New", 24, "normal"))

    def game_over(self):
        """Writes game over on the screen.

        The game ends when the snake collides with either
        the walls or its own tail. When this happens, this function
        writes 'GAME OVER' at the centre of the screen.
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",
                   font=("Courier New", 24, "normal"))

    def increase_score(self):
        """Increases score when necessary.

        When the snake collides with a piece of food
        the score is increased by one point.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_score(self):
        """Fetches the user's final score.

        return : the score at the end of the game (type: int)
        """
        return self.score
