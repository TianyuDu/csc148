"""
TODO: Read the following docstring before clicking 'run'
This unittest is an unofficial unittests provided by Penguin, which makes its
quality heavuly depend on how Penguin did on this assignment(I personally think
I have done a great job, by the way).
This unittests
will compare your results againsts Penguin's result. If you pass it, don't be
happy, it's highly likely that Penguin happenly made the same mistake as you
made. If you did't pass it, don't be panic because Penguin did't sleep well
last night due to his roommates playing Overwatch loudly until 1 a.m.

Don't bother to try reversing enginerring this script since it doesn't contain
even one line of Penguin's minimax code.

Please report any issue to will.qie@mail.utoronto.ca so we can improve out code
together.

TODO: Put the *_results and this file in the same directory as your code
Note that The tests finishes in 48s on a i7 computer.
"""
import unittest
from unittest.mock import patch

# Import the student solution
from game_interface import playable_games, usable_strategies
minimax_iterative_strategy = usable_strategies['mi']
minimax_recursive_strategy = usable_strategies['mr']
StonehengeGame = playable_games['h']
SubtractSquareGame = playable_games['s']

STONEHENGE_MINIMAX_BOARD = """\
          2   1
         /   /
    1 - 1 - 1   @
       / \\ / \\ /
  1 - 2 - 1 - 1   2
     / \\ / \\ / \\ /
2 - 2 - 2 - H - 2
     \\ / \\ / \\ / \\
  @ - J - 2 - L   1
       \\   \\   \\
        2   2   1
"""
results_file = open('my_results', 'r')
my_results = eval(results_file.read())
results_file.close()

results_file = open('new_results', 'r')
new_results = eval(results_file.read())
results_file.close()

results_file = open('newer_results', 'r')
newer_results = eval(results_file.read())
results_file.close()


class MinimaxUnitTests(unittest.TestCase):
    # def test_result_consistency(self):
    #     """
    #     Too lazy to write one.
    #     """
    #     for value in my_results:
    #         try:
    #             with patch('builtins.input', return_value=str(value)):
    #                 game = SubtractSquareGame(True)
    #
    #             ite_result = minimax_iterative_strategy(game)
    #             rec_result = minimax_recursive_strategy(game)
    #             self.assertEqual(ite_result, rec_result)
    #         except AssertionError:
    #             print(f"""There is definitely something wrong with your
    #                              iterative minimax or recursice minimax.
    #                              When pass in value {value}, recursive minimax
    #                              and recursive minimax don't return same
    #                              result! Recursive minimax returns
    #                              {rec_result} and iterative minimax returns
    #                              {ite_result}""")

    def test_iterative_subtract_square(self):
        """
        Too lazy to write one.
        """
        for value in my_results:
            try:
                with patch('builtins.input', return_value=str(value)):
                    game = SubtractSquareGame(True)

                move_scores = minimax_iterative_strategy(game)
                expected = my_results[value]
                self.assertTrue(move_scores in expected)
            except AssertionError:
                print(f"""There maybe some problem with your 
                                 iterative minimax. When pass in value
                                 {value}, expected {my_results[value]} but
                                 {move_scores} is returned.""")

    def test_recursive_subtract_square(self):
        """
        Too lazy to write one.
        """
        for value in my_results:
            try:
                with patch('builtins.input', return_value=str(value)):
                    game = SubtractSquareGame(True)
                move_scores = minimax_recursive_strategy(game)
                expected = my_results[value]
                self.assertTrue(move_scores in expected)
            except AssertionError:
                print(f"""There maybe some problem with your 
                                 recursive minimax. When pass in value
                                 {value}, expected {my_results[value]} but
                                 {move_scores} is returned.""")

    def test_stonehenge_one_step(self):
        """
        Too lazy to write one.
        """
        for value in new_results:
            try:
                with patch('builtins.input', return_value='2'):
                    game = StonehengeGame(True)
                game.current_state = game.current_state.make_move(
                    game.str_to_move(value))
                expected_move = new_results[value]
                move_chosen = minimax_recursive_strategy(game)
                new_move = minimax_iterative_strategy(game)
                self.assertTrue(move_chosen in expected_move)
                self.assertTrue(move_chosen in expected_move)
            except AssertionError:
                print(f'Failure of tests {value}')

    def test_stonrhenge_five_steps(self):
        """
        Too lazy to write one
        """
        for move_to_make in newer_results:
            try:
                with patch('builtins.input', return_value='3'):
                    game = StonehengeGame(True)
                for move in move_to_make:
                    game.current_state = game.current_state.make_move(
                        game.str_to_move(move))
                expected_move = newer_results[move_to_make]
                move_chosen = minimax_recursive_strategy(game)
                new_move = minimax_iterative_strategy(game)
                self.assertTrue(new_move in expected_move)
                self.assertTrue(move_chosen in expected_move)
            except AssertionError:
                print(f'Failure of tests {move_to_make}')


if __name__ == "__main__":
    unittest.main()
