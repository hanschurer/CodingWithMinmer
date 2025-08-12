from typing import List, Dict, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph:
    def __init__(self, roots: Optional[List[Node]] = None):
        self.roots = roots if roots is not None else []

def dfs_133_variant(node: Node, old_to_new: Dict[Node, Node]) -> Node:
    """
    深度优先搜索克隆图的变种版本
    处理可能断开的图结构
    """
    if node in old_to_new:
        return old_to_new[node]
    
    # 创建新节点
    old_to_new[node] = Node(node.val)
    
    # 递归克隆所有邻居
    for neighbor in node.neighbors:
        old_to_new[node].neighbors.append(
            dfs_133_variant(neighbor, old_to_new)
        )
    
    return old_to_new[node]

def clone_graph_133_first_variant(input_graph: Graph) -> Graph:
    """
    克隆图的变种版本
    处理可能包含多个根节点的断开图
    """
    output = Graph()
    
    for node in input_graph.roots:
        if node is None:
            continue
        
        # 为每个根节点创建新的映射表
        old_to_new = {}
        output.roots.append(dfs_133_variant(node, old_to_new))
    
    return output

# 测试函数
def test_clone_graph_variant():
    # 创建测试图
    # 图1: 1 -- 2
    #      |    |
    #      4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    # 图2: 5 -- 6
    node5 = Node(5)
    node6 = Node(6)
    node5.neighbors = [node6]
    node6.neighbors = [node5]
    
    # 创建输入图（包含两个断开的子图）
    input_graph = Graph([node1, node5])
    
    # 克隆图
    output_graph = clone_graph_133_first_variant(input_graph)
    
    # 验证结果
    print("原始图的根节点数量:", len(input_graph.roots))
    print("克隆图的根节点数量:", len(output_graph.roots))
    
    for i, root in enumerate(output_graph.roots):
        print(f"克隆图根节点 {i}: 值={root.val}, 邻居数量={len(root.neighbors)}")
        for neighbor in root.neighbors:
            print(f"  - 邻居: 值={neighbor.val}, 邻居数量={len(neighbor.neighbors)}")
    
    # 验证克隆是否成功（地址不同）
    print(f"\n原始节点1地址: {id(node1)}")
    print(f"克隆节点1地址: {id(output_graph.roots[0])}")
    print("克隆成功!" if id(node1) != id(output_graph.roots[0]) else "克隆失败!")

if __name__ == "__main__":
    test_clone_graph_variant() 