import csv
from turtle import Turtle
import random
from configurator import get_attributes

attributes = get_attributes('config.csv')

class Food(Turtle):
    """Controls everything realted to the food.

    Turtle subclass. 
    
    Functions:
    - refresh : creates a new piece of food

    """

    def __init__(self):
        super().__init__()
        self.shape(attributes[3])
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(attributes[2])
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Creates a new random set of coordinates.

        A new piece of food is created at the coordinates 
        randomly generated here.
        """

        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)
