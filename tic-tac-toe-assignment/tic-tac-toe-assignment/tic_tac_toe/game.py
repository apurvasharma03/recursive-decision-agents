from copy import deepcopy

from .board import Board, CellState
from .player import Player, PLAYER_NAMES
import time




class Game(object):
    def __init__(self, player_x, player_o, Xwins, Owins, draws, X_time, X_turns, O_time, O_turns, size=3, num_to_win=None,
                 starting_board=None):
        self._player_x = player_x
        self._player_o = player_o

        self._current_player = (Player.X, self._player_x)
        self._next_player = (Player.O, self._player_o)
        
        self.Xwins =  Xwins
        self.Owins =  Owins
        self.draws =  draws
        
        self.X_time = X_time
        self.X_turns = X_turns
        self.O_time = O_time
        self.O_turns = O_turns
        

        if starting_board is None:
            self._board = Board(size=size, num_to_win=num_to_win)
        else:
            self._board = starting_board

        self._num_rounds = self._board.size ** 2 - len(self._board.empty_cells)
   
    def play(self):
        #X_time = 0
        #X_turns = 0
        #O_time = 0
        #O_turns = 0
        while (self._board.winner is None
               and self._num_rounds < self._board.size ** 2):
            self._show_board()
            start_agent = time.time()
            self._make_next_move()
            if (self._current_player == (Player.X, self._player_x)):
                self.X_time = self.X_time + time.time() - start_agent
                self.X_turns = self.X_turns + 1
            else:
                self.O_time = self.O_time + time.time() - start_agent
                self.O_turns = self.O_turns + 1
            self._current_player, self._next_player = \
                self._next_player, self._current_player
            self._num_rounds = self._num_rounds + 1
        #print("X_time " + str(X_time))
        #print("X_turns " + str(X_turns))
        self._show_board()
        if self._board.winner is None:
            print("It's a draw!")
            self.draws = self.draws + 1
        else:
            print("Congratulations, {} won!".format(
                PLAYER_NAMES[self._board.winner]))
        #print(PLAYER_NAMES[self._board.winner])
            if (PLAYER_NAMES[self._board.winner] == "x"):
                self.Xwins = self.Xwins + 1
            else:
                self.Owins = self.Owins + 1
        
        #print("X turns: " + str(X_turns))
        #print("O turns: " + str(O_turns))
        #print("Wins by X: " + str(self.Xwins))
        #print("Wins by O: " + str(self.Owins))
        #print("Draws: " + str(self.draws))

    def _show_board(self):
        print(self._board)
        print("")

    def _make_next_move(self):
        move = self._current_player[1].next_move(deepcopy(self._board))

        assert move.player == self._current_player[0]
        assert self._board.cell(move.row, move.col) == CellState.EMPTY

        self._board.set_cell(move.player, move.row, move.col)
