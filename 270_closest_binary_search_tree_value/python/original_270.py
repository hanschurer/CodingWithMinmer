from utils.treenode import TreeNode

class Solution_270:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        在二叉搜索树中找到最接近目标值的节点值
        
        Args:
            root: 二叉搜索树的根节点
            target: 目标值 (float类型)
            
        Returns:
            最接近目标值的节点值
        """
        closest_distance = float('inf')
        result = 0
        
        while root is not None:
            distance = abs(root.val - target)
            
            # 如果找到更近的距离，或者距离相等但值更小
            if (distance < closest_distance or 
                (distance == closest_distance and root.val < result)):
                closest_distance = distance
                result = root.val
            
            # 如果找到完全匹配的值，直接返回
            if distance == 0:
                return root.val
            
            # 根据BST性质决定遍历方向
            if root.val < target:
                root = root.right
            else:
                root = root.left
        
        return result


# 测试代码
def test_closest_value():
    # 创建测试树: [4,2,5,1,3]
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    solution = Solution_270()
    
    # 测试用例
    test_cases = [
        (3.714286, 4),  # 应该返回4
        (2.1, 2),       # 应该返回2
        (1.9, 2),       # 应该返回2
        (5.1, 5),       # 应该返回5
        (0.5, 1),       # 应该返回1
    ]
    
    for target, expected in test_cases:
        result = solution.closestValue(root, target)
        print(f"Target: {target}, Expected: {expected}, Got: {result}, {'✓' if result == expected else '✗'}")


if __name__ == "__main__":
    test_closest_value()
