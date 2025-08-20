from typing import Optional
from itertools import accumulate
from bisect import bisect_left, bisect_right

#如果这个函数会被call 100000 times， 怎么提升算法效率 答： inorder 的过程中构建前缀和， 然后二分找上下
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self, root) -> None:
        self.vals = []
        self.presum = [0]
        self.inorder(root)
    
    def inorder(self, root):
        if not root: return

        self.inorder(root.left)
        self.vals.append(root.val)
        self.presum.append(self.presum[-1]+root.val)
        self.inorder(root.right)

    def calculate(self, low: int, high: int) -> int:

        left = bisect_left(self.vals, low)
        right = bisect_left(self.vals, high+1)-1

        return self.presum[right+1] - self.presum[left]

        

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(6)

    root.right = TreeNode(15)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)

    solution = Solution(root)
    print(solution.vals)
    print(solution.presum)
    assert solution.calculate(5, 16) == 56
    assert solution.calculate(0, 9000) == 1 + 3 + 5 + 6 + 7 + 10 + 13 + 15 + 18
    assert solution.calculate(7, 7) == 7
    assert solution.calculate(14, 18) == 33
    assert solution.calculate(3, 6) == 14