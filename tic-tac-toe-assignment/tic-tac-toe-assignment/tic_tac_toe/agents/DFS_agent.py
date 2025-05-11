from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES
import copy

NODE_COUNTER = 0
node_totalX = 0
node_totalO = 0

def increment():
    global NODE_COUNTER
    
    # count nodes
    NODE_COUNTER = NODE_COUNTER + 1

def totalNodeX():
    global node_totalX
    node_totalX = node_totalX + NODE_COUNTER

def totalNodeO():
    global node_totalO
    node_totalO = node_totalO + NODE_COUNTER

def get_win_score(move, board, x_player, x_move):
    if x_move:
        board.set_cell(0, move[0], move[1])
    else:
        board.set_cell(1, move[0], move[1])

    if (board.winner != None or not board.empty_cells):
        # 0 = false
        if (board.winner == 0 and x_player) or (board.winner == 1 and not x_player):
            return 2
        elif not board.empty_cells:
            return 1
        else:
            return 0

    moves_to_test = copy.deepcopy(board.empty_cells)
    loop_arr = []
    for move in moves_to_test:
        increment()
        x = get_win_score(move, copy.deepcopy(board), x_player, not x_move)
        loop_arr.append(x)
    if (x_player and x_move or not x_player and not x_move):
        minmax_val = min(loop_arr)
    else:
        minmax_val = max(loop_arr)
    return minmax_val

class dfsAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        def _find_move():
            
        
            moves_to_test = copy.deepcopy(board.empty_cells)
            max_score = 0
            best_move = moves_to_test[0]
            x_move = False
            x_player = False
            if PLAYER_NAMES[self._player] == 'x':
                x_move = True
                x_player = True
            for move in moves_to_test:
                board_copy = copy.deepcopy(board)
                x = get_win_score(move, board_copy, x_player, x_move)
                print("move:", move, "///score", x)
                if x > max_score:
                    max_score = x
                    best_move = move
            return best_move
        move = _find_move()

        print("{}'s next move is:".format(PLAYER_NAMES[self._player]))
        print("{}".format(move))
        print("NODES SEARCHED:", NODE_COUNTER)
        if (PLAYER_NAMES[self._player] == 'x'):
            totalNodeX()
        else:
            totalNodeO()
        if (node_totalX != 0):
            print("X's nodes searched: " + str(node_totalX))
        if (node_totalO != 0):
            print("O's nodes searched: " + str(node_totalO))

        return Move(self._player, move[0], move[1])