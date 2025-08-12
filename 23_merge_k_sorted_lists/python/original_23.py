import heapq
from typing import List, Optional
from ListNode import ListNode

class Solution_23:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists and return it as one sorted list.
        
        Args:
            lists: List of ListNode heads, each representing a sorted linked list
            
        Returns:
            Head of the merged sorted linked list
        """
        # Min heap to store (value, list_index, node) tuples
        min_heap = []
        
        # Initialize heap with first node from each non-empty list
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(min_heap, (head.val, i, head))
        
        # Create dummy head for result
        dummy = ListNode(-1)
        current = dummy
        
        while min_heap:
            # Get the smallest element
            val, list_index, node = heapq.heappop(min_heap)
            
            # Add to result
            current.next = node
            current = current.next
            
            # Add next node from the same list if it exists
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))
        
        return dummy.next

if __name__ == '__main__':
    # Test case 1: Merge 3 lists
    list1 = ListNode.from_list([1, 4, 5])
    list2 = ListNode.from_list([1, 3, 4])
    list3 = ListNode.from_list([2, 6])
    
    solution = Solution_23()
    result = solution.mergeKLists([list1, list2, list3])
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert result.to_list() == expected
    print("Test case 1 passed!")
    
    # Test case 2: Empty lists
    result = solution.mergeKLists([])
    assert result is None
    print("Test case 2 passed!")
    
    # Test case 3: Lists with None
    result = solution.mergeKLists([None, None])
    assert result is None
    print("Test case 3 passed!")
    
    # Test case 4: Single list
    list1 = ListNode.from_list([1, 2, 3])
    result = solution.mergeKLists([list1])
    expected = [1, 2, 3]
    assert result.to_list() == expected
    print("Test case 4 passed!")
    
    # Test case 5: Mixed empty and non-empty lists
    list1 = ListNode.from_list([1, 2])
    list2 = None
    list3 = ListNode.from_list([3, 4])
    result = solution.mergeKLists([list1, list2, list3])
    expected = [1, 2, 3, 4]
    assert result.to_list() == expected
    print("Test case 5 passed!")
    
    print("All tests passed!") 