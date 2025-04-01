from DiceSet import DiceSet
from GameProperties import GameProperties
from Player import Player
from score_logic import parse_player_choices_input, check_if_valid_choice, compute_score


class GameInterface:

    def __init__(self, game_properties : GameProperties):
       self.gProperties = game_properties

    def print_game_status(self):
        print(f"Current pot value is {self.gProperties.pot.get}. \n" +
                f"Current number of dices is {self.gProperties.get_number_of_dices()}. \n" +
                f"Players scores are: \n" +
                ", ".join(f"Player {player.get_name} score is {player.get_score}" for player in self.gProperties.players))

    @staticmethod
    def print_set_of_rolls(rolls):
        print(DiceSet.set_of_dices_to_str(rolls))

    def print_current_player(self):
        print("Current player: ", self.get_current_player_str())

    def print_winner(self):
        print(f"Player {self.gProperties.get_current_player().get_name} won!")

    def get_current_player_str(self) -> str:
        return self.gProperties.get_current_player().get_name


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

    @staticmethod
    def ask_for_winning_value():
        while True:
            try:
                print("Please enter the winning value: ")
                value = int(input().strip())
                if value == 0:
                    print("Error: Winning value cannot be zero.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    @staticmethod
    def ask_for_players() -> list[Player]:
        players = []
        while True:
            print("Please enter the name of the player: ")
            name = input().strip()
            players.append(Player(name))
            if len(players) != 1:
                print("Do you want to add another player? [y/n]")
                if GameInterface.ask_for_y_n() == "n":
                    break
        return players












