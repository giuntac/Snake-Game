'''This is out main working file'''

# Start from creating the snake

from turtle import Screen, Turtle
import time 
from snake import Snake #importing the class

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake() #calling class
# the class creates the snake body

#screen.update()
#2. move the snake automatically

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    
    for seg_num in range(len(segments)-1,0,-1):
    #start where we start the range, stop and step - we want to go from 2 1, step -1
        new_x= segments[seg_num -1].xcor()
        new_y=segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)#we want the third segment to go to the second position
#we have to move also the first segment away 
    segments[0].forward(20)
    segments[0].left(90)
    #the pieces will do only a circle 
    
    #we need to think about segments that move in a graph

#3 Control the snake using the up-down-left-right arrow keys.

screen.listen()       
screen.onkey(‘Up’)
screen.onkey(‘Down’)
screen.onkey(‘Left’)
screen.onkey(‘Right)


head = segments[0]
up = 90
down = 270
left = 180
right = 0 

#Move the head of the snake (segment[0]) by 0,90,180 or 270 degrees.

def up():
    if head.heading() != down: 
        head.setheading(up) #if it goes up, it cannot go down
def down():
    if head.heading() != up: 
        head.setheading(down) #if it goes down, it cannot go up 
def left():
    if head.heading() != right: 
        head.setheading(left) #if it goes left, it cannot go right
def right():
    if head.heading() != left: 
        head.setheading(right) #if it goes right, it cannot go left
      
                                  
                                      
                                      
                                      
                                      






screen.exitonclick() #run it it does not disappear straight away 
