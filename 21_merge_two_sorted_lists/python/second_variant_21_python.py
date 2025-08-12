from typing import List
#merge 3 sorted Lists without duplicate
def merge_3_sorted_lists_second_variant_21(listA: List[int], 
                                           listB: List[int], 
                                           listC: List[int]) -> List[int]:
    """
    Merge 3 sorted lists without duplicates.
    Returns a sorted list with unique elements from all three input lists.
    """
    result = []
    a = b = c = 0
    last_added = None  # Track the last added value to avoid duplicates
    
    while a < len(listA) or b < len(listB) or c < len(listC):
        # Get current values from each list, use inf as sentinel
        a_val = listA[a] if a < len(listA) else float('inf')
        b_val = listB[b] if b < len(listB) else float('inf')
        c_val = listC[c] if c < len(listC) else float('inf')
        
        # Find minimum value
        min_val = min(a_val, b_val, c_val)
        
        # Add to result only if it's different from last added value
        if last_added != min_val:
            result.append(min_val)
            last_added = min_val
        
        # Advance pointer for the list that contributed the minimum value
        if a_val == min_val:
            a += 1
        elif b_val == min_val:
            b += 1
        else:  # c_val == min_val
            c += 1
    
    return result

if __name__ == '__main__':
    a = [1, 1, 1, 3, 4, 5]
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 3, 4, 5, 6, 8, 10]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = []
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 3, 4, 5, 6, 8, 10]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = []
    b = []
    c = []
    expected = []
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = [1]
    b = [2]
    c = [3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 3]
    expected = [1, 2, 3]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)

    a = [2, 2]
    b = [2]
    c = [0]
    expected = [0, 2]
    assert expected == merge_3_sorted_lists_second_variant_21(a, b, c)
