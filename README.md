# recursive-decision-agents

A simulation framework for evaluating adversarial search strategies in deterministic, turn-based environments. This project implements and compares multiple agents—random, depth-first Minimax, and Alpha-Beta Pruned—on a flexible board-based game engine. It is designed to study decision-making under zero-sum, perfect-information conditions.

## Overview

This project was built to explore AI agent behavior through self-play, with each agent implementing a different move-selection strategy. Game results include not only win/loss/draw outcomes but also performance metrics like per-agent runtime and turn counts. The environment supports variable board sizes and win conditions.

### Implemented Agents

- **Random Agent**  
  Selects a move uniformly at random from available cells.

- **Minimax Agent (DFS)**  
  Performs recursive depth-first evaluation of the game tree using the Minimax strategy to choose optimal moves.

- **Alpha-Beta Agent**  
  Enhances Minimax by pruning branches that do not influence the final decision, improving efficiency without compromising correctness.

## Project Structure

- `main.py`: Entry point for running simulations or interactive matches.
- `board.py`: Encapsulates the board logic, including move validation, win detection, and diagonal/row/column access.
- `game.py`: Controls game execution flow, agent turns, timing, and result tracking.
- `player.py`: Defines player identities and turn ownership (X vs O).
- `random_agent.py`, `dfs_agent.py`, `alphabeta_agent.py`: Agent strategies implemented separately.

## Results Summary

- **Random vs Random**: Mixed results with low draw rate. Slight advantage typically for X (first mover).
- **Minimax vs Random**: Minimax agent consistently outperforms due to exhaustive tree search.
- **Minimax vs Minimax**: First player often wins, illustrating the first-move advantage in zero-sum perfect-information games.
- **Alpha-Beta vs Minimax**: Identical decisions, with reduced runtime due to effective pruning.

## Execution Workflow

1. The user runs `main.py` and selects agent configurations (e.g., Random vs DFS).
2. Each agent computes its move based on the current board state.
3. The board checks for valid moves and win conditions after every turn.
4. The game continues until a win or draw is detected.
5. Results are printed, and runtime statistics (per agent) are tracked across repeated games.

## Key Learnings

- Designed and implemented multiple AI agents within a consistent game framework.
- Developed recursive algorithms for optimal decision-making under adversarial conditions.
- Applied Alpha-Beta Pruning to reduce search complexity while preserving accuracy.
- Quantitatively evaluated performance using runtime per agent, number of turns, and outcome frequencies.

## Future Work

- Add a graphical interface for real-time human-vs-agent matches.
- Extend support to non-square boards or N-in-a-row generalizations.
- Experiment with learning-based agents (e.g., Monte Carlo Tree Search or Q-Learning).

---

This project was implemented in Python 3. All gameplay logic is fully deterministic and based on perfect-information assumptions.
