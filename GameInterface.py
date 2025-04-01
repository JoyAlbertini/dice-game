from DiceSet import DiceSet
from GameProperties import GameProperties
from Player import Player
from Pot import Pot
from score_logic import parse_player_choices_input, check_if_valid_choice, compute_score


class GameInterface:

    def __init__(self, players : list[Player], pot : Pot, winning_value : int, nr_dices : int):
       self.__start_game_flag = False
       self.gameProperies = GameProperties(players, pot, winning_value, nr_dices)

    def start_game(self):
        self.__start_game_flag = True
        self.gameProperies.choose_first_player()
        print("Fist player chosen is ", self.gameProperies.get_current_player().name)

    def print_game_status(self):
        print(f"Current pot value is {self.gameProperies.pot.get}. " +
              ", ".join(f"Player {self.gameProperies.players.name} score is {player.score}" for player in self.players))

    @staticmethod
    def print_set_of_rolls(rolls):
        print(DiceSet.set_of_dices_to_str(rolls))

    def print_current_player(self):
        print("Current player: ", self.get_current_player_str())

    def get_current_player_str(self) -> str:
        return self.gameProperies.get_current_player().name

    def print_player_choice_score(self, player_choice):
        print(self.gameProperies.evaluate_player_choice_score(player_choice))

    @staticmethod
    def print_continue_or_stop():
        print("Do you want to roll the dices or stop? [y/n]?")




    def play_round(self):
        if not self.__start_game_flag:
            self.start_game()
        else:
            self.gameProperies.swap_next_player()
            self.print_current_player()


    @staticmethod
    def ask_for_correct_input(rolled_set : list[int]) -> list[int]:
        while True:
            choice = input()
            choices : list[int] = parse_player_choices_input(choice)
            if (choices is not None and len(choices) > 0
                    and check_if_valid_choice(rolled_set, choices)
                    and compute_score(choices) != 0):
                return choices
            else:
                print("Invalid input. Please try again")

    @staticmethod
    def ask_for_y_n():
        p_continue = input().strip()
        if p_continue != "n" and p_continue != "y":
            print("Invalid input. Please try again [y/n]:")
            return GameInterface.ask_for_y_n()
        return p_continue

    def switch_player(self):
        self.print_game_status()
        self.gameProperies.swap_next_player()
        self.print_current_player()
        self.same_player_round_eval()

    def same_player_round_eval(self):

        if not self.gameProperies.get_current_player().score < self.gameProperies.winning_value:
            print(f"Player {self.gameProperies.get_current_player().name} won!")
            self.__start_game_flag = False
            return

        if self.gameProperies.get_number_of_dices() == 0:
            self.gameProperies.reset_dices()

        roll_set: list[int] = self.gameProperies.define_set_of_rolls(self.gameProperies.get_number_of_dices())
        self.print_set_of_rolls(roll_set)

        round_over = self.gameProperies.evaluate_round_over(roll_set)
        if round_over:
            print("Round is over")
            self.gameProperies.reset_pot()
            self.gameProperies.reset_dices()
            self.switch_player()
        else:
            verified_choices = self.ask_for_correct_input(roll_set)
            score = compute_score(verified_choices)
            print(f"Score is {score}")
            self.print_continue_or_stop()

            p_continue = self.ask_for_y_n()
            if p_continue == "n":
                self.gameProperies.update_player_score(score)
                self.gameProperies.update_pot(score)
                self.dice_set.reduce_dices(len(verified_choices))















