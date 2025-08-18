from typing import Optional
#find the cloest node 
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.top = None
        self.bottom = None

class SkipList:
    def search_closest(self, root: Optional['Node'], target: int) -> Optional['Node']:
        if root is None:
            return None
        if root.val == target:
            return root

        c = root
        #改成bottom
        while c.bottom is not None:
            while c.next is not None and c.next.val <= target:
                c = c.next
                if c.val == target:
                    return c
            c = c.bottom
        #加一行这个
        while c.next is not None and c.next.val <= target:
            c = c.next
        return c