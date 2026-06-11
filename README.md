# ByteGame
ByteGame is a Python game supporting both two-player gameplay and single-player mode against an AI-controlled opponent.

## Features
- Two-player mode (player vs player)
- Single-player mode against a computer (AI opponent)
- Simple heuristic-based AI 
- Console-based (CLI) game
- Turn-based game mechanics with clear state transitions

## Technologies Used
- Python

## How It Works
- ByteGame is a turn-based console game where two players take turns making moves according to the game rules. The game maintains a shared state that is updated after each move.
- In single-player mode, the human player competes against a computer-controlled opponent. The AI evaluates possible moves using a simple heuristic: it simulates available actions and avoids moves that would immediately allow the opponent to score.
- The game continues until a win condition is reached, after which the final result is displayed in the console.
- All interaction happens through the terminal, where players input their moves and receive game updates after each turn.

## How To Run The Application
### 1. Clone the repository
```bash
git clone <repo-url>
cd your-project-folder
```
### 2. Install server dependencies
Go to the server directory and install required packages:

```bash
cd server
npm install
```
### 3. Start the server
```bash
npm start
```
The server will run on:
```bash
ws://localhost:3000
```
### 4. Run the client
Open the client folder and start `index.html`.

> **Recommended way:**  
> Use VS Code Live Server extension  
> Right click `index.html` → “Open with Live Server”

## Screenshots
### Initial State of the Application


### Active Chat (Messages Sent)



## Project Information
- Developed: 2023  
- Improved: 2026  
- Type: Academic Project

## Author
- Andjela Djordjevic
