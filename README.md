# 2048 Terminal

A command-line implementation of the popular 2048 sliding block puzzle game for macOS.

---

## Overview

Combine tiles with the same number to create larger numbers and reach the 2048 tile to win. Simple rules, addictive gameplay, pure terminal fun.

---

## Features

- **Pure Terminal Gameplay** — no GUI, lightweight, fast
- **Score Tracking** — keep track of your best scores
- **Move Counter** — see how many moves you've made
- **Win Condition** — reach 2048 to win (or continue playing)
- **Game Over Detection** — automatic detection when no more moves are available
- **Random Tile Spawning** — 90% chance of 2, 10% chance of 4
- **Zero Dependencies** — pure Python 3 implementation

---

## Requirements

- **Python** 3.6 or higher
- **macOS** terminal with `clear` command
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
| `W` | Move tiles up |
| `A` | Move tiles left |
| `S` | Move tiles down |
| `D` | Move tiles right |
| `Q` | Quit game |

---

## How to Play

1. Start with two random tiles (valued 2 or 4)
2. Use WASD to move tiles in the grid
3. When two tiles with the same number touch, they merge into one
4. Each merge adds to your score
5. Try to create a tile with the value 2048 to win
6. After winning, continue playing for higher scores
7. Game ends when no more moves are available

---

## Example Gameplay

```
===================================
           2048 TERMINAL
===================================
Score: 2,304 | Moves: 28
-----------------------------------
|   32 |  128 |  256 | 1024 |
|   16 |   64 |  512 |    4 |
|    8 |    4 |    2 |      |
|    4 |      |      |      |
-----------------------------------
Controls: W(up) S(down) A(left) D(right) Q(quit)
===================================
```

---

## Architecture

**Single-file implementation** (~200 lines)

- `Game2048` class — core game logic, grid management, tile merging
- `Direction` enum — movement directions (WASD)
- `main()` — game loop and input handling

---

## Environment

macOS · Python 3 · Tested on M1/M4 MacBook Air

---

## License

MIT
