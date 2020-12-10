import csv
from turtle import Screen, Turtle
from configurator import get_attributes

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

attributes = get_attributes('config.csv')

class Snake:
    """Controls everything snake-related from appearance to behavior. 
    
    The functions included are used to create, move 
    and control (with arrowkeys) the snake. 
    Functions:
    - create_snake : creates snake body
    - add_segment : adds segment to snake body
    - extend : extends snake body
    - move : moves snake body
    - up : makes snake go up
    - down : makes snake go down
    - left : makes snake go left
    - right : makes snake go right

    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake body on the screen.
        
        Three white squares are drawn on the screen at the chosen
        starting poistions.
        """
        for position in STARTING_POSITIONS:
            # Add a segment to the position we are looping through
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a segment to the snake when it eats food.
        ----------
        Parameters
        ----------
        position : coordinated at which to add a segment
        """
        new_segment = Turtle("square")
        new_segment.color(attributes[1])
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the snake body with a new segment.
        
        The new segment is added to the position of the last segment
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Makes the snake body move continuously.
        """
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Control the snake with arrowkeys.
        
        If the snake is going up it can't go down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Control the snake with arrowkeys.
        
        If the snake is going down it can't go up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Control the snake with arrowkeys.
        
        If the snake is going left it can't go right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Control the snake with arrowkeys.
        
        If the snake is going right it can't go left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
