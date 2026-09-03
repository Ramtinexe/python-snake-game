from turtle import Turtle
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = "green"
class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]


    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color(SNAKE_COLOR)
            new_segment.penup()
            new_segment.goto(0 + (i * -20), 0)
            self.snake_list.append(new_segment)



    def add_segment(self, postion):
        new_segment = Turtle(shape="square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(postion)
        self.snake_list.append(new_segment)


    def extend_snake(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for segment in range(len(self.snake_list)-1 , 0 , -1):
            new_x = self.snake_list[segment - 1].xcor()
            new_y = self.snake_list[segment - 1].ycor()
            self.snake_list[segment].goto(new_x,new_y)
        self.head.forward(MOVE_SPEED)


    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)

