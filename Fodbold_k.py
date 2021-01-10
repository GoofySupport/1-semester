"""
Created on Mon Nov 16 09:20:41 2020

@author: Kristoffer Karlsen

Email : Kkarls18@student.aau.dk

Gruppe 308Ac 

Lavet i sammenarbejde med medlemer fra anden gruppe.

"""

import os

nations_file = r"C:\Users\Bruger\Desktop\Eksamen\Calculus (CAL) - MAT_MAOK_MATT 14-01-2019\AUU MATØK\Python\nations.txt"
round_files = [r"C:\Users\Bruger\Desktop\Eksamen\Calculus (CAL) - MAT_MAOK_MATT 14-01-2019\AUU MATØK\Python\round1.txt", r"C:\Users\Bruger\Desktop\Eksamen\Calculus (CAL) - MAT_MAOK_MATT 14-01-2019\AUU MATØK\Python\round2.txt", r"C:\Users\Bruger\Desktop\Eksamen\Calculus (CAL) - MAT_MAOK_MATT 14-01-2019\AUU MATØK\Python\round3.txt"]
results_list = [0, 0, 0, 0]

#opner filerne og for dem sat iorden 

def get_nations():
    with open(nations_file, "r") as f:
        nation = f.read()
    nations = nation.rstrip().split("\n")
    return nations

#behandling af kampene 

def get_matches(match_files):
    all_matches = []
    if isinstance(match_files, list):
        for match in match_files:
            with open(match, "r") as f:
                round_matches = f.read()
            round_matches = round_matches.rstrip().split("\n")
            for r in round_matches:
                all_matches.append(r)
    elif isinstance(match_files, str):
        with open(match_files, "r") as f:
            round_matches = f.read()
        round_matches = round_matches.rstrip().split("\n")
        for r in round_matches:
            all_matches.append(r)

    return all_matches

#Tjekker for hvilket hold der vinder og retunere det 
def get_winner_teams(matches):
    winners = []
    for match in matches:
        if _get_team_score(match, "s")[0] > _get_team_score(match, "s")[1]:
            winners.append(_get_team_score(match, 't')[0])
        elif _get_team_score(match, "s")[0] < _get_team_score(match, "s")[1]:
            winners.append(_get_team_score(match, 't')[1])
        else:
            winners.append(_get_team_score(match, 't'))
    return winners

#winner eller taber
def _get_team_score(match, team_score):
    if team_score == "t":
        team = match.split()[:3]
        team.pop(1)
        return team
    elif team_score == "s":
        score = match.split()[-3:]
        score.pop(1)
        for s in range(len(score)):
            score[s] = int(score[s])
        return score

# point optælling
def update_score(matches):
    winners = get_winner_teams(get_matches(matches))
    teams = get_nations()
    for winner in winners:
        if winner in teams:
            for i in range(len(teams)):
                if winner == teams[i]:
                    results_list[i] += 3
        else:
            if isinstance(winner, list):
                for r in winner:
                    for i in range(len(teams)):
                        if r == teams[i]:
                            results_list[i] += 1
                         
hold = get_nations()
update_score(round_files)
for i, v in enumerate(sorted(results_list, reverse = True)):
    print(f"{hold[i]} - PTS: {v}")