import random

class DiceSet:

    NR_OF_DICES = 6

    def __init__(self):
        self.__dices = DiceSet.NR_OF_DICES

    def get_dices(self) -> int:
        return self.__dices

    def reduce_dices(self, amount : int):
        self.__dices = max(0, self.__dices - amount)

    def reset_dices(self):
        self.__dices = DiceSet.NR_OF_DICES

    def are_dices_available(self) -> bool:
        return self.__dices > 0

    # functional style
    @staticmethod
    def get_dice_roll() -> int:
        return random.randint(1, 6)

    @staticmethod
    def get_set_of_rolls(nr_dices) -> list[int]:
        return [DiceSet.get_dice_roll() for _ in range(nr_dices)]

    @staticmethod
    def set_of_dices_to_str(set_of_dices: list[int]) -> str:
        return " ".join(str(x) for x in set_of_dices)





