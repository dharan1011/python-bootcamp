import random
class ScoreBoard:
    def __init__(self, team_one_name, team_two_name):
        self.team_one = team_one_name
        self.team_two = team_two_name
        self.team_one_score = 0
        self.team_two_score = 0

    def coin_toss(self):
        possibility = ["heads", "tails"]
        rand = random.randint(1,100)
        if(rand % 2 == 0):
            self.batting_team = self.team_one
            self.bowling_team = self.team_two
        else:
            self.batting_team = self.team_two
            self.bowling_team = self.team_one
    
    def score(self, runs):
        if(self.batting_team == self.team_one):
            self.team_one_score += runs
        else:
            self.team_two_score += runs
    
    def print_scoreboard(self):
        print(self.batting_team,"Score is ",end="")
        if(self.batting_team == self.team_one):
            print(self.team_one_score)
        else:
            print(self.team_two_score)

sc = ScoreBoard("India","AUS")
sc.coin_toss()
sc.score(4)
sc.score(1)
sc.score(6)
sc.print_scoreboard()