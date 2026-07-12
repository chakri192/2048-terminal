# 2048 

<div align="center">
  <img src="demo.gif" alt="2048-terminal Gameplay" width="600" />
  <p><em>2048 Terminal Demo</em></p>
</div>


A vibrant, colored terminal implementation of the popular 2048 sliding block puzzle game for macOS. Pure terminal gameplay with beautiful ANSI color tiles.

---

## Overview

Combine tiles with the same number to create larger numbers and reach the 2048 tile to win. Simple rules, addictive gameplay, beautiful terminal colors, and zero dependencies.

---

## Features

- **Colored Tiles** — Each tile value has a unique color scheme matching the original 2048 game
- **Pure Terminal Gameplay** — no GUI, lightweight, fast
- **Score Tracking** — keep track of your points in real-time
- **Move Counter** — see how many moves you've made
- **Win Condition** — reach 2048 to win (or continue playing)
- **Game Over Detection** — automatic detection when no more moves are available
- **Random Tile Spawning** — 90% chance of 2, 10% chance of 4
- **Zero Dependencies** — pure Python 3 implementation, no external packages

---

## Requirements

- **Python** 3.6 or higher
- **macOS** terminal with ANSI color support
- No external dependencies

---

## Installation

```bash
git clone https://github.com/chakri192/2048-terminal.git
cd 2048-terminal
chmod +x game2048.py
```

Add to your PATH in `~/.zshenv`:

```sh
export PATH="$HOME/path/to/2048-terminal:$PATH"
```

Or create an alias:

```sh
alias 2048="python3 ~/.2048-terminal/game2048.py"
```

---

## Usage

```bash
python3 game2048.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `W` or `↑` | Move tiles up |
| `A` or `←` | Move tiles left |
| `S` or `↓` | Move tiles down |
| `D` or `→` | Move tiles right |
| `Q` | Quit game |

---

## How to Play

1. Start with two random tiles (valued 2 or 4)
2. Use WASD or arrow keys to move tiles in the grid
3. When two tiles with the same number touch, they merge into one
4. Each merge adds to your score
5. Try to create a tile with the value 2048 to win
6. After winning, continue playing for higher scores
7. Game ends when you can no longer make any valid moves

---

## Color Scheme

Each tile has a unique color:

- **2** — Light beige
- **4** — Beige
- **8** — Orange
- **16** — Dark orange
- **32** — Red
- **64** — Dark red
- **128** — Gold
- **256** — Dark gold
- **512** — Golden
- **1024** — Dark golden
- **2048+** — Bright gold

---

## Architecture

**Single-file implementation** (~280 lines)

- `Game2048` class — core game logic, grid management, tile merging
- `Color` class — ANSI color codes for terminal coloring
- `Direction` enum — movement directions (WASD)
- `main()` — game loop and input handling

---

## Performance

- **Startup:** Instant
- **Responsiveness:** Real-time input handling
- **Memory:** < 1MB
- **CPU:** Minimal usage

---

## Environment

macOS · Python 3 · Tested on M1/M4 MacBook Air

---

## Author

Created by [chakri192](https://github.com/chakri192)

## Contributors

| Contributor | Role |
|-------------|------|
| [chakri192](https://github.com/chakri192) | Author |
| [aider](https://github.com/Aider-AI/aider) | AI pair programmer |

### AI tooling

README and code contributions assisted by [aider](https://github.com/Aider-AI/aider) using local LLMs via [Ollama](https://ollama.com):

| Model | Used for |
|-------|----------|
| `qwen2.5-coder:7b` | Code suggestions, refactoring |
| `llama3.1:8b` | Prose, documentation, commit messages |
