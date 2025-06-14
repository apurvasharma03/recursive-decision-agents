import random

from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES


class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
         def _input_move():
            try:
                print("")
                print("{}'s next move".format(PLAYER_NAMES[self._player]))
                list1 = [0, 1, 2]
                row = random.choice(list1)
                col = random.choice(list1)
                print("")

                return Move(self._player, row, col)
            except ValueError:
                print("Row an col must be integers between 0 and {}".format(
                    board.size))

         move = _input_move()
         next_moves = valid_moves(board, self._player)

         while move not in next_moves:
            print("{} is not valid, try again.".format(move))
            print("Valid moves: ")
            print(next_moves)
            move = _input_move()

         return move
