from typing import List, Set, Tuple

# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
class Robot:
    def move(self) -> bool:
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        """
        pass

    def turnLeft(self) -> None:
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        """
        pass

    def turnRight(self) -> None:
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        """
        pass

    def clean(self) -> None:
        """Clean the current cell."""
        pass


class Solution_489:
    def __init__(self):
        # Direction offsets: (row, col)
        self.directions = [
            (-1, 0),  # Top
            (0, 1),   # Right
            (1, 0),   # Down
            (0, -1)   # Left
        ]
        self.visited: Set[Tuple[int, int]] = set()

    def dfs(self, robot: Robot, direction: int, row: int, col: int) -> None:
        robot.clean()
        self.visited.add((row, col))

        for i in range(len(self.directions)):
            new_direction = (direction + i) % 4
            new_row = row + self.directions[new_direction][0]
            new_col = col + self.directions[new_direction][1]

            if (new_row, new_col) in self.visited or not robot.move():
                robot.turnRight()
                continue
            
            self.dfs(robot, new_direction, new_row, new_col)
            robot.turnRight()
        
        # Return to previous position
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def cleanRoom(self, robot: Robot) -> None:
        direction = 0
        self.dfs(robot, direction, 0, 0)
