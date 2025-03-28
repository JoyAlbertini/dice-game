class Pot:
    def __init__(self):
        self.__value = 0

    def add(self, amount):
        self.__value += amount

    @property
    def get(self):
        return self.__value

    def reset(self):
        self.__value = 0