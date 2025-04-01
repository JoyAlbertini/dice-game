#1- 100 points
#5- 50 points
#Three of a kind of 1 – 1000 points
#Three of a kind of 2 – 200 points
#Three of a kind of 3 – 300 points
#Three of a kind of 4 – 400 points
#Three of a kind of 5 – 500 points
#Three of a kind of 6 – 600 points
#For each number over three of a kind you double the amount (example 3 2’s
#=200, 4 2’s =400, 5 2’s =800, 6 2’s=1,600).
#Pairs and Straights.
# - When a player rolls 1,2,3,4,5,6 when rolling all 6 dice this is a Straight.
# - When a player gets 3 sets of pairs when rolling 6 dice this is Pairs.
# - Pairs and Straights are worth 1000 points


import random
from typing import Any





# in functional style each function should be pure and should not have any side effects,
# because in such way is easier to test and debug each single function

def parse_player_choices_input(choice: str)-> None | list[int]:
    try:
        return [int(x) for x in choice]
    except ValueError:
        return None

def check_if_valid_choice(rolled_set: list[int], choices: list[int]) -> bool:
    if len(choices) > len(rolled_set):
        return False
    available = sorted(rolled_set)
    choices = sorted(choices)

    for i in range(len(choices)):
        if choices[i] != available[i]:
            return False
    return True

def compute_score(verified_choiche: list[int]) -> int:
    ## pattern matching
    match verified_choiche:
        case []:
            return 0
        case [1, *rest]:
            return 100 + compute_score(rest)
        case [1,1,1, * rest]:
            return 1000 + compute_score(rest)
        case [1, 1, 1, 1, *rest]:
            return 2000 + compute_score(rest)
        case [1, 1, 1, 1, 1, *rest]:
            return 4000 + compute_score(rest)
        case [1, 1, 1, 1, 1, 1]:
            return 8000
        case [2, 2, 2, *rest]:
            return 200 + compute_score(rest)
        case [2, 2, 2, 2, *rest]:
            return 400 + compute_score(rest)
        case [2, 2, 2, 2, 2, *rest]:
            return 800 + compute_score(rest)
        case [2, 2, 2, 2, 2, 2]:
            return 1600
        case [3, 3, 3, *rest]:
            return 300 + compute_score(rest)
        case [3, 3, 3, 3, *rest]:
            return 600 + compute_score(rest)
        case [3, 3, 3, 3, 3, *rest]:
            return 1200 + compute_score(rest)
        case [3, 3, 3, 3, 3, 3]:
            return 2400
        case [4, 4, 4, *rest]:
            return 400 + compute_score(rest)
        case [4, 4, 4, 4, *rest]:
            return 800 + compute_score(rest)
        case [4, 4, 4, 4, 4, *rest]:
            return 1600 + compute_score(rest)
        case [4, 4, 4, 4, 4, 4]:
            return 3200
        case [5, *rest]:
            return 50 + compute_score(rest)
        case [5, 5, 5, *rest]:
            return 500 + compute_score(rest)
        case[5, 5, 5, 5, *rest]:
            return 1000 + compute_score(rest)
        case[5, 5, 5, 5, 5, *rest]:
            return 2000 + compute_score(rest)
        case[5, 5, 5, 5, 5, 5]:
            return 4000
        case[6, 6, 6, *rest]:
            return 600 + compute_score(rest)
        case[6, 6, 6, 6, *rest]:
            return 1200 + compute_score(rest)
        case[6, 6, 6, 6, 6, *rest]:
            return 2400 + compute_score(rest)
        case[6, 6, 6, 6, 6, 6]:
            return 4800
        case[1,2,3,4,5,6]:
            return 1000
        case _:
            return 0 + compute_score(verified_choiche[1:])

