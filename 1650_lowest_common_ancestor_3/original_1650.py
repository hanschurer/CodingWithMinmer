class Node:
    def __init__(self, val=0, left=None, right=None, next=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        self.parent = parent

def lowestCommonAncestor_1650(p_start: Node, q_start: Node) -> Node:
    """
    找到两个节点的最低公共祖先
    
    算法思路：
    1. 使用两个指针p和q分别从p_start和q_start开始
    2. 两个指针同时向上遍历父节点
    3. 当其中一个到达根节点时，重置到另一个起始点
    4. 最终两个指针会在最低公共祖先处相遇
    
    时间复杂度: O(h)，其中h是树的高度
    空间复杂度: O(1)
    """
    p = p_start
    q = q_start
    
    while p != q:
        if p.parent is not None:
            p = p.parent
        else:
            p = q_start
            
        if q.parent is not None:
            q = q.parent
        else:
            q = p_start
    
    return p

def test_original_1650():
    """测试原始版本的算法"""
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
    
    # 设置父子关系
    root.left = node_2
    root.right = node_3
    node_2.parent = root
    node_3.parent = root
    
    node_2.left = node_4
    node_2.right = node_5
    node_4.parent = node_2
    node_5.parent = node_2
    
    node_5.right = node_6
    node_6.parent = node_5
    
    node_6.left = node_7
    node_7.parent = node_6
    
    # 测试用例
    print("测试原始版本算法:")
    
    # 测试1: 不同子树的节点
    result = lowestCommonAncestor_1650(node_4, node_7)
    print(f"节点4和节点7的最低公共祖先: {result.val} (期望: 2)")
    assert result.val == 2, f"期望2，实际{result.val}"
    
    # 测试2: 同一子树的节点
    result = lowestCommonAncestor_1650(node_5, node_6)
    print(f"节点5和节点6的最低公共祖先: {result.val} (期望: 5)")
    assert result.val == 5, f"期望5，实际{result.val}"
    
    # 测试3: 一个节点是另一个的祖先
    result = lowestCommonAncestor_1650(node_5, node_7)
    print(f"节点5和节点7的最低公共祖先: {result.val} (期望: 5)")
    assert result.val == 5, f"期望5，实际{result.val}"
    
    # 测试4: 根节点和叶子节点
    result = lowestCommonAncestor_1650(root, node_3)
    print(f"根节点和节点3的最低公共祖先: {result.val} (期望: 1)")
    assert result.val == 1, f"期望1，实际{result.val}"
    
    # 测试5: 两个叶子节点
    result = lowestCommonAncestor_1650(node_4, node_3)
    print(f"节点4和节点3的最低公共祖先: {result.val} (期望: 1)")
    assert result.val == 1, f"期望1，实际{result.val}"
    
    print("所有测试通过！")

if __name__ == "__main__":
    test_original_1650()
