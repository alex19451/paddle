from turtle import Turtle

WIDTH_PADDLE = 1
HEIGHT_PADDLE = 5



class Paddle(Turtle):

    def __init__(self, coordinat):
       super().__init__()
       self.shape("square")
       self.color("white")
       self.shapesize(stretch_wid=HEIGHT_PADDLE, stretch_len=WIDTH_PADDLE )
       self.penup()
       self.goto(coordinat)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor()  - 30
        self.goto(self.xcor(),new_y)


    








    

 

