from typing import Optional
#求average of bst
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeAverageBST(self, root: Optional[TreeNode], low: int, high: int) -> float:
        count = 0

        def dfs(root):
            nonlocal count
            if not root: return 0
            x = root.val
            if x > high:
                return dfs(root.left)
            elif x < low:
                return dfs(root.right)
            else:
                count +=1

            return x+dfs(root.left)+dfs(root.right)
        
        return dfs(root) / count

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right = TreeNode(15)
    root.right.right = TreeNode(18)

    assert solution.rangeAverageBST(root, 7, 15) == 32.0 / 3.0
    assert solution.rangeAverageBST(root, 0, 9000) == 58.0 / 6.0
    assert solution.rangeAverageBST(root, 7, 7) == 7.0
    assert solution.rangeAverageBST(root, 14, 18) == 33.0 / 2.0
    assert solution.rangeAverageBST(root, 3, 6) == 4.0