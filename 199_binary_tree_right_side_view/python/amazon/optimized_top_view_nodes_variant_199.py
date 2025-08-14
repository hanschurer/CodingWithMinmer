from typing import Optional, Deque, defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionVariantFollowup:
    def topView(self, root: Optional[TreeNode]):
        if not root:
            return []
        
        # 存储每列的第一个节点值（key: 列号, value: 节点值）
        column_map = {}
        # 队列元素：(节点, 列号)
        queue = deque()
        queue.append((root, 0))
        
        min_col = 0  # 最小列号
        max_col = 0  # 最大列号
        
        while queue:
            node, col = queue.popleft()
            
            # 只记录每列第一个出现的节点（BFS保证先出现的节点层级更低）
            if col not in column_map:
                column_map[col] = node.val
                # 更新最小/最大列号
                min_col = min(min_col, col)
                max_col = max(max_col, col)
            
            # 左子树列号-1，右子树列号+1，入队
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        # 按列号从小到大收集结果
        result = []
        for col in range(min_col, max_col + 1):
            result.append(column_map[col])
        
        return result
