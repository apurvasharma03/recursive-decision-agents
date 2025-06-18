# ♟️ Recursive Decision Agents

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/apurvasharma03/recursive-decision-agents)
![Agents](https://img.shields.io/badge/Agents-Minimax%2C%20Alpha--Beta%2C%20Random-brightgreen)


A simulation framework for evaluating adversarial search strategies in deterministic, turn-based environments. This project implements and compares multiple AI agents—Random, Minimax, and Alpha-Beta Pruned—on a flexible board-based game engine to analyze decision-making under zero-sum, perfect-information conditions.

---

## 🚀 Overview

This framework enables self-play between various agents, each with a distinct move-selection strategy. The system tracks win/loss/draw results along with performance metrics like:

- Per-agent decision time
- Total turns taken
- Win/draw frequency

The game engine supports configurable board dimensions and dynamic win conditions (e.g., 3-in-a-row, 4-in-a-row).

---

## 🤖 Implemented Agents

| Agent            | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| 🎲 **Random Agent**      | Selects a move uniformly at random from available cells                       |
| 🧠 **Minimax (DFS)**     | Uses recursive depth-first Minimax strategy for optimal decision-making        |
| ✂️ **Alpha-Beta Pruned** | Enhances Minimax by pruning non-impactful branches to improve efficiency      |

---

## 🗂️ Project Structure

```
recursive-decision-agents/
├── main.py              # Launch simulations or interactive matches
├── board.py             # Core board logic: win detection, move validity
├── game.py              # Game loop, turn control, result tracking
├── player.py            # Player role and turn ownership
├── random_agent.py      # Random agent logic
├── dfs_agent.py         # Minimax agent (depth-first search)
├── alphabeta_agent.py   # Minimax with Alpha-Beta pruning
```

---

## 📊 Results Summary

| Matchup               | Observed Outcomes                          | Insights                             |
|-----------------------|--------------------------------------------|--------------------------------------|
| Random vs Random      | Mixed results; slight edge for first player| High variance, low draw rate         |
| Minimax vs Random     | Minimax dominates consistently             | Exploits suboptimal random behavior  |
| Minimax vs Minimax    | First player wins more often               | Demonstrates first-move advantage    |
| Alpha-Beta vs Minimax | Same moves, faster execution               | Pruning improves performance         |

---

## 🧪 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/recursive-decision-agents
cd recursive-decision-agents
```

### 2. Run the Program

```bash
python main.py
```

You’ll be prompted to:
- Select two agents to play against each other
- Set board size and win condition (e.g., 3x3 board, 3-in-a-row to win)
- Observe the result and performance breakdown

---

## 🔄 Gameplay Flow

1. **Agent Selection** – Choose agent pair (e.g., Minimax vs Random)
2. **Move Calculation** – Each agent analyzes board state and returns a move
3. **Game Update** – The engine validates moves and checks for victory
4. **Result Output** – Displays winner/draw, turn count, and agent runtime

---

## 🧠 Key Learnings

- Developed recursive game-playing agents within a modular framework
- Implemented core adversarial search algorithms: Minimax and Alpha-Beta
- Quantified performance with measurable metrics (runtime, turns, win rate)
- Observed how strategic depth and pruning influence outcomes in zero-sum games

---

## 📈 Example Output

```
Game: Minimax (X) vs Random (O)

Board:
X | O | X
---------
O | X |  
---------
X |   | O

Winner: Player X
Turns: 7
Runtime: X = 0.09s | O = 0.01s
```

---

## 🧩 Requirements

- Python 3.7 or higher
- No external packages required (standard library only)

---

## 🛠 Future Work

- Add GUI for real-time human vs agent play (e.g., with Tkinter or Pygame)
- Support rectangular boards (e.g., 5x4) and general N-in-a-row settings
- Integrate learning agents (e.g., Q-Learning, MCTS)
- Log historical results across simulations for deeper analysis

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Contributions

Pull requests, issue reports, and feature suggestions are welcome. Let’s build smarter agents together!

---

Recursive Decision Agents is designed to teach, test, and explore strategic behavior in perfect-information environments. Whether you’re studying AI, game theory, or decision-making systems, this project provides a solid foundation for adversarial agent design.
