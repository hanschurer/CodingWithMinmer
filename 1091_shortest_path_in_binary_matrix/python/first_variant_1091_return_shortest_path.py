from typing import List
from collections import deque

#变种返回path 【】
class Solution_1091_First_Variant:
    """
    LeetCode 1091 Variant: Return the actual shortest path
    
    Given an n x n binary matrix grid, return the shortest clear path 
    from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1).
    
    This variant returns the actual path coordinates instead of just the length.
    """
    
    def __init__(self):
        # 8 directions: up, up-right, right, down-right, down, down-left, left, up-left
        self.directions = [
            [-1, 0], [-1, 1], [0, 1], [1, 1],
            [1, 0], [1, -1], [0, -1], [-1, -1]
        ]
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Find the shortest path from top-left to bottom-right and return the path.
        
        Args:
            grid: Binary matrix where 0 represents clear cell, 1 represents blocked cell
            
        Returns:
            List of coordinates representing the shortest path, or empty list if no path exists
        """
        if not grid or not grid[0]:
            return []
            
        n = len(grid)
        m = len(grid[0])
        
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return []
        
        # Mark start cell as visited
        grid[0][0] = 1
        
        # BFS queue: (row, col, path)
        queue = deque([(0, 0, [[0, 0]])])
        
        while queue:
            row, col, path = queue.popleft()
            
            # Reached destination
            if row == n - 1 and col == m - 1:
                return path
            
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
                
                # Mark as visited and add to queue with updated path
                grid[new_row][new_col] = 1
                new_path = path + [[new_row, new_col]]
                queue.append((new_row, new_col, new_path))
        
        return []  # No path found


# Example usage and test
if __name__ == "__main__":
    solution = Solution_1091_First_Variant()
    
    # Test case 1: Example from LeetCode
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    path1 = solution.shortestPathBinaryMatrix([row[:] for row in grid1])
    print(f"Grid 1 shortest path: {path1}")
    print(f"Path length: {len(path1)}")
    
    # Test case 2: Larger grid
    grid2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    path2 = solution.shortestPathBinaryMatrix([row[:] for row in grid2])
    print(f"Grid 2 shortest path: {path2}")
    print(f"Path length: {len(path2)}")
    
    # Test case 3: No path possible
    grid3 = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    path3 = solution.shortestPathBinaryMatrix([row[:] for row in grid3])
    print(f"Grid 3 shortest path: {path3}")
    
    # Test case 4: Simple 2x2 grid
    grid4 = [
        [0, 0],
        [0, 0]
    ]
    path4 = solution.shortestPathBinaryMatrix([row[:] for row in grid4])
    print(f"Grid 4 shortest path: {path4}")
    print(f"Path length: {len(path4)}")
