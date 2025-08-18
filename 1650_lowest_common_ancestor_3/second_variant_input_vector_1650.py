class Node:
    def __init__(self, val=0, left=None, right=None, next=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        self.parent = parent

def lowestCommonAncestor_second_variant_1650(nodes: list[Node], p_start: Node, q_start: Node) -> Node:
    """
    变体版本：当没有根节点信息时，通过构建子节点到父节点的映射来找到最低公共祖先
    
    算法思路：
    1. 遍历所有节点，构建子节点到父节点的映射
    2. 使用两个指针p和q分别从p_start和q_start开始
    3. 两个指针同时向上遍历父节点（通过映射获取）
    4. 当其中一个到达根节点时，重置到另一个起始点
    5. 最终两个指针会在最低公共祖先处相遇
    
    时间复杂度: O(n + h)，其中n是节点数量，h是树的高度
    空间复杂度: O(n)，用于存储子节点到父节点的映射
    """
    # 构建子节点到父节点的映射
    child_to_parent = {}
    for node in nodes:
        if node.left is not None:
            child_to_parent[node.left] = node
        if node.right is not None:
            child_to_parent[node.right] = node
    
    p = p_start
    q = q_start
    
    while p != q:
        if p in child_to_parent:
            p = child_to_parent[p]
        else:
            p = q_start
            
        if q in child_to_parent:
            q = child_to_parent[q]
        else:
            q = p_start
    
    return p

def test_second_variant_1650():
    """测试变体版本的算法"""
    # 构建测试树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #        \
    #         6
    #        /
    #       7
    
    root = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    
    # 设置左右子节点关系（不设置parent指针）
    root.left = node_2
    root.right = node_3
    
    node_2.left = node_4
    node_2.right = node_5
    
    node_5.right = node_6
    
    node_6.left = node_7
    
    # 构建节点列表
    nodes = [root, node_2, node_4, node_5, node_6, node_7, node_3]
    
    print("测试变体版本算法:")
    
    # 测试用例1: 不同子树的节点
    result = lowestCommonAncestor_second_variant_1650(nodes, node_4, node_7)
    print(f"节点4和节点7的最低公共祖先: {result.val} (期望: 2)")
    assert result.val == 2, f"期望2，实际{result.val}"
    
    # 测试用例2: 同一节点（根据注释，这种情况在实际约束中不允许，但算法应该能处理）
    result = lowestCommonAncestor_second_variant_1650(nodes, node_3, node_3)
    print(f"节点3和节点3的最低公共祖先: {result.val} (期望: 3)")
    assert result.val == 3, f"期望3，实际{result.val}"
    
    # 测试用例3: 同一子树，答案是p
    result = lowestCommonAncestor_second_variant_1650(nodes, node_5, node_6)
    print(f"节点5和节点6的最低公共祖先: {result.val} (期望: 5)")
    assert result.val == 5, f"期望5，实际{result.val}"
    
    # 测试用例4: 同一子树
    result = lowestCommonAncestor_second_variant_1650(nodes, node_5, node_7)
    print(f"节点5和节点7的最低公共祖先: {result.val} (期望: 5)")
    assert result.val == 5, f"期望5，实际{result.val}"
    
    # 测试用例5: 根节点和另一个节点
    result = lowestCommonAncestor_second_variant_1650(nodes, root, node_3)
    print(f"根节点和节点3的最低公共祖先: {result.val} (期望: 1)")
    assert result.val == 1, f"期望1，实际{result.val}"
    
    print("所有测试通过！")

def test_edge_cases():
    """测试边界情况"""
    print("\n测试边界情况:")
    
    # 测试1: 只有根节点
    root = Node(1)
    nodes = [root]
    result = lowestCommonAncestor_second_variant_1650(nodes, root, root)
    print(f"只有根节点的情况: {result.val} (期望: 1)")
    assert result.val == 1, f"期望1，实际{result.val}"
    
    # 测试2: 线性树
    # 1 -> 2 -> 3
    root = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    
    root.right = node_2
    node_2.right = node_3
    
    nodes = [root, node_2, node_3]
    
    result = lowestCommonAncestor_second_variant_1650(nodes, root, node_3)
    print(f"线性树的情况: {result.val} (期望: 1)")
    assert result.val == 1, f"期望1，实际{result.val}"
    
    # 测试3: 不平衡树
    #     1
    #    /
    #   2
    #  /
    # 3
    root = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    
    root.left = node_2
    node_2.left = node_3
    
    nodes = [root, node_2, node_3]
    
    result = lowestCommonAncestor_second_variant_1650(nodes, node_3, root)
    print(f"不平衡树的情况: {result.val} (期望: 1)")
    assert result.val == 1, f"期望1，实际{result.val}"
    
    print("所有边界情况测试通过！")

if __name__ == "__main__":
    test_second_variant_1650()
    test_edge_cases()
