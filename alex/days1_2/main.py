import football

"""teams = [
    "Arsenal",
    "Chelsea",
    "Manchester United",
    "Milan",
    "Inter",
    "Barcelona",
    "PSG",
    "CF Montreal",
    "Roma",
    "Real Madrid",
    "Bayern Munich",
    "Ajax",
    "Marseille",
    "Toronto FC",
    "LA Galaxy",
    "Celtic",
    "Alcorcón"
]"""

teams = []

while True:
    try:
        num_teams = int(input("how many teams do you want? "))
        assert num_teams > 0
        break
    except (ValueError, AssertionError):
        print("Please enter a integer greater than 0")

while True:
    try:
        num_groups = int(input("how many groups do you want? "))
        assert num_teams >= num_groups > 0
        break
    except (ValueError, AssertionError):
        print("Please enter a integer greater than 0 but less than or equal the number of teams")

for i in range(num_teams):
    teams.append(input("what do you want to name your team? "))

print("\n")

groups = football.make_groups(teams, num_groups)

for i, group in enumerate(groups):
    print(f"Group {i+1}: " + ", ".join(group))
