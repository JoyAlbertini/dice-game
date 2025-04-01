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


from collections import Counter


# in functional style each function should be pure and should not have any side effects,
# because in such way is easier to test and debug each single function

def parse_player_choices_input(choice: str)-> None | list[int]:
    try:
        return [int(x) for x in choice]
    except ValueError:
        return None

def check_match_with_the_rolled_set(rolled_set: list[int], choices: list[int]) -> bool:
    if len(choices) > len(rolled_set):
        return False
    rolled_counter = Counter(rolled_set)
    choices_counter = Counter(choices)

    return all(rolled_counter[num] >= count for num, count in choices_counter.items())


def compute_score(verified_choice: list[int]) -> int:
    if len(verified_choice) == 6:
        counts = Counter(verified_choice)
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            return 1000

    match verified_choice:
        case [1, 2, 3, 4, 5, 6]:
            return 1000

    match verified_choice:
        case [1, 1, 1, 1, 1, 1]:
            return 8000
        case [1, 1, 1, 1, 1, *rest]:
            return 4000 + compute_score(rest)
        case [1, 1, 1, 1, *rest]:
            return 2000 + compute_score(rest)
        case [1, 1, 1, *rest]:
            return 1000 + compute_score(rest)
        case [1, *rest]:
            return 100 + compute_score(rest)

    match verified_choice:
        case [2, 2, 2, 2, 2, 2]:
            return 1600
        case [2, 2, 2, 2, 2, *rest]:
            return 800 + compute_score(rest)
        case [2, 2, 2, 2, *rest]:
            return 400 + compute_score(rest)
        case [2, 2, 2, *rest]:
            return 200 + compute_score(rest)

    match verified_choice:
        case [3, 3, 3, 3, 3, 3]:
            return 2400
        case [3, 3, 3, 3, 3, *rest]:
            return 1200 + compute_score(rest)
        case [3, 3, 3, 3, *rest]:
            return 600 + compute_score(rest)
        case [3, 3, 3, *rest]:
            return 300 + compute_score(rest)

    match verified_choice:
        case [4, 4, 4, 4, 4, 4]:
            return 3200
        case [4, 4, 4, 4, 4, *rest]:
            return 1600 + compute_score(rest)
        case [4, 4, 4, 4, *rest]:
            return 800 + compute_score(rest)
        case [4, 4, 4, *rest]:
            return 400 + compute_score(rest)

    match verified_choice:
        case [5, 5, 5, 5, 5, 5]:
            return 4000
        case [5, 5, 5, 5, 5, *rest]:
            return 2000 + compute_score(rest)
        case [5, 5, 5, 5, *rest]:
            return 1000 + compute_score(rest)
        case [5, 5, 5, *rest]:
            return 500 + compute_score(rest)
        case [5, *rest]:
            return 50 + compute_score(rest)

    match verified_choice:
        case [6, 6, 6, 6, 6, 6]:
            return 4800
        case [6, 6, 6, 6, 6, *rest]:
            return 2400 + compute_score(rest)
        case [6, 6, 6, 6, *rest]:
            return 1200 + compute_score(rest)
        case [6, 6, 6, *rest]:
            return 600 + compute_score(rest)

    if verified_choice:
        return compute_score(verified_choice[1:])
    else:
        return 0


