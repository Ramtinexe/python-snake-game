from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()


screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(my_food) < 15:
        my_food.re_location()
        my_snake.extend_snake()
        my_scoreboard.increase_score()

    if (my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or
        my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280):
          is_game_on = False
          my_scoreboard.game_over()

    for segment in my_snake.snake_list[1:]:

        if my_snake.head.distance(segment) < 10:
            is_game_on = False
            my_scoreboard.game_over()






screen.exitonclick()