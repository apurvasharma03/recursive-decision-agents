from pprint import pprint

from ..board import Board, CellState
from .base_agent import Agent, Move, valid_moves
from ..player import Player, PLAYER_NAMES
import sys


class DFSAgent(Agent):
    def __init__(self, player):
        super().__init__(player)
        #super().__init__(Board)
        #self._board = Board(size=3, num_to_win=None)
        #valid = True

    def next_move(self, board):
        def _input_move():
            try:
                """
                print("")
                print("{}'s next move".format(PLAYER_NAMES[self._player]))
                row = int(input("\trow: "))
                col = int(input("\tcol: "))
                print("")

                return Move(self._player, row, col)
                """
                #stack = []
                
                # states whether the move is valid
                valid = True
                
                # initialized as low num so the first returned score replaces its val
                bestScore = -5
                
                #finalMove = Move(self._player, 0, 0)
                #print("recursion limit: " + str(sys.getrecursionlimit()))
                
                # to fix max recursion limit exceeded error 
                # although recursion error probably caused by logic error
                sys.setrecursionlimit(2200)
                
                #print("recursion limit: " + str(sys.getrecursionlimit()))
                
                # iterate through every space in grid
                for i in range(3):
                    for j in range(3):
                        
                        # checks if the move is valid (if spot is already filled)
                        if (Move(self._player, i, j) not in valid_moves(board, self._player)):
                            valid = False
                            print("inside first if")
                            
                            # initialize a val for var
                            finalMove = Move(self._player, 0, 0)
                        
                        # only goes on to eval move if it's valid
                        if (valid):
                            print("inside second if")
                            
                            # move that is being evaluated
                            testMove = Move(self._player, i, j)
                            
                            # call to minimax to get score based on the move
                            score = minimax(testMove, 0, False)
                            print("score: " + str(score))
                            
                            # highest score should be the best score
                            if (score > bestScore):
                                print("score > best score")
                                bestScore = score
                                
                                # the finalMove should be the one with the bestScore
                                finalMove = Move(self._player, i, j)
                            else:
                                finalMove = Move(self._player, 0, 0)
                                
                # gives the move for the agent to play 
                return finalMove
            except ValueError:
                print("Row an col must be integers between 0 and {}".format(
                    board.size))

        # minimax algorithm
        def minimax(testMove, depth, isMax):
            print("inside minimax")
            
            # states whether the move is valid
            valid = True
            # if it is at an end state, return the score
            #if winner(self._player)
            
            # initialize whether a player has won the game get
            win = False
            
            # checks to see if x has won the game
            if (self._player == "x"):
                
                # sets score to good if DFS agent wins the game
                # need to change so it's not hard coded to specific player
                score = 1
                
                # set win to True b/c a player won
                win = True
           
            # checks to see if o has won the game
            elif (self._player == "o"):
                
                # sets score to bad if non-DFS agent wins the game
                # need to change so it's not hard coded to specific player
                score = -1
                
                # set win to True b/c a player won
                win = True
            
            # checks to see if the game has ended
            elif (self._player == "draw"):
                
                # sets score to intermediate score if there is a tie
                score = 0
                
                # set win to True b/c the game is over
                win = True
            
            # if a player has won, the minimax algorithm should end
            if (win):
                print("return score")
                
                # the score should be checked against the bestScore 
                # to determine if the current move should be the play
                return score
            
            # check if the current agent is the maximizing one        
            if (isMax):
                print("inside isMax")
                
                # iterate through every space in grid
                for i in range(3):
                    for j in range(3):
                        print("inside isMax loop")
                        
                        # checks if the move is valid (if spot is already filled)
                        if (Move(self._player, i, j) not in valid_moves(board, self._player)):
                            valid = False
                            
                        # only goes on to eval move if it's valid
                        if (valid):
                            
                            # move that is being evaluated
                            testMove = Move(self._player, i, j)
                            
                            # call to minimax to get score based on the move
                            # depth should increase with every single iteration
                            # should be True instead of False?
                            score = minimax(testMove, depth + 1, False)
                            
                            # highest score should be the best score
                            if (score > bestScore):
                                print("score > bestscore inside minimax")
                                bestScore = score
                                
                                # the finalMove should be the one with the bestScore
                                finalMove = Move(self._player, i, j)
                return bestScore
            
            # to test the possible moves for the minimizing agent   
            else:
                print("inside else")
                
                # iterate through every space in grid
                for i in range(3):
                    for j in range(3):
                        
                        # store the valid moves in a var
                        next_moves = valid_moves(board, self._player)
                        
                        # checks if the move is valid (if spot is already filled)
                        if (Move(self._player, i, j) not in next_moves):
                            valid = False
                            
                        # only goes on to eval move if it's valid
                        if (valid):
                            print("inside valid else")
                            
                             # move that is being evaluated
                            testMove = Move(self._player, i, j)
                            
                            # call to minimax to get score based on the move
                            # depth should increase with every single iteration
                            # should be False instead of True?
                            score = minimax(testMove, depth + 1, True)
                            
                            # highest score should be the best score
                            if (score > bestScore):
                                bestScore = score
                                
                                # the finalMove should be the one with the bestScore
                                finalMove = Move(self._player, i, j)
                return bestScore

        move = _input_move()
        next_moves = valid_moves(board, self._player)

        """
        while move not in next_moves:
            print("{} is not valid, try again.".format(move))
            print("Valid moves: ")
            pprint(next_moves)
            move = _input_move()
        """

        return move
