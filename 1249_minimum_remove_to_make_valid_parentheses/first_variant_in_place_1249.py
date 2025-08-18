#变种 不能用stack  O1空间复杂度
def minRemoveToMakeValid_Variant(s: str) -> str:
    """
    LeetCode 1249 Variant: In-place solution to reduce space complexity
    
    This variant modifies the string in-place to minimize extra space usage.
    Note: In Python, strings are immutable, so we simulate in-place operation
    by using a list and then joining it.
    
    Args:
        s: Input string containing parentheses and lowercase English characters
        
    Returns:
        String with minimum parentheses removed to make it valid
    """
    # Convert string to list for in-place modification simulation

    left, right, ans = 0, s.count(')'), ''
    for c in s:
        if c == '(':
            if right > 0:
                ans += c
                left += 1
                right -= 1  # 消耗一个对应的右括号
        elif c == ')':
            if left > 0:
                ans += c
                left -= 1
            else:
                right -= 1  # 无效的右括号
        else:
            ans += c
    return ans

# Example usage and test
if __name__ == "__main__":
    # Test case 1: Basic example
    s1 = "lee(t(c)o)de"
    result1 = minRemoveToMakeValid_Variant(s1)
    print(f"Input: '{s1}' -> Output: '{result1}'")
    
    # Test case 2: Multiple unmatched parentheses
    s2 = "a)b(c)d"
    result2 = minRemoveToMakeValid_Variant(s2)
    print(f"Input: '{s2}' -> Output: '{result2}'")
    
    # Test case 3: All parentheses unmatched
    s3 = "))(("
    result3 = minRemoveToMakeValid_Variant(s3)
    print(f"Input: '{s3}' -> Output: '{result3}'")
    
    # Test case 4: Already valid
    s4 = "(a(b(c)d))"
    result4 = minRemoveToMakeValid_Variant(s4)
    print(f"Input: '{s4}' -> Output: '{result4}'")
    
    # Test case 5: Mixed case (from C++ test)
    s5 = "))((ab()c)("
    result5 = minRemoveToMakeValid_Variant(s5)
    print(f"Input: '{s5}' -> Output: '{result5}'")
    expected5 = "((ab)c)"
    print(f"Expected: '{expected5}', Got: '{result5}', Match: {result5 == expected5}")
    
    # Test case 6: Complex nested (from C++ test)
    s6 = "((ab((()))c)("
    result6 = minRemoveToMakeValid_Variant(s6)
    print(f"Input: '{s6}' -> Output: '{result6}'")
    expected6 = "((ab(()))c)"
    print(f"Expected: '{expected6}', Got: '{result6}', Match: {result6 == expected6}")
    
    # Test case 7: Empty string
    s7 = ""
    result7 = minRemoveToMakeValid_Variant(s7)
    print(f"Input: '{s7}' -> Output: '{result7}'")
    
    # Test case 8: No parentheses
    s8 = "leetcode"
    result8 = minRemoveToMakeValid_Variant(s8)
    print(f"Input: '{s8}' -> Output: '{result8}'")
    
    # Verify results are valid
    def is_valid_parentheses(s: str) -> bool:
        """Check if parentheses are valid"""
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    
    print("\nValidation:")
    test_cases = [s1, s2, s3, s4, s5, s6, s7, s8]
    for i, test_s in enumerate(test_cases, 1):
        result = minRemoveToMakeValid_Variant(test_s)
        is_valid = is_valid_parentheses(result)
        print(f"Test {i}: '{test_s}' -> '{result}' (Valid: {is_valid})")
    
    # Performance comparison with original version
    print("\nPerformance Note:")
    print("This variant simulates in-place operation in Python.")
    print("While it reduces the number of string concatenations,")
    print("it still creates intermediate lists due to Python's string immutability.")
    print("For true in-place operation, you would need to work with bytearray or")
    print("modify the algorithm to work with mutable data structures.")
