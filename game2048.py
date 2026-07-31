#!/usr/bin/env python3
"""2048 Terminal Game - Colored Terminal Version for macOS"""

import os
import sys
import random
import copy
from enum import Enum


class Color:
    """ANSI color codes for terminal"""
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Background colors
    BG_EMPTY = '\033[48;2;100;100;100m'      # Gray
    BG_2 = '\033[48;2;238;228;218m'          # Light beige
    BG_4 = '\033[48;2;237;224;200m'          # Beige
    BG_8 = '\033[48;2;242;177;121m'          # Orange
    BG_16 = '\033[48;2;245;149;99m'          # Dark orange
    BG_32 = '\033[48;2;246;124;95m'          # Red
    BG_64 = '\033[48;2;246;94;59m'           # Dark red
    BG_128 = '\033[48;2;237;207;114m'        # Gold
    BG_256 = '\033[48;2;237;204;97m'         # Dark gold
    BG_512 = '\033[48;2;237;200;80m'         # Golden
    BG_1024 = '\033[48;2;237;197;63m'        # Dark golden
    BG_2048 = '\033[48;2;237;194;46m'        # Bright gold
    BG_HIGH = '\033[48;2;60;58;50m'          # Dark

    # Text colors
    TEXT_DARK = '\033[38;2;119;110;101m'     # Dark text
    TEXT_LIGHT = '\033[38;2;249;246;242m'    # Light text
    TEXT_WHITE = '\033[38;2;255;255;255m'    # White


class Direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'


