'''This class incudes the code to read config.csv file and set the correct parameters'''

import csv

class Configurator():

    def __init__(self):
        self.file = 'config.csv'

    def get_background(self):
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.background_color = str(row[0])
        return self.background_color

    def get_snake_color(self):
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.snake_color = str(row[1])
        return self.snake_color

    def get_food_color(self):
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.food_color = str(row[2])
        return self.food_color

    def get_food_shape(self):
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.food_shape = str(row[3])
        return self.food_shape
