from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard_right = Scoreboard((320,260))
scoreboard_left = Scoreboard((-320,260))


screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong game")
screen.listen()
screen.onkey(left_paddle.go_up, "o")
screen.onkey(left_paddle.go_down, "l")

screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() <-280 :
       ball.bounce_ball()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() >340 or ball.distance(left_paddle) < 50 and ball.xcor() > -340 :
        ball.bounce_ball_x()

    if ball.xcor() > 380:
        ball.reset_posstion()
        scoreboard_left.increare_score()
        
    elif ball.xcor() <-380:
        ball.reset_posstion()
        scoreboard_right.increare_score()
    
    if scoreboard_left.score > 5 or scoreboard_right.score > 5:
        game_is_on = False
        scoreboard_left.game_over()
        scoreboard_right.game_over()



screen.exitonclick()
