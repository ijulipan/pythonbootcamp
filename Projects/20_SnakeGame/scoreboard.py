from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, align="center", font=('Arial', 8, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=('Arial', 20, "normal"))

    def increse_score(self):
        # Updates the scoreboard and refreshes the screen everytime we update the score
        self.score += 1
        self.clear()
        self.update_scoreboard()