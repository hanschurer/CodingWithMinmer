from typing import List, Set, Tuple, NamedTuple
from collections import namedtuple

# Direction offsets: (row, col)
Direction = namedtuple('Direction', ['offsets'])

class Mouse:
    def __init__(self, grid: List[List[str]], cheese_location: Tuple[int, int]):
        # NOT PART OF IMPLEMENTATION
        self.grid = grid
        self.cheese_location = cheese_location
        
        # Direction offsets: (row, col)
        self.directions = [
            Direction((-1, 0)),  # Top
            Direction((0, 1)),    # Right
            Direction((1, 0)),    # Down
            Direction((0, -1))    # Left
        ]
        
        # Opposite directions for backtracking
        self.opposite_directions = [
            Direction((1, 0)),    # Bottom
            Direction((0, -1)),   # Left
            Direction((-1, 0)),   # Top
            Direction((0, 1))     # Right
        ]
        
        self.visited: Set[Tuple[int, int]] = set()

    def dfs(self, row: int, col: int) -> bool:
        if self.hasCheese(row, col):
            return True
        
        self.visited.add((row, col))

        for i in range(len(self.directions)):
            new_row = row + self.directions[i].offsets[0]
            new_col = col + self.directions[i].offsets[1]
            
            if (new_row, new_col) in self.visited:
                continue
                
            if not self.move(self.directions[i], row, col):
                self.move(self.opposite_directions[i], row, col)
                continue

            if self.dfs(new_row, new_col):
                return True
                
            self.move(self.opposite_directions[i], row, col)
        
        return False

    def move(self, direction: Direction, row: int, col: int) -> bool:
        """
        Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
        """
        new_row = row + direction.offsets[0]
        new_col = col + direction.offsets[1]

        # Check boundaries
        if new_row < 0 or new_row >= len(self.grid):
            return False
            
        if new_col < 0 or new_col >= len(self.grid[0]):
            return False
            
        # Check if cell is blocked
        if self.grid[new_row][new_col] == 'X':
            return False

        return True

    def hasCheese(self, row: int, col: int) -> bool:
        """
        Returns true if there is a cheese in the current cell.
        """
        return row == self.cheese_location[0] and col == self.cheese_location[1]

    def getCheese(self) -> bool:
        """
        Should return true and leave the mouse at that location or
        false if we can't find cheese and return the mouse back to
        where it started.
        """
        return self.dfs(0, 0)
