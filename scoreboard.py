from turtle import Turtle
FONT = ("Courier", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__() 
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.updateScore()
        

    def updateScore(self):
        self.write(f"Level: {self.level} ", font = FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", font = FONT)

    def increaseScore(self):
        self.level += 1
        self.clear()
        self.updateScore()

