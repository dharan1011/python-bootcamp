"""
-- properties -- what it contains
runs
wicket
strike batsman name
strike batsman runs
non-strike batsman name
non-strike batsman runs
bowler name
overs
ball in over

-- action -- what it does

display strike batsman score
display non strike batsman score
display current over
display current ball
display bowler name
display total runs

on runs scored
on wicket
on strike rotate
change over
"""

class scoreboard:
    def __init__(self):
        self.runs = 0
        self.wickets = 0
        self.strike_batsman = ""
        self.strike_batsman_runs = 0
        self.non_strike_batsman = ""
        self.non_strike_batsman_runs = 0
        self.bowler = ""
        self.overs = 0
        self.ball_in_over = 0

    def display_strike_batsman_score(self):
        print(self.strike_batsman,":",self.strike_batsman_runs)

    def display_non_strike_batsman_score(self):
        print(self.non_strike_batsman,":",self.non_strike_batsman_runs)

    def display_over(self):
        print("current over :", self.overs)
    
    def display_current_ball(self):
        print("current ball :", self.ball_in_over)

    def display_total_runs(self):
        print("total runs :", self.runs)

    def on_runs_scored(self, runs_scored):
        self.strike_batsman_runs += runs_scored
        self.runs += runs_scored

    def on_strike_rotate(self):
        self.strike_batsman, self.non_strike_batsman = self.non_strike_batsman, self.strike_batsman
        self.strike_batsman_runs, self.non_strike_batsman_runs = self.non_strike_batsman, self.strike_batsman_runs

    def on_wicket(self):
        if(self.wicket <= 10):
            self.wicket += 1
        if(self.wicket == 11):
            print("All Out")
        print("Out batsman :", self.strike_batsman)
    
    def change_over(self):
        self.over += 1
