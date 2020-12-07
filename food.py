'''This class includes the code for creating the food'''

import csv
from turtle import Turtle
import random
from configurator import Configurator

configurator = Configurator()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(configurator.get_food_shape())
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(configurator.get_food_color())
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)
