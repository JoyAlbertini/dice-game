import random
from DiceSet import DiceSet
from Pot import Pot


class GameValues:
    def __init__(self):
        self.winning_value = None
        self.__current_player_idx = 0
        self.__pot = Pot()
        self.__diceSet = DiceSet()
        self.players = None

    ## player

    def choose_first_player(self):
        self.__current_player_idx = random.randint(0, len(self.players) - 1)

    def swap_next_player(self):
        self.__current_player_idx = (self.__current_player_idx + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.__current_player_idx]

    ## dice set

    def define_set_of_rolls(self, nr_dices : int) -> list[int]:
        return self.__diceSet.get_set_of_rolls(nr_dices)

    def get_number_of_dices(self):
        return self.__diceSet.get_dices()

    def reset_dices(self):
        self.__diceSet.reset_dices()

    def reduce_dices(self, amount : int):
        self.__diceSet.reduce_dices(amount)

    def are_no_dices_left(self) -> bool:
        return self.__diceSet.get_dices() == 0

    ## player

    def update_player_score(self, score):
        self.get_current_player().increase_score(score)

    ## pot

    def set_pot(self, score):
        self.__pot.set_pot(score)

    def reset_pot(self):
        self.__pot.reset()

    def get_pot(self):
        return self.__pot.get


