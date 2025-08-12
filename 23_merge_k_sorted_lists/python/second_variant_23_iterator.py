import heapq
from typing import List

class Solution_23_Second_Variant:
    """
    Iterator class for merging K sorted integer arrays.
    Provides hasNext() and next() methods similar to Java Iterator.
    """
    
    def __init__(self, lists: List[List[int]]):
        """
        Initialize the iterator with K sorted integer arrays.
        
        Args:
            lists: List of sorted integer arrays
        """
        self.lists = lists
        self.min_heap = []
        
        # Initialize heap with first element from each non-empty list
        for i, arr in enumerate(lists):
            if arr:  # Check if list is not empty
                heapq.heappush(self.min_heap, (arr[0], i, 0))
    
    def hasNext(self) -> bool:
        """
        Check if there are more elements to iterate over.
        
        Returns:
            True if there are more elements, False otherwise
        """
        return len(self.min_heap) > 0
    
    def next(self) -> int:
        """
        Get the next smallest element from the merged lists.
        
        Returns:
            The next smallest integer
            
        Raises:
            StopIteration: If no more elements are available
        """
        if not self.hasNext():
            raise StopIteration("No more elements left")
        
        # Get the smallest element
        val, list_index, element_index = heapq.heappop(self.min_heap)
        
        # Add next element from the same list if it exists
        element_index += 1
        if element_index < len(self.lists[list_index]):
            heapq.heappush(self.min_heap, (self.lists[list_index][element_index], list_index, element_index))
        
        return val
    
    def __iter__(self):
        """Make the class iterable."""
        return self
    
    def __next__(self):
        """Python iterator protocol."""
        return self.next()

if __name__ == '__main__':
    # Test case 1: Basic iteration
    lists = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]
    iterator = Solution_23_Second_Variant(lists)
    
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert result == expected
    print("Test case 1 passed!")
    
    # Test case 2: Python iterator protocol
    lists = [
        [1, 3],
        [2, 4]
    ]
    iterator = Solution_23_Second_Variant(lists)
    
    result = list(iterator)  # Using Python iterator protocol
    expected = [1, 2, 3, 4]
    assert result == expected
    print("Test case 2 passed!")
    
    # Test case 3: Empty lists
    iterator = Solution_23_Second_Variant([])
    assert not iterator.hasNext()
    print("Test case 3 passed!")
    
    # Test case 4: Lists with empty arrays
    lists = [[], [1, 2], []]
    iterator = Solution_23_Second_Variant(lists)
    
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    
    expected = [1, 2]
    assert result == expected
    print("Test case 4 passed!")
    
    # Test case 5: Exception handling
    lists = [[1]]
    iterator = Solution_23_Second_Variant(lists)
    
    # Get the first element
    assert iterator.next() == 1
    
    # Should raise StopIteration
    try:
        iterator.next()
        assert False, "Should have raised StopIteration"
    except StopIteration:
        print("Test case 5 passed!")
    
    # Test case 6: Large dataset
    lists = [
        [1, 100, 1000],
        [2, 200, 2000],
        [3, 300, 3000]
    ]
    iterator = Solution_23_Second_Variant(lists)
    
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    
    expected = [1, 2, 3, 100, 200, 300, 1000, 2000, 3000]
    assert result == expected
    print("Test case 6 passed!")
    
    print("All tests passed!") 