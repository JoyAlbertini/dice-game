
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

