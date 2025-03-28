import random

import score_logic
from DiceSet import DiceSet
from Player import Player
from Pot import Pot




class Game:
    def __init__(self, players : list[Player], pot : Pot, winning_value : int, nr_dices : int):
        self.current_player_idx = 0
        self.players = players
        self.pot = pot
        self.winning_value = winning_value
        self.diceSet = DiceSet(nr_dices)
        self.current_rolled_set = []

    def choose_first_player(self):
        self.current_player_idx = random.randint(0, len(self.players) - 1)

    def swap_next_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.current_player_idx]

    def start_game(self):
        self.choose_first_player()
        print(" Fist player chosen is ", self.players[self.current_player_idx].name)

    def print_game_status(self):
        print(f"Current pot value is {self.pot.get}. " +
              ", ".join(f"Player {player.name} score is {player.score}" for player in self.players))

    def define_set_of_rolls(self):
        self.current_rolled_set = self.diceSet.get_set_of_rolls(self.diceSet.get_dices())

    def print_set_of_rolls(self):
        print(DiceSet.set_of_dices_to_str(self.current_rolled_set))

    def evaluate_round_over(self):
        return score_logic.compute_score(sorted(self.current_rolled_set)) != 0

    def evaluate_player_choice_score(self, player_choice) -> int:
        return score_logic.compute_player_score(player_choice, self.current_rolled_set)

    def update_player_score(self, score):
        self.get_current_player().increase_score(score)

    def update_pot(self, score):
        self.pot.add(score)

    def reset_pot(self):
        self.pot.reset()




