from utils.treenode import TreeNode

class Solution_270_Variant:
    def closestValue(self, root: TreeNode, target: int) -> int:
        """
        在二叉搜索树中找到最接近目标值的节点值（变体版本）
        目标值为整数类型，遍历逻辑略有调整
        
        Args:
            root: 二叉搜索树的根节点
            target: 目标值 (整数类型)
            
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
            
            # 根据BST性质决定遍历方向（注意：这里的逻辑与原始版本略有不同）
            if root.val > target:
                root = root.left
            else:
                root = root.right
        
        return result


# 测试代码
def test_closest_value_variant():
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
    
    solution = Solution_270_Variant()
    
    # 测试用例
    test_cases = [
        (3, 3),    # 应该返回3
        (2, 2),    # 应该返回2
        (1, 1),    # 应该返回1
        (5, 5),    # 应该返回5
        (0, 1),    # 应该返回1
        (6, 5),    # 应该返回5
    ]
    
    for target, expected in test_cases:
        result = solution.closestValue(root, target)
        print(f"Target: {target}, Expected: {expected}, Got: {result}, {'✓' if result == expected else '✗'}")


if __name__ == "__main__":
    test_closest_value_variant()
