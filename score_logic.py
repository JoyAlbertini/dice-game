from collections import Counter
from typing import Tuple


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

def compute_score_and_count(verified_choice: list[int]) -> Tuple[int, int]:
    if len(verified_choice) == 6:
        counts = Counter(verified_choice)
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            return 1000, 6

    match verified_choice:
        case [1, 2, 3, 4, 5, 6]:
            return 1000, 6

    match verified_choice:
        case [1, 1, 1, 1, 1, 1]:
            return 8000, 6
        case [1, 1, 1, 1, 1, *rest]:
            score, count = compute_score_and_count(rest)
            return 4000 + score, 5 + count
        case [1, 1, 1, 1, *rest]:
            score, count = compute_score_and_count(rest)
            return 2000 + score, 4 + count
        case [1, 1, 1, *rest]:
            score, count = compute_score_and_count(rest)
            return 1000 + score, 3 + count
        case [1, *rest]:
            score, count = compute_score_and_count(rest)
            return 100 + score, 1 + count

    match verified_choice:
        case [2, 2, 2, 2, 2, 2]:
            return 1600, 6
        case [2, 2, 2, 2, 2, *rest]:
            score, count = compute_score_and_count(rest)
            return 800 + score, 5 + count
        case [2, 2, 2, 2, *rest]:
            score, count = compute_score_and_count(rest)
            return 400 + score, 4 + count
        case [2, 2, 2, *rest]:
            score, count = compute_score_and_count(rest)
            return 200 + score, 3 + count

    match verified_choice:
        case [3, 3, 3, 3, 3, 3]:
            return 2400, 6
        case [3, 3, 3, 3, 3, *rest]:
            score, count = compute_score_and_count(rest)
            return 1200 + score, 5 + count
        case [3, 3, 3, 3, *rest]:
            score, count = compute_score_and_count(rest)
            return 600 + score, 4 + count
        case [3, 3, 3, *rest]:
            score, count = compute_score_and_count(rest)
            return 300 + score, 3 + count

    match verified_choice:
        case [4, 4, 4, 4, 4, 4]:
            return 3200, 6
        case [4, 4, 4, 4, 4, *rest]:
            score, count = compute_score_and_count(rest)
            return 1600 + score, 5 + count
        case [4, 4, 4, 4, *rest]:
            score, count = compute_score_and_count(rest)
            return 800 + score, 4 + count
        case [4, 4, 4, *rest]:
            score, count = compute_score_and_count(rest)
            return 400 + score, 3 + count

    match verified_choice:
        case [5, 5, 5, 5, 5, 5]:
            return 4000, 6
        case [5, 5, 5, 5, 5, *rest]:
            score, count = compute_score_and_count(rest)
            return 2000 + score, 5 + count
        case [5, 5, 5, 5, *rest]:
            score, count = compute_score_and_count(rest)
            return 1000 + score, 4 + count
        case [5, 5, 5, *rest]:
            score, count = compute_score_and_count(rest)
            return 500 + score, 3 + count
        case [5, *rest]:
            score, count = compute_score_and_count(rest)
            return 50 + score, 1 + count

    match verified_choice:
        case [6, 6, 6, 6, 6, 6]:
            return 4800, 6
        case [6, 6, 6, 6, 6, *rest]:
            score, count = compute_score_and_count(rest)
            return 2400 + score, 5 + count
        case [6, 6, 6, 6, *rest]:
            score, count = compute_score_and_count(rest)
            return 1200 + score, 4 + count
        case [6, 6, 6, *rest]:
            score, count = compute_score_and_count(rest)
            return 600 + score, 3 + count

    if verified_choice:
        return compute_score_and_count(verified_choice[1:])
    else:
        return (0, 0)

def compute_score(verified_choice: list[int]) -> int:
    return compute_score_and_count(verified_choice)[0]

def nr_of_scoring_dices(choices: list[int]) -> int:
    return compute_score_and_count(choices)[1]

def match_the_number_of_scoring_dices(choices: list[int]) -> bool:
    return len(choices) == compute_score_and_count(choices)[1]



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
