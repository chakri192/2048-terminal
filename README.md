# 2048-terminal

2048 in your terminal, in full colour. One Python file, no dependencies.

<img src="demo.gif" alt="2048-terminal gameplay" width="620" />

## Install

Needs Python 3.6+ and a terminal with 24-bit colour (Terminal.app, iTerm2, Ghostty, kitty, Alacritty, WezTerm, most Linux terminals).

```sh
git clone https://github.com/chakri192/2048-terminal.git
cd 2048-terminal
python3 game2048.py
```

To run it as `2048` from anywhere:

```sh
chmod +x game2048.py
ln -s "$PWD/game2048.py" /usr/local/bin/2048
```

## How to play

Type a key and press Enter.

| Key | Action |
|---|---|
| `w` `a` `s` `d` | Move up, left, down, right |
| `q` | Quit |
| `Ctrl-C` | Quit |

Tiles with the same number merge when they slide into each other. Each new tile is a 2 (90%) or a 4 (10%). Reach 2048 to win, then choose whether to keep going. The game ends when no move is possible, and your score is printed when you quit.

Arrow keys aren't supported.

## Contributors

| | |
|---|---|
| [chakri192](https://github.com/chakri192) | Author |
| [aider](https://github.com/Aider-AI/aider) | AI pair programmer |
