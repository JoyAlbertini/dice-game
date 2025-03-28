
class Player:
    def __init__(self, name: str, score: int):
        self.__name = name
        self.score = score

    def increase_score(self, amount: int):
        self.score += amount

    @property
    def name(self):
        return self.name

