#!/usr/bin/env python3
"""2048 Terminal Game for macOS"""

import os
import sys
import random
import copy
from enum import Enum


class Direction(Enum):
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'


class Game2048:
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
        self._move(direction)
        can_move = grid_copy != self.grid
        self.grid = grid_copy
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

    def display(self):
        """Display the game board."""
        os.system('clear')
        print("\n" + "=" * 35)
        print("           2048 TERMINAL")
        print("=" * 35)
        print(f"Score: {self.score:,} | Moves: {self.moves}")
        print("-" * 35)
        
        for row in self.grid:
            print("|", end="")
            for tile in row:
                if tile == 0:
                    print("     |", end="")
                else:
                    print(f" {tile:>4} |", end="")
            print()
        
        print("-" * 35)
        if self.won:
            print("🎉 YOU WON! Continue? (y/n)")
        elif self.game_over:
            print("❌ GAME OVER! No more moves available.")
        else:
            print("Controls: W(up) S(down) A(left) D(right) Q(quit)")
        print("=" * 35 + "\n")


def main():
    """Main game loop."""
    game = Game2048()
    
    try:
        while True:
            game.display()
            
            if game.game_over:
                print(f"Final Score: {game.score:,}")
                break
            
            if game.won:
                choice = input("Enter 'y' to continue or 'n' to quit: ").lower()
                if choice == 'n':
                    print(f"Final Score: {game.score:,}")
                    break
                else:
                    game.won = False
                    continue
            
            move = input("Enter move (w/a/s/d) or 'q' to quit: ").lower()
            
            if move == 'q':
                print(f"Game ended. Final Score: {game.score:,}")
                break
            
            try:
                direction = Direction(move)
                if not game.move(direction):
                    print("Invalid move!")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid input! Use w/a/s/d or 'q' to quit.")
                input("Press Enter to continue...")
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Final Score:", game.score)
        sys.exit(0)


if __name__ == "__main__":
    main()
