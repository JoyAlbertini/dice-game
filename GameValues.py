import random
from DiceSet import DiceSet
from Player import PlayerDebug
from Pot import Pot


class GameValues:
    def __init__(self):
        self.winning_value = None
        self.__current_player_idx = 0
        self.__pot = Pot()
        self.__diceSet = DiceSet()
        self.players = None
        self.board_size = 0

    ## player

    def choose_first_player(self):
        self.__current_player_idx = random.randint(0, len(self.players) - 1)

    def swap_next_player(self):
        self.__current_player_idx = (self.__current_player_idx + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.__current_player_idx]

    def is_player_on_the_board(self):
        return self.get_current_player().get_score >= self.board_size

    def get_player_with_max_score(self):
        if self.players is None:
            return None
        return max(self.players, key=lambda x: x.get_score)

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


if __name__ == "__main__":
    g = GameValues()
    g.players = [PlayerDebug("a", 10000), PlayerDebug("b", 12000)]
    assert g.get_player_with_max_score().get_name == "b"
