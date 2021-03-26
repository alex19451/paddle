from turtle import Turtle


ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, coordinat):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(coordinat)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score {self.score}", align = ALIGMENT , font = FONT)

    def increare_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = ALIGMENT , font = FONT)