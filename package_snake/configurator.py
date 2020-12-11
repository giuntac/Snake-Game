"""
This module reads config.csv file and sets the correct parameters.

The game can be personalised by the user and the configurator
makes it look like the user specified it in the dedicated csv file.

Functions:
- get_attributes : get background color, snake color, food color and food shape

"""

import csv

default_filename = 'config.csv'


def get_attributes(filename):
    """Gets specified attributes (colors and shapes).

    Returns a list with the specified attributes.
    """

    dict_list = []

    try:
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                background_color = row['background']
                dict_list.append(background_color)
                snake_color = row['snake']
                dict_list.append(snake_color)
                food_color = row['food']
                dict_list.append(food_color)
                food_shape = row['shape']
                dict_list.append(food_shape)

        return dict_list

    except FileNotFoundError:
        print("File %s not found" % filename)


if __name__ == "__main__":

    attributes = get_attributes(default_filename)
