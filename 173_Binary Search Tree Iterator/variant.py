class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTPreorderIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        if root:
            self.stack.append(root)  # 根节点先入栈

    def next(self) -> int:
        # 弹出栈顶节点（当前根节点）
        cur = self.stack.pop()
        val = cur.val
        
        # 前序遍历：先右后左入栈（栈是LIFO，保证左子树先被访问）
        if cur.right:
            self.stack.append(cur.right)
        if cur.left:
            self.stack.append(cur.left)
        
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0