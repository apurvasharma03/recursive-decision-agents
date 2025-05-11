from .base_agent import Agent, Move, valid_moves
from ..player import PLAYER_NAMES
import copy

# initialize values
NODE_COUNTER = 0
node_totalX = 0
node_totalO = 0
alpha = -1000
beta = 1000


# count the total nodes searched for the x agent
def totalNodeX():
    global node_totalX
    node_totalX = node_totalX + NODE_COUNTER

# count the total nodes searched for the o agent
def totalNodeO():
    global node_totalO
    node_totalO = node_totalO + NODE_COUNTER

# count the number of nodes searched for that move
def increment():
    global NODE_COUNTER
    
    
    # count nodes
    NODE_COUNTER = NODE_COUNTER + 1
    

def get_win_score(move, board, x_player, x_move, alpha, beta):
    #print("alpha inside " + str(alpha))
    #print("beta inside " + str(beta))
    if x_move:
        board.set_cell(0, move[0], move[1])
    else:
        board.set_cell(1, move[0], move[1])

    # if there is no winner or the board isn't empty
    if (board.winner != None or not board.empty_cells):
        # if the player has won
        if (board.winner == 0 and x_player) or (board.winner == 1 and not x_player):
            return 2
        
        # if the player has not won, but there are moves on the board
        elif not board.empty_cells:
            return 1
        else:
            return 0

    # empty copy
    moves_to_test = copy.deepcopy(board.empty_cells)
    loop_arr = []
    stop = False
    for move in moves_to_test:
        if (beta <= alpha):
            stop = True
        if (stop):
            break
        increment()
        
        # get score
        x = get_win_score(move, copy.deepcopy(board), x_player, not x_move, alpha, beta)
        loop_arr.append(x)
    
    # if x is the AB agent and testing it's turn or the exact opposite
    if (x_player and x_move or not x_player and not x_move):
        minmax_val = min(loop_arr)
        if (minmax_val < beta):
            
            # here because beta is the best value of the minimizer
            beta = minmax_val
            #print("beta inside " + str(beta))
            if (beta <= alpha):
                   stop = True
                
            
    else:
        minmax_val = max(loop_arr)
        if (minmax_val > alpha):
           
            # here because alpha is the best value of the maximizer
            alpha = minmax_val
            if (beta <= alpha):
                    stop = True
    #def getA():
        #return alpha
    #def getB():
        #return beta
    return minmax_val

class ABagent(Agent):

    def __init__(self, player, node_totalX):
        super().__init__(player)
        self.node_totalX = node_totalX 

    def next_move(self, board):
        def _find_move():
            
            
        
            moves_to_test = copy.deepcopy(board.empty_cells)
            max_score = 0
            best_move = moves_to_test[0]
            x_move = False
            x_player = False
            
            # check which agent's turn it currently is
            if PLAYER_NAMES[self._player] == 'x':
                x_move = True
                x_player = True
            for move in moves_to_test:
                board_copy = copy.deepcopy(board)
                
                x = get_win_score(move, board_copy, x_player, x_move, alpha, beta)
               
                
                # if the lowest min is less than the highest max, end recursion
                if (beta <= alpha):
                    break
                
                print("move:", move, "///score", x)
                
                # finds the highest score to find the best move
                if x > max_score:
                    max_score = x
                    best_move = move
            return best_move
        move = _find_move()

        print("{}'s next move is:".format(PLAYER_NAMES[self._player]))
        print("{}".format(move))
        print("NODES SEARCHED:", NODE_COUNTER)
        
        # count nodes searched for each agent
        if (PLAYER_NAMES[self._player] == 'x'):
            totalNodeX()
        else:
            totalNodeO()
            
        # value will be 0 if it is currently the other agent's turn
        if (node_totalX != 0):
            print("X's nodes searched: " + str(node_totalX))
        if (node_totalO != 0):
            print("O's nodes searched: " + str(node_totalO))

        return Move(self._player, move[0], move[1])
