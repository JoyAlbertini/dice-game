from GameInterface import GameInterface
from GameValues import GameValues
from Player import Player, PlayerDebug
from score_logic import compute_score


class GameStateMachine:

    def __init__(self):
        self._gameProperties = GameValues()
        self._interface = GameInterface(self._gameProperties)
        self._gameProperties.winning_value = self._interface.ask_for_value("winning value")
        self._gameProperties.board_size = self._interface.ask_for_value("board size", self._gameProperties.winning_value)
        self._gameProperties.players = self._interface.ask_for_players()
        self.start_game()


    def start_game(self):
        self._gameProperties.choose_first_player()
        self._interface.print_current_player()
        self.same_player_round_eval(0)
        print("\n\n")


    def switch_player(self, round_over : bool):
        self._interface.print_game_status()
        self._gameProperties.swap_next_player()
        ##  check if the game is over
        if not self._gameProperties.get_current_player().get_score < self._gameProperties.winning_value:
            self._interface.print_winner()
            return

        self._interface.print_current_player()
        if not round_over:
            self._interface.print_reset_pot_and_dices()
            reset_pot : bool = self._interface.ask_for_y_n()
            if reset_pot:
                self._gameProperties.reset_pot()
                self._gameProperties.reset_dices()
        self.same_player_round_eval(self._gameProperties.get_pot())


    def same_player_round_eval(self, continuous_score):

        def evaluate_round_over() -> bool:
            return compute_score(sorted(roll_set)) == 0

        def is_player_on_the_board(current_score : int):
            return self._gameProperties.is_player_on_the_board() or current_score >= self._gameProperties.board_size

        def print_reach_boarding_score(current_score : int):
            if current_score >= self._gameProperties.board_size and not self._gameProperties.is_player_on_the_board():
                self._interface.print_reach_boarding_score()

        if self._gameProperties.are_no_dices_left():
            self._gameProperties.reset_dices()

        roll_set: list[int] = self._gameProperties.define_set_of_rolls(self._gameProperties.get_number_of_dices())
        self._interface.print_set_of_rolls(roll_set)

        # sorted will give the maximum score

        if evaluate_round_over():
            self._interface.print_round_over()
            self._gameProperties.reset_pot()
            self._gameProperties.reset_dices()
            self.switch_player(True)
        else:

            self._interface.print_choose_the_dices()
            verified_choices = self._interface.ask_for_correct_input(roll_set)
            c_score = compute_score(verified_choices)
            total_score = continuous_score + c_score
            print_reach_boarding_score(total_score)
            self._interface.print_round_scores(c_score, total_score)

            self._gameProperties.reduce_dices(len(verified_choices))


            dices_are_zero = self._gameProperties.are_no_dices_left()
            if not dices_are_zero and is_player_on_the_board(total_score):
                self._interface.print_continue_or_stop()

            p_continue = True if dices_are_zero or not is_player_on_the_board(total_score) \
                else self._interface.ask_for_y_n()

            if not p_continue:
                self._gameProperties.update_player_score(total_score)
                self._gameProperties.set_pot(total_score)
                self.switch_player(False)
            else:
                self.same_player_round_eval(continuous_score + c_score)


class GameStateMachineDebug(GameStateMachine):
    def __init__(self, players: list[Player], winning_value: int):
        self._gameProperties = GameValues()
        self._interface = GameInterface(self._gameProperties)
        self._gameProperties.players = players
        self._gameProperties.winning_value = winning_value
        self._gameProperties.board_size = 800
        self.start_game()






def test1():
    GameStateMachineDebug([Player("Joy"), Player("Paolo")], 1000)

def test2():
    GameStateMachineDebug([PlayerDebug("Joy", 10000), Player("Paolo")], 10000)

def test3():
    GameStateMachineDebug([PlayerDebug("Joy", 3000), Player("Paolo"), PlayerDebug("Marzio", 4000)], 10000)

if __name__ == "__main__":
    GameStateMachine()
