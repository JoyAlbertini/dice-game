
class Player:
    def __init__(self, name: str):
        self.__name = name
        self.__score = 0

    def increase_score(self, amount: int):
        self.__score += amount

    @property
    def get_score(self) -> int:
        return self.__score

    @property
    def get_name(self):
        return self.__name




class PlayerDebug(Player):

    def __init__(self, name: str, score: int):
        super().__init__(name)
        self.__settable_score = score

    def increase_score(self, amount: int):
        self.__settable_score += amount

    @property
    def get_score(self) -> int:
        return self.__settable_score


