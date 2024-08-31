from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, 'w')
screen.onkey(r_paddle.down, 's')
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    # Detect collision with top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    
    
    #Detect collision with right wall and score a point to left player
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with left wall and score a point to right player
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()