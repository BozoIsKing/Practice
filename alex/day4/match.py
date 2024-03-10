import random


class Match:
    def __init__(self, venue, home_team, away_team):
        self.venue = venue
        self.home = home_team
        self.away = away_team

    def play(self):
        roll = random.randint(1, 6)
        if roll > self.away.rating:
            home_goals = roll - self.away.rating
        else:
            home_goals = 0

        roll = random.randint(1, 6)
        if roll > self.home.rating:
            away_goals = roll - self.home.rating
        else:
            away_goals = 0

        return home_goals, away_goals


class Team:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


team1 = Team("Arsenal", 3)
team2 = Team("Atletico Ottawa", 1)

match = Match("Emirates Stadium", team1, team2)
result = match.play()

print(f"Arsenal {result[0]} - {result[1]} Atletico Ottawa")
