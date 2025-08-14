class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_num, negative_count):
            if not node:
                return 0
            
            # 累加当前节点的负数计数（不使用全局变量，而是通过参数传递）
            new_neg_count = negative_count + (1 if node.val < 0 else 0)
            # 拼接当前数字
            new_num = current_num * 10 + abs(node.val)
            
            # 叶子节点：计算符号并返回
            if not node.left and not node.right:
                sign = -1 if new_neg_count % 2 == 1 else 1
                return new_num * sign
            
            # 非叶子节点：递归左右子树（传递新的计数，自然实现回溯）
            return dfs(node.left, new_num, new_neg_count) + dfs(node.right, new_num, new_neg_count)
        
        return dfs(root, 0, 0)

if __name__ == "__main__":
    solution = Solution()
    root = Solution.TreeNode(1, 
            left=Solution.TreeNode(-2), 
            right=Solution.TreeNode(3))
    assert solution.sumNumbers(root) == 1

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2, 
                left=Solution.TreeNode(-9)), 
            right=Solution.TreeNode(4, 
                left=Solution.TreeNode(-5)))
    assert solution.sumNumbers(root) == -129 + 145

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2, 
                left=Solution.TreeNode(-9, 
                    left=Solution.TreeNode(3), 
                        right=Solution.TreeNode(-3))),
            right=Solution.TreeNode(4, 
                left=Solution.TreeNode(-5), 
                    right=Solution.TreeNode(6)))
    assert solution.sumNumbers(root) == -1293 + 1293 + 145 + -146

    root = Solution.TreeNode(1, 
            left=Solution.TreeNode(2), 
            right=Solution.TreeNode(3))
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2), 
            right=Solution.TreeNode(-3))
    assert solution.sumNumbers(root) == 12 + 13

    root = Solution.TreeNode(-1, 
            left=Solution.TreeNode(-2, 
                left=Solution.TreeNode(-3)))
    assert solution.sumNumbers(root) == -123

    root = None
    assert solution.sumNumbers(root) == 0