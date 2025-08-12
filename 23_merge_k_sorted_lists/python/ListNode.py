from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None, random: Optional['ListNode'] = None):
        self.val = val
        self.next = next
        self.random = random
    
    def __str__(self):
        return f"ListNode({self.val})"
    
    def __repr__(self):
        return self.__str__()
    
    @classmethod
    def from_list(cls, values: list[int]) -> Optional['ListNode']:
        """Create a linked list from a list of values."""
        if not values:
            return None
        
        head = cls(values[0])
        current = head
        for val in values[1:]:
            current.next = cls(val)
            current = current.next
        
        return head
    
    def to_list(self) -> list[int]:
        """Convert linked list to a list of values."""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result 