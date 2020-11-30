
''' This class help to keep track of the score and create the scoreboard '''

from turtle import Turtle

Class Scorebaord(Turtle):

    def __init__(self):
	super().__init__()
	self.score = 0
	self.color("white")
	self.penup() #remove white arrows
	self.goto(0, 260)
	self.hideturtle() #to remove the arrow
	self.update_scoreboard
	
	

    def update_scoreboard(self):
	self.write(f"Score: {self.score}", align="centre", font=("Courier New", 24, "normal"))

    def increase_score(self):
	self.score += 1
	self.clear()
	self.update_scoreboard()
