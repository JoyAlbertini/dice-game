from GameInterface import GameInterface
from GameProperties import GameProperties
from Player import Player
from score_logic import compute_score


class GameStateMachine:

    def __init__(self):
        self.gameProperties = GameProperties()
        self.interface = GameInterface(self.gameProperties)
        self.gameProperties.winning_value = self.interface.ask_for_winning_value()
        self.gameProperties.players = self.interface.ask_for_players()
        self.start_game()



    def start_game(self):
        self.gameProperties.choose_first_player()
        self.interface.print_current_player()
        self.same_player_round_eval()


    def switch_player(self, round_over : bool):
        self.interface.print_game_status()
        self.gameProperties.swap_next_player()
        ##  check if the game is over
        if not self.gameProperties.get_current_player().get_score < self.gameProperties.winning_value:
            self.interface.print_winner()
            return

        self.interface.print_current_player()
        if not round_over:
            print("Do you want to reset the pot and your number of dices? [y/n]")
            reset_pot = self.interface.ask_for_y_n()
            if reset_pot == "y":
                self.gameProperties.reset_pot()
                self.gameProperties.reset_dices()
        self.same_player_round_eval()


    def same_player_round_eval(self):
        if self.gameProperties.get_number_of_dices() == 0:
            self.gameProperties.reset_dices()

        roll_set: list[int] = self.gameProperties.define_set_of_rolls(self.gameProperties.get_number_of_dices())
        self.interface.print_set_of_rolls(roll_set)

        round_over = compute_score(sorted(roll_set)) == 0
        if round_over:
            print("Round is over")
            self.gameProperties.reset_pot()
            self.gameProperties.reset_dices()
            self.switch_player(True)
        else:
            print("Choose the dices you want to keep:")
            verified_choices = self.interface.ask_for_correct_input(roll_set)
            score = compute_score(verified_choices)
            print(f"Score is {score}")
            self.interface.print_continue_or_stop()

            p_continue = self.interface.ask_for_y_n()

            self.gameProperties.reduce_dices(len(verified_choices))
            if p_continue == "n":
                self.gameProperties.update_player_score(score)
                self.gameProperties.update_pot(score)
                self.switch_player(False)
            else:
                self.same_player_round_eval()

if __name__ == "__main__":
    GameStateMachine()