<div align="center">

# 2048-terminal

**The sliding-block puzzle, in true colour, in your terminal.**

One Python file, no dependencies, no curses — just 24-bit ANSI and the standard library.

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.6%2B-1c1c1e?style=flat-square&logo=python&logoColor=3776AB" />
  <img alt="Dependencies" src="https://img.shields.io/badge/dependencies-none-1c1c1e?style=flat-square" />
  <img alt="Size" src="https://img.shields.io/badge/259-lines-1c1c1e?style=flat-square" />
  <img alt="Colour" src="https://img.shields.io/badge/24--bit-truecolor-1c1c1e?style=flat-square" />
</p>

<br />

<img src="demo.gif" alt="2048-terminal gameplay" width="620" />

</div>

<br />

---

## Play it

```bash
git clone https://github.com/chakri192/2048-terminal.git
cd 2048-terminal
python3 game2048.py
```

Nothing to install. Python 3.6 or newer, and a terminal that does 24-bit colour — Terminal.app, iTerm2, Alacritty, kitty, WezTerm, and modern Windows Terminal all qualify.

Want it on your `$PATH`?

```bash
chmod +x game2048.py
ln -s "$PWD/game2048.py" /usr/local/bin/2048
```

---

## Controls

Type a letter, then press **Enter**.

| Key | Action |
|---|---|
| `w` | Up |
| `a` | Left |
| `s` | Down |
| `d` | Right |
| `q` | Quit, and print your final score |

Input is line-buffered, so every move needs a Return. Arrow keys aren't wired up — that would mean putting the terminal into raw mode and parsing escape sequences, which is exactly the dependency-free simplicity this trades away. `Ctrl-C` quits cleanly and still reports your score.

Reach 2048 and it asks whether to keep going; answer `y` and play on for a higher tile.

---

## How the board actually moves

The whole game is three functions applied to one row:

```python
line = self._compress(self.grid[i])      # [2,0,2,4] → [2,2,4]     drop the gaps
line = self._merge(line)                 # [2,2,4]   → [4,4]       combine, +4 score
self.grid[i] = self._pad_line(line, 4)   # [4,4]     → [4,4,0,0]   refill to width
```

Everything else is bookkeeping around that. `RIGHT` is `LEFT` on a reversed row, reversed back. `UP` is the same pipeline over a column. `DOWN` is a reversed column. Four directions, one algorithm, no special cases.

**Merged tiles are locked for the rest of the move.** `_merge` advances by two after combining a pair, so `[2,2,4]` becomes `[4,4]` and not `[8]`. Skip that detail and the game becomes trivially easy — it's the rule that makes 2048 a puzzle instead of a pile.

**Legality is decided by simulation.** `_can_move` deep-copies the grid, plays the move, and asks whether anything changed. There's a subtlety in there: `_merge` bumps `self.score` as a side effect, so a probe would quietly award points for moves you never made. It saves and restores the score around the trial.

Game over is that same check run four times — when no direction changes the grid, there are no moves left.

---

## The colours

Every tile value gets the palette from the original browser game, emitted as true-colour ANSI (`\033[48;2;R;G;Bm`) rather than the 16-colour approximations most terminal ports settle for:

| Tile | Colour | | Tile | Colour |
|---|---|---|---|---|
| `2` | light beige | | `128` | gold |
| `4` | beige | | `256` | deeper gold |
| `8` | orange | | `512` | golden |
| `16` | dark orange | | `1024` | dark golden |
| `32` | red | | `2048` | bright gold |
| `64` | dark red | | above | dark slate |

Text flips from dark to light at `8`, which is where the backgrounds get dark enough to need it.

---

## Layout

```
2048-terminal/
├── game2048.py    Color · Direction · Game2048 · main      259 lines
└── demo.gif
```

`Game2048` holds the grid, score, move count, and win/over flags. New tiles spawn on a random empty cell — 90% a `2`, 10% a `4`, same odds as the original.

---

## Author

[chakri192](https://github.com/chakri192) · tested on macOS, Apple Silicon
