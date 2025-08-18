from typing import List
from collections import deque


class Solution_1091:
    """
    LeetCode 1091: Shortest Path in Binary Matrix
    
    Given an n x n binary matrix grid, return the length of the shortest clear path 
    from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1).
    
    A clear path is a path from the top-left cell to the bottom-right cell such that:
    - All visited cells of the path are 0
    - All adjacent cells of the path are 8-directionally connected
    - The length of a clear path is the number of visited cells of this path
    """
    
    def __init__(self):
        # 8 directions: up, up-right, right, down-right, down, down-left, left, up-left
        self.directions = [
            [-1, 0], [-1, 1], [0, 1], [1, 1],
            [1, 0], [1, -1], [0, -1], [-1, -1]
        ]
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Find the shortest path length from top-left to bottom-right.
        
        Args:
            grid: Binary matrix where 0 represents clear cell, 1 represents blocked cell
            
        Returns:
            Length of shortest path, or -1 if no path exists
        """
        if not grid or not grid[0]:
            return -1
            
        n = len(grid)
        m = len(grid[0])
        
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        
        # Mark start cell as visited
        grid[0][0] = 1
        
        # BFS queue: (row, col, steps)
        queue = deque([(0, 0, 1)])
        
        while queue:
            row, col, steps = queue.popleft()
            
            # Reached destination
            if row == n - 1 and col == m - 1:
                return steps
            
            # Try all 8 directions
            for dr, dc in self.directions:
                new_row = row + dr
                new_col = col + dc
                
                # Check bounds
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue
                
                # Check if cell is clear and unvisited
                if grid[new_row][new_col] == 1:
                    continue
                
                # Mark as visited and add to queue
                grid[new_row][new_col] = 1
                queue.append((new_row, new_col, steps + 1))
        
        return -1  # No path found


# Example usage and test
if __name__ == "__main__":
    solution = Solution_1091()
    
    # Test case 1: Example from LeetCode
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    print(f"Grid 1 shortest path length: {solution.shortestPathBinaryMatrix([row[:] for row in grid1])}")
    
    # Test case 2: Larger grid
    grid2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(f"Grid 2 shortest path length: {solution.shortestPathBinaryMatrix([row[:] for row in grid2])}")
    
    # Test case 3: No path possible
    grid3 = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(f"Grid 3 shortest path length: {solution.shortestPathBinaryMatrix([row[:] for row in grid3])}")
