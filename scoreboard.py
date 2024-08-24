from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.score = 0
        self.color("white")
        self.write(f"Score:  {self.score}", False, align="center", font=('Arial', 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER U LOSER, HAHA",align="center",font=('Arial',30,"normal"))
    def update_scoreboard(self):
        self.write(f"Score:  {self.score}", False, align="center", font=('Arial', 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()