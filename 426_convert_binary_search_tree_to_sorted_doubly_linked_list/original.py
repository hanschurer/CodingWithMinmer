"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return 
        self.head = self.pre = None

        def dfs(root):

            if not root: return 

            dfs(root.left)

            if not self.head:
                self.head = root
            else:
                self.pre.right, root.left = root, self.pre
            
            self.pre = root


            dfs(root.right)
        
       

        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
        