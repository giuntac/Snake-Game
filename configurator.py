"""
This module reads config.csv file and sets the correct parameters.

The game can be personalised by the user and the configurator
fetches information the user gave via terminal.

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
    edit = input(
        "You just launched the configuration script.\
             Do you want to change the configuration parameters? (y/N) ")
    if edit.upper() in ["YES", "Y"]:
        background_color = input(f"Background color: [{attributes[0]}] ")
        snake_color = input(f"Snake color: [{attributes[1]}] ")
        food_color = input(f"Food color: [{attributes[2]}] ")
        food_shape = input(f"Food shape: [{attributes[3]}] ")
        with open('config.csv', 'w', newline='') as csvfile:
            fieldnames = ['background', 'snake', 'food', 'shape']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'background': background_color,
                             'snake': snake_color, 'food': food_color,
                             'shape': food_shape})

    # Checking again the modifications with another query
    attributes = get_attributes(default_filename)
    print(f"This is your configuration:\n{attributes}")
