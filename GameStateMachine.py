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
        self.same_player_round_eval(0)
        print("\n\n")


    def switch_player(self, round_over : bool):
        self.interface.print_game_status()
        self.gameProperties.swap_next_player()
        ##  check if the game is over
        if not self.gameProperties.get_current_player().get_score < self.gameProperties.winning_value:
            self.interface.print_winner()
            return

        self.interface.print_current_player()
        if not round_over:
            print("--Do you want to reset the pot and your number of dices? [y/n]--")
            reset_pot : bool = self.interface.ask_for_y_n()
            if reset_pot:
                self.gameProperties.reset_pot()
                self.gameProperties.reset_dices()
        self.same_player_round_eval(self.gameProperties.pot.get)


    def same_player_round_eval(self, continuous_score):
        if self.gameProperties.get_number_of_dices() == 0:
            self.gameProperties.reset_dices()

        roll_set: list[int] = self.gameProperties.define_set_of_rolls(self.gameProperties.get_number_of_dices())
        self.interface.print_set_of_rolls(roll_set)

        # sorted will give the maximum score
        round_over = compute_score(sorted(roll_set)) == 0
        if round_over:
            print("Round is over")
            self.gameProperties.reset_pot()
            self.gameProperties.reset_dices()
            self.switch_player(True)
        else:

            print("Choose the dices you want to keep:")
            verified_choices = self.interface.ask_for_correct_input(roll_set)
            c_score = compute_score(verified_choices)
            total_score = continuous_score + c_score
            print(f"Current score is {c_score}, total score is {total_score}")

            self.gameProperties.reduce_dices(len(verified_choices))


            dices_are_zero = self.gameProperties.get_number_of_dices() == 0
            if not dices_are_zero:
                self.interface.print_continue_or_stop()

            p_continue = True if dices_are_zero else self.interface.ask_for_y_n()

            if not p_continue:
                self.gameProperties.update_player_score(total_score)
                self.gameProperties.set_pot(total_score)
                self.switch_player(False)
            else:
                self.same_player_round_eval(continuous_score + c_score)


class GameStateMachineDebug(GameStateMachine):
    def __init__(self, players: list[Player], winning_value: int):
        self.gameProperties = GameProperties()
        self.interface = GameInterface(self.gameProperties)
        self.gameProperties.players = players
        self.gameProperties.winning_value = winning_value
        self.start_game()



if __name__ == "__main__":
    #GameStateMachine()
    GameStateMachineDebug([Player("Joy"),Player("Paolo")], 1000)