from typing import List
#返回一条路径就行 用dfs

class Solution_1091_Second_Variant:
    """
    LeetCode 1091 Variant: Return a single path using DFS
    
    Given an n x n binary matrix grid, return a clear path 
    from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1).
    
    This variant uses DFS to find any valid path (not necessarily the shortest).
    """
    
    def __init__(self):
        # 8 directions: up, up-right, right, down-right, down, down-left, left, up-left
        self.directions = [
            [-1, 0], [-1, 1], [0, 1], [1, 1],
            [1, 0], [1, -1], [0, -1], [-1, -1]
        ]
    
    def _dfs_1091(self, grid: List[List[int]], path: List[List[int]], row: int, col: int) -> bool:
        """
        DFS helper function to find a path to destination.
        
        Args:
            grid: Binary matrix
            path: Current path being built
            row: Current row position
            col: Current column position
            
        Returns:
            True if path to destination found, False otherwise
        """
        # Mark current cell as visited
        grid[row][col] = 1
        path.append([row, col])
        
        # Check if we reached the destination
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return True
        
        # Try all 8 directions
        for dr, dc in self.directions:
            new_row = row + dr
            new_col = col + dc
            
            # Check bounds
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                continue
            
            # Check if cell is clear and unvisited
            if grid[new_row][new_col] == 1:
                continue
            
            # Recursively try this direction
            if self._dfs_1091(grid, path, new_row, new_col):
                return True
        
        # If no direction leads to destination, backtrack
        path.pop()
        return False
    
    def pathBinaryMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Find a path from top-left to bottom-right using DFS.
        
        Args:
            grid: Binary matrix where 0 represents clear cell, 1 represents blocked cell
            
        Returns:
            List of coordinates representing a valid path, or empty list if no path exists
        """
        if not grid or not grid[0]:
            return []
            
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
            return []
        
        # Create a copy of grid to avoid modifying the original
        grid_copy = [row[:] for row in grid]
        path = []
        
        # Start DFS from (0, 0)
        self._dfs_1091(grid_copy, path, 0, 0)
        
        return path


# Example usage and test
if __name__ == "__main__":
    solution = Solution_1091_Second_Variant()
    
    # Test case 1: Example from LeetCode
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    path1 = solution.pathBinaryMatrix(grid1)
    print(f"Grid 1 path: {path1}")
    print(f"Path length: {len(path1)}")
    
    # Test case 2: Larger grid
    grid2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    path2 = solution.pathBinaryMatrix(grid2)
    print(f"Grid 2 path: {path2}")
    print(f"Path length: {len(path2)}")
    
    # Test case 3: No path possible
    grid3 = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    path3 = solution.pathBinaryMatrix(grid3)
    print(f"Grid 3 path: {path3}")
    
    # Test case 4: Simple 2x2 grid
    grid4 = [
        [0, 0],
        [0, 0]
    ]
    path4 = solution.pathBinaryMatrix(grid4)
    print(f"Grid 4 path: {path4}")
    print(f"Path length: {len(path4)}")
    
    # Test case 5: Complex grid with multiple possible paths
    grid5 = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]
    path5 = solution.pathBinaryMatrix(grid5)
    print(f"Grid 5 path: {path5}")
    print(f"Path length: {len(path5)}")
    
    # Verify that the path is valid
    if path5:
        print("Verifying path validity...")
        valid = True
        for i, (r, c) in enumerate(path5):
            if grid5[r][c] == 1 and i > 0:  # Start cell can be 1 after marking
                valid = False
                break
        print(f"Path is valid: {valid}")
