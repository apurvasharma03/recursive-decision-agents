from tic_tac_toe.game import Player, Game
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent
from tic_tac_toe.agents.DFS_agent import dfsAgent
from tic_tac_toe.agents.AB_agent import ABagent, node_totalX
import time

AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Random Agent", RandomAgent),
    ("DFS Agent", dfsAgent),
    ("AB Agent", ABagent)
]




def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = "\n".join(
                map(lambda x: "\t{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: \n{}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent
        except ValueError:
            return None
    #start_agent = time.time()
    agent = _try_pick()
    #print(time.time() - start_agent)

    node_totalX = 0
    node_totalO = 0
    
    while agent is None:
        print("Incorrect selection, try again.")
        agent = _try_pick()

    if (agent == 3):
        return AGENTS[agent][1](player, node_totalX)
    else:
       return AGENTS[agent][1](player) 


def main():
    num_games = 0
    total_time = 0
    total_O = 0
    total_X = 0
    total_draws = 0
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    play = "y"
    
    Xwins = 0
    Owins = 0
    draws = 0
    
    X_time = 0
    X_turns = 0
    O_time = 0
    O_turns = 0
    
    #node_totalX = 0
    #node_totalO = 0
    
    

    while play == "y":
        start = time.time()
        game = Game(player_x, player_o, Xwins, Owins, draws, X_time, X_turns, O_time, O_turns)
        game.play()
        total_time += time.time() - start
        #print(time.time() - start)
        #testM = True
        num_games += 1
        if (game.draws == 1):
            total_draws += 1
        elif (game.Xwins == 1):
            total_X += 1
        else:
            total_O += 1
        play = input("Play again? y/[n]: ")
        
    X_time = game.X_time
    X_turns = game.X_turns
    O_time = game.O_time
    O_turns = game.O_turns
    #node_totalX = ABagent.node_totalX
    #print("X_time " + str(X_time))
    #print("X_turns " + str(X_turns))
    print("Wins by X: " + str(total_X) + " | Percentage: " + str((total_X/num_games)*100) + " %")
    print("Wins by O: " + str(total_O) + " | Percentage: " + str((total_O/num_games)*100) + " %")
    print("Draws: " + str(total_draws) + "     | Percentage: " + str((total_draws/num_games)*100) + " %")
    print("X's average runtime: " + str(X_time/X_turns))
    print("O's average runtime: " + str(O_time/O_turns))
    print("Algorithm's average runtime: " + str(total_time/num_games))
    #print("X's nodes searched: " + str(node_totalX))
if __name__ == "__main__":
    main()
