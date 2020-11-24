'''This class includes the code needed create the snake body'''

from turtle import Screen, Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]  

class Snake:

	def __init__(self):
	    self.segments = []
	    self.create_snake()
	    self.head=self.segments[0]

	def create_snake(self):
	    for position in STARTING_POSITIONS:
	        new_segment = Turtle("square")
	        new_segment.color("white")
	        new_segment.penup()
	        new_segment.goto(position)
	        self.segments.append(new_segment)

