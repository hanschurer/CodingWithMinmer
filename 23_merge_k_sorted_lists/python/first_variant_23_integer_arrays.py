import heapq
from typing import List

class Solution_23_First_Variant:
    def mergeKLists(self, lists: List[List[int]]) -> List[int]:
        """
        Merge k sorted integer arrays and return it as one sorted array.
        
        Args:
            lists: List of sorted integer arrays
            
        Returns:
            Merged sorted array
        """
        # Min heap to store (value, list_index, element_index) tuples
        min_heap = []
        
        # Initialize heap with first element from each non-empty list
        for i, arr in enumerate(lists):
            if arr:  # Check if list is not empty
                heapq.heappush(min_heap, (arr[0], i, 0))
        
        result = []
        
        while min_heap:
            # Get the smallest element
            val, list_index, element_index = heapq.heappop(min_heap)
            
            # Add to result
            result.append(val)
            
            # Add next element from the same list if it exists
            element_index += 1
            if element_index < len(lists[list_index]):
                heapq.heappush(min_heap, (lists[list_index][element_index], list_index, element_index))
        
        return result

if __name__ == '__main__':
    # Test case 1: Merge 3 arrays
    lists = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]
    solution = Solution_23_First_Variant()
    result = solution.mergeKLists(lists)
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert result == expected
    print("Test case 1 passed!")
    
    # Test case 2: Empty lists
    result = solution.mergeKLists([])
    expected = []
    assert result == expected
    print("Test case 2 passed!")
    
    # Test case 3: Lists with empty arrays
    lists = [[], [1, 2], []]
    result = solution.mergeKLists(lists)
    expected = [1, 2]
    assert result == expected
    print("Test case 3 passed!")
    
    # Test case 4: Single list
    lists = [[1, 2, 3]]
    result = solution.mergeKLists(lists)
    expected = [1, 2, 3]
    assert result == expected
    print("Test case 4 passed!")
    
    # Test case 5: All empty lists
    lists = [[], [], []]
    result = solution.mergeKLists(lists)
    expected = []
    assert result == expected
    print("Test case 5 passed!")
    
    # Test case 6: Large numbers
    lists = [
        [1, 100, 1000],
        [2, 200, 2000],
        [3, 300, 3000]
    ]
    result = solution.mergeKLists(lists)
    expected = [1, 2, 3, 100, 200, 300, 1000, 2000, 3000]
    assert result == expected
    print("Test case 6 passed!")
    
    print("All tests passed!") 