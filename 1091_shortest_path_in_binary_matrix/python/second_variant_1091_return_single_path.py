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

        # Mark current cell as visited
        grid[row][col] = 1
        path.append([row, col])
        n = len(grid)
        
        # Check if we reached the destination
        if row == n - 1 and col == n - 1:
            return True
        
        # Try all 8 directions
        for dr, dc in self.directions:
            new_row = row + dr
            new_col = col + dc

            if new_row in range(n) and new_col in range(n) and grid[new_row][new_col] == 0:
            # Recursively try this direction
                self._dfs_1091(grid, path, new_row, new_col)
                
        
        # If no direction leads to destination, backtrack
        path.pop()
        return False
    
    def pathBinaryMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        if not grid or not grid[0]:
            return []
            
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
            return []
        
        path = []
        
        # Start DFS from (0, 0)
        self._dfs_1091(grid.copy(), path, 0, 0)
        
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
