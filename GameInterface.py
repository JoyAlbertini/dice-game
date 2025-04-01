from DiceSet import DiceSet
from GameProperties import GameProperties
from score_logic import parse_player_choices_input, check_if_valid_choice, compute_score


class GameInterface:

    def __init__(self, game_properties : GameProperties):
       self.gProperties = game_properties

    def print_game_status(self):
        print(f"Current pot value is {self.gProperties.pot.get}. \n" +
                f"Current number of dices is {self.gProperties.get_number_of_dices()}. \n" +
                f"Players scores are: \n" +
                ", ".join(f"Player {player.name} score is {player.score}" for player in self.gProperties.players))

    @staticmethod
    def print_set_of_rolls(rolls):
        print(DiceSet.set_of_dices_to_str(rolls))

    def print_current_player(self):
        print("Current player: ", self.get_current_player_str())

    def print_winner(self):
        print(f"Player {self.gProperties.get_current_player().name} won!")

    def get_current_player_str(self) -> str:
        return self.gProperties.get_current_player().name


    @staticmethod
    def print_continue_or_stop():
        print("Do you want to roll the dices or stop? [y/n]?")

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



















