from DiceSet import DiceSet
from GameValues import GameValues
from Player import Player
from score_logic import parse_player_choices_input, \
    match_the_number_of_scoring_dices, check_match_with_the_rolled_set


class GameInterface:

    def __init__(self, game_properties : GameValues):
       self.__gValues = game_properties

    def print_game_status(self):
        print(f"\n----------------------------------------------------------\n" +
              f"Current pot value is {self.__gValues.get_pot()}. \n" +
                f"Current number of dices is {self.__gValues.get_number_of_dices()}. \n" +
                f"Players scores are: " + (", ".join(f"player {player.get_name} : {player.get_score}" for player in self.__gValues.players)) + "\n"
              + f"-----------------------------------------------------------\n")


    @staticmethod
    def print_set_of_rolls(rolls):
        print(DiceSet.set_of_dices_to_str(rolls))

    def print_current_player(self):
        print("Current player: ", self.get_current_player_str())

    def print_winner(self):
        print(f"Player {self.__gValues.get_current_player().get_name} won!")

    def get_current_player_str(self) -> str:
        return self.__gValues.get_current_player().get_name

    @staticmethod
    def print_reset_pot_and_dices():
        print("--Do you want to reset the pot and your number of dices? [y/n]--")

    @staticmethod
    def print_continue_or_stop():
        print("--Do you want to roll the dices? [y/n]?--")

    @staticmethod
    def print_round_over():
        print("--Round is over--")

    @staticmethod
    def print_choose_the_dices():
        print("--Choose the dices you want to keep:--")

    @staticmethod
    def print_round_scores(c_score :int, total_score : int):
        print(f"Current score is {c_score}, total score is {total_score}")
    ## Sub routines

    @staticmethod
    def ask_for_correct_input(rolled_set : list[int]) -> list[int]:
        while True:
            choice = input().strip()
            choices : list[int] = parse_player_choices_input(choice)
            #print("parsed choices: ", choices)
            if (choices is not None and len(choices) > 0
                    and check_match_with_the_rolled_set(rolled_set, choices)
                    and match_the_number_of_scoring_dices(choices)
            ):
                return choices
            else:
                print("Invalid input. Please try again")


    @staticmethod
    def ask_for_y_n() -> bool:
        p_continue = input().strip()
        if p_continue != "n" and p_continue != "y":
            print("--Invalid input. Please try again [y/n]:--")
            return GameInterface.ask_for_y_n()
        return True if p_continue == "y" else False

    @staticmethod
    def ask_for_value(value_name : str) -> int:
        while True:
            try:
                print(f"--Please enter the {value_name}: --")
                value = int(input().strip())
                if value == 0:
                    print(f"--Error: {value_name} cannot be zero--")
                else:
                    return value
            except ValueError:
                print("--Invalid input. Please enter a valid integer--")

    @staticmethod
    def ask_for_players() -> list[Player]:
        players = []
        player_names = set()
        while True:
            print("--Please enter the name of the player: --")
            name = input().strip()
            if name in player_names:
                print("--Error: Player name already exists. Please enter a different name.--")
                continue
            players.append(Player(name))
            player_names.add(name)
            if len(players) != 1:
                print("--Do you want to add another player? [y/n]--")
                if not GameInterface.ask_for_y_n():
                    break
        return players










