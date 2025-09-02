# ✊✋✌️ Rock-Paper-Scissors AI

This project implements an AI agent that learns and adapts to opponent strategies in the game of Rock-Paper-Scissors.  
The AI analyzes the opponent’s past moves using **Markov chain models of varying lengths (2 to 8)** to predict the next move and counter it.  
This multi-length approach allows the AI to adapt to different opponent patterns, from short-term habits to longer repeating sequences.  

It was inspired by the **freeCodeCamp Machine Learning with Python** project challenge.

---

## 📁 Files Included

- **main.py** – ✅ Entry point to run matches and test different players.  
- **RPS_game.py** – 🧠 Contains built-in bot strategies (Quincy, Abbey, Kris, etc.).  
- **RPS.py** – 🤖 Contains the custom `player` function (your AI model).  
- **test_module.py** – 🧪 Unit tests to validate correctness of the solution.  
- **README.md** – ℹ️ Project documentation.

---

## 🧪 Libraries Used
- Python Standard Library only (no external dependencies).

---

## ⚙️ How It Works
1. The AI tracks the opponent’s move history.  
2. It builds frequency tables of sequences (Markov chains) with lengths ranging from **2 to 8**.  
3. For each round, the AI checks which sequence length best matches the recent history.  
4. It predicts the opponent’s most likely next move and selects the counter move.  
5. If there’s not enough data (e.g., at the start), the AI defaults to a random choice.  

This makes the AI flexible:  
- **Short sequences (2-3)** → quickly catch simple repeating patterns.  
- **Longer sequences (5-8)** → detect complex strategies and loops.  

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors-ai.git
   cd rock-paper-scissors-ai