class Game2048:
    # Color mapping for tiles
    COLOR_MAP = {
        0: (Color.BG_EMPTY, Color.TEXT_DARK),
        2: (Color.BG_2, Color.TEXT_DARK),
        4: (Color.BG_4, Color.TEXT_DARK),
        8: (Color.BG_8, Color.TEXT_WHITE),
        16: (Color.BG_16, Color.TEXT_WHITE),
        32: (Color.BG_32, Color.TEXT_WHITE),
        64: (Color.BG_64, Color.TEXT_WHITE),
        128: (Color.BG_128, Color.TEXT_DARK),
        256: (Color.BG_256, Color.TEXT_DARK),
        512: (Color.BG_512, Color.TEXT_DARK),
        1024: (Color.BG_1024, Color.TEXT_DARK),
        2048: (Color.BG_2048, Color.TEXT_DARK),
    }

    def __init__(self, size=4):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.score = 0
        self.moves = 0
        self.game_over = False
        self.won = False
        self._add_random_tile()
        self._add_random_tile()

    def _add_random_tile(self):
        """Add a random tile (90% chance of 2, 10% chance of 4)."""
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 4 if random.random() < 0.1 else 2

    def _can_move(self, direction):
        """Check if a move is possible."""
        grid_copy = copy.deepcopy(self.grid)
        score_copy = self.score  # _move -> _merge mutates score; restore it so
                                 # probing for possible moves can't inflate it
        self._move(direction)
        can_move = grid_copy != self.grid
        self.grid = grid_copy
        self.score = score_copy
        return can_move

    def _move(self, direction):
        """Execute a move."""
        if direction == Direction.LEFT:
            self._move_left()
        elif direction == Direction.RIGHT:
            self._move_right()
        elif direction == Direction.UP:
            self._move_up()
        elif direction == Direction.DOWN:
            self._move_down()

    def _compress(self, line):
        """Remove zeros from a line."""
        return [x for x in line if x != 0]

    def _merge(self, line):
        """Merge tiles in a line."""
        new_line = []
        i = 0
        while i < len(line):
            if i + 1 < len(line) and line[i] == line[i + 1]:
                merged = line[i] * 2
                new_line.append(merged)
                self.score += merged
                i += 2
            else:
                new_line.append(line[i])
                i += 1
        return new_line

    def _pad_line(self, line, size):
        """Pad a line with zeros."""
        return line + [0] * (size - len(line))

    def _move_left(self):
        """Move tiles left."""
        for i in range(self.size):
            line = self._compress(self.grid[i])
            line = self._merge(line)
            self.grid[i] = self._pad_line(line, self.size)

    def _move_right(self):
        """Move tiles right."""
        for i in range(self.size):
            line = self._compress(self.grid[i][::-1])
            line = self._merge(line)
            self.grid[i] = self._pad_line(line, self.size)[::-1]

    def _move_up(self):
        """Move tiles up."""
        for j in range(self.size):
            column = [self.grid[i][j] for i in range(self.size)]
            column = self._compress(column)
            column = self._merge(column)
            column = self._pad_line(column, self.size)
            for i in range(self.size):
                self.grid[i][j] = column[i]

    def _move_down(self):
        """Move tiles down."""
        for j in range(self.size):
            column = [self.grid[i][j] for i in range(self.size)][::-1]
            column = self._compress(column)
            column = self._merge(column)
            column = self._pad_line(column, self.size)[::-1]
            for i in range(self.size):
                self.grid[i][j] = column[i]

    def move(self, direction):
        """Execute move and add new tile."""
        if self.game_over or self.won:
            return False

        grid_copy = copy.deepcopy(self.grid)
        self._move(direction)

        if grid_copy != self.grid:
            self._add_random_tile()
            self.moves += 1
            self._check_game_state()
            return True
        return False

    def _check_game_state(self):
        """Check if game is won or over."""
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 2048 and not self.won:
                    self.won = True
                    return

        if not any(self._can_move(d) for d in Direction):
            self.game_over = True

    def _get_color(self, value):
        """Get color for a tile value."""
        if value in self.COLOR_MAP:
            return self.COLOR_MAP[value]
        return self.COLOR_MAP.get(2048, (Color.BG_HIGH, Color.TEXT_WHITE))

    def _format_tile(self, value):
        """Format a tile with color."""
        bg, text = self._get_color(value)
        if value == 0:
            return f"{bg}   {Color.RESET}"
        else:
            tile_str = str(value).rjust(3)
            return f"{bg}{text}{tile_str}{Color.RESET}"

    def display(self):
        """Display the game board with colors."""
        os.system('clear')

        print(f"\n{Color.TEXT_WHITE}{Color.BOLD}2048.c{Color.RESET}".ljust(25) +
              f"{Color.TEXT_WHITE}{self.score} pts{Color.RESET}\n")

        for row in self.grid:
            for tile in row:
                print(self._format_tile(tile), end=" ")
            print()

        print(f"\n{Color.TEXT_WHITE}←,↑,→,↓ or q{Color.RESET}\n")

    def reset(self):
        """Reset the game."""
        self.__init__(self.size)


def main():
    """Main game loop."""
    game = Game2048()

    try:
        while True:
            game.display()

            if game.game_over:
                print(f"{Color.TEXT_WHITE}GAME OVER! Final Score: {game.score}{Color.RESET}")
                break

            if game.won:
                choice = input(f"{Color.TEXT_WHITE}YOU WIN! Continue? (y/n): {Color.RESET}").lower()
                if choice == 'n':
                    print(f"{Color.TEXT_WHITE}Final Score: {game.score}{Color.RESET}")
                    break
                else:
                    game.won = False
                    continue

            move = input(f"{Color.TEXT_WHITE}Move (w/a/s/d) or q: {Color.RESET}").lower()

            if move == 'q':
                print(f"{Color.TEXT_WHITE}Final Score: {game.score}{Color.RESET}")
                break

            try:
                direction = Direction(move)
                if not game.move(direction):
                    print(f"{Color.TEXT_WHITE}Invalid move!{Color.RESET}")
                    input("Press Enter to continue...")
            except ValueError:
                print(f"{Color.TEXT_WHITE}Invalid input!{Color.RESET}")
                input("Press Enter to continue...")

    except KeyboardInterrupt:
        print(f"\n{Color.TEXT_WHITE}Game interrupted. Final Score: {game.score}{Color.RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
