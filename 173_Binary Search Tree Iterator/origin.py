# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self._started = False

    def _pushLeft(self, node):
        """Helper method to push all left path nodes to stack"""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration("No more elements")
        
        # If this is the first call, start filling the stack
        if not self._started:
            self._pushLeft(self.root)
            self._started = True
        
        cur = self.stack.pop()
        
        # Push left path of right subtree if exists
        if cur.right:
            self._pushLeft(cur.right)
        
        return cur.val

    def hasNext(self) -> bool:
        # If not started, check if root exists
        if not self._started:
            return self.root is not None
        # If started, check if stack has elements
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()