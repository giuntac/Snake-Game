import csv

class Configurator():
    """Reads config.csv file and sets the correct parameters.

    The game can be personlized by the user and the confidgurator
    makes it look like the user specified in the dedicated csv file.

    Functions:
    - get_background : get background color
    - get_snake_color : get snake color
    - get_food_color : get food color
    - get_food_shape : get food shape
    
    """

    def __init__(self):
        self.file = 'config.csv'

    def get_background(self):
        """Gets specified background color.
        
        Returns a string.
        """
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.background_color = str(row[0])
        return self.background_color

    def get_snake_color(self):
        """Gets specified snake color.
        
        Returns a string.
        """
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.snake_color = str(row[1])
        return self.snake_color

    def get_food_color(self):
        """Gets specified food color.
        
        Returns a string.
        """
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.food_color = str(row[2])
        return self.food_color

    def get_food_shape(self):
        """Gets specified food shape.
        
        Returns a string.
        """
        with open(self.file) as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            next(self.csv_reader)
            for row in self.csv_reader:
                self.food_shape = str(row[3])
        return self.food_shape