def nr_of_scoring_dices(verified_choice: list[int]) -> int:
    match verified_choice:
        case [1, 2, 3, 4, 5, 6]:
            return 6  # straight uses all dice

    match verified_choice:
        case [1, 1, 1, 1, 1, 1]:
            return 6
        case [1, 1, 1, 1, 1, *rest]:
            return 5 + nr_of_scoring_dices(rest)
        case [1, 1, 1, 1, *rest]:
            return 4 + nr_of_scoring_dices(rest)
        case [1, 1, 1, *rest]:
            return 3 + nr_of_scoring_dices(rest)
        case [1, *rest]:
            return 1 + nr_of_scoring_dices(rest)

    match verified_choice:
        case [2, 2, 2, 2, 2, 2]:
            return 6
        case [2, 2, 2, 2, 2, *rest]:
            return 5 + nr_of_scoring_dices(rest)
        case [2, 2, 2, 2, *rest]:
            return 4 + nr_of_scoring_dices(rest)
        case [2, 2, 2, *rest]:
            return 3 + nr_of_scoring_dices(rest)

    match verified_choice:
        case [3, 3, 3, 3, 3, 3]:
            return 6
        case [3, 3, 3, 3, 3, *rest]:
            return 5 + nr_of_scoring_dices(rest)
        case [3, 3, 3, 3, *rest]:
            return 4 + nr_of_scoring_dices(rest)
        case [3, 3, 3, *rest]:
            return 3 + nr_of_scoring_dices(rest)

    match verified_choice:
        case [4, 4, 4, 4, 4, 4]:
            return 6
        case [4, 4, 4, 4, 4, *rest]:
            return 5 + nr_of_scoring_dices(rest)
        case [4, 4, 4, 4, *rest]:
            return 4 + nr_of_scoring_dices(rest)
        case [4, 4, 4, *rest]:
            return 3 + nr_of_scoring_dices(rest)

    match verified_choice:
        case [5, 5, 5, 5, 5, 5]:
            return 6
        case [5, 5, 5, 5, 5, *rest]:
            return 5 + nr_of_scoring_dices(rest)
        case [5, 5, 5, 5, *rest]:
            return 4 + nr_of_scoring_dices(rest)
        case [5, 5, 5, *rest]:
            return 3 + nr_of_scoring_dices(rest)
        case [5, *rest]:
            return 1 + nr_of_scoring_dices(rest)

    match verified_choice:
        case [6, 6, 6, 6, 6, 6]:
            return 6
        case [6, 6, 6, 6, 6, *rest]:
            return 5 + nr_of_scoring_dices(rest)
        case [6, 6, 6, 6, *rest]:
            return 4 + nr_of_scoring_dices(rest)
        case [6, 6, 6, *rest]:
            return 3 + nr_of_scoring_dices(rest)

    if verified_choice:
        return nr_of_scoring_dices(verified_choice[1:])
    else:
        return 0


def match_the_number_of_scoring_dices(choices: list[int]) -> bool:
    return len(choices) == nr_of_scoring_dices(choices)



if __name__  == "__main__":
    assert compute_score([1, 1, 1, 1, 1, 1]) == 8000
    assert compute_score([1, 1, 1, 1, 1, 2]) == 4000
    assert compute_score([1, 5]) == 150
    assert compute_score([1, 1, 5]) == 250
    assert compute_score([1, 5, 5]) == 200
    assert compute_score([2,3,4]) == 0
    assert compute_score([4,3,4,2,2,2]) == 200
    assert compute_score([6, 2, 5, 4, 1, 4,]) == 150
    assert compute_score([1, 1, 2, 2, 3, 1]) == 300
    assert compute_score([2,2,5]) == 50 # round over check

    ## 3 pairs test
    assert compute_score([2,2,3,3,4,4]) == 1000
    assert compute_score([1, 1, 3, 3, 4, 4]) == 1000
    assert compute_score([1, 1, 5, 5, 4, 4]) == 1000
    assert compute_score([2, 2, 3, 3, 4, 6]) == 0
    assert compute_score([6,6,3,3,4,4]) == 1000

    # input verification
    assert nr_of_scoring_dices([2, 2, 5]) == 1
    assert nr_of_scoring_dices([1, 1, 5]) == 3
    assert nr_of_scoring_dices([1, 2, 5]) == 2
    assert nr_of_scoring_dices([1, 2, 3, 4, 5, 6]) == 6
    assert nr_of_scoring_dices([5,5,5]) == 3

    assert check_match_with_the_rolled_set([6, 5, 3, 5, 5], [5, 5, 5]) == True
    assert check_match_with_the_rolled_set([6, 5, 3, 5, 5], [5, 2, 5]) == False
    assert check_match_with_the_rolled_set([1, 5, 1, 5, 1], [1, 1, 1, 5, 5]) == True
    assert check_match_with_the_rolled_set([1, 2, 1, 5, 1], [1, 1, 5, 5]) == False
    assert check_match_with_the_rolled_set([5, 1, 5,5, 4, 5], [5,5,5,5,5,5]) == False
    assert check_match_with_the_rolled_set([5, 1, 5, 5, 4, 5], [5, 5, 5, 5, 5, 5, 3]) == False
    assert check_match_with_the_rolled_set([5, 1, 5, 5, 4, 5], [5, 5, 5, 5, 8]) == False
