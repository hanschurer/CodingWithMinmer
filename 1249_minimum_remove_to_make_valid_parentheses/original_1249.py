def minRemoveToMakeValid(s: str) -> str:
    """
    LeetCode 1249: Minimum Remove to Make Valid Parentheses
    
    Given a string s of '(' , ')' and lowercase English characters.
    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
    so that the resulting parentheses string is valid and return any valid string.
    
    Args:
        s: Input string containing parentheses and lowercase English characters
        
    Returns:
        String with minimum parentheses removed to make it valid
    """
    extra_opens = 0
    total_opens = 0
    temp = []
    
    # First pass: handle closing parentheses
    for ch in s:
        if ch == ')':
            if extra_opens == 0:
                continue  # Skip unmatched closing parenthesis
            extra_opens -= 1
            temp.append(ch)
        elif ch == '(':
            total_opens += 1
            extra_opens += 1
            temp.append(ch)
        else:
            temp.append(ch)
    
    # Second pass: handle opening parentheses
    result = []
    keep = total_opens - extra_opens
    for ch in temp:
        if ch == '(':
            if keep == 0:
                continue  # Skip excess opening parentheses
            result.append(ch)
            keep -= 1
        else:
            result.append(ch)
    
    return ''.join(result)


# Example usage and test
if __name__ == "__main__":
    # Test case 1: Basic example
    s1 = "lee(t(c)o)de"
    result1 = minRemoveToMakeValid(s1)
    print(f"Input: '{s1}' -> Output: '{result1}'")
    
    # Test case 2: Multiple unmatched parentheses
    s2 = "a)b(c)d"
    result2 = minRemoveToMakeValid(s2)
    print(f"Input: '{s2}' -> Output: '{result2}'")
    
    # Test case 3: All parentheses unmatched
    s3 = "))(("
    result3 = minRemoveToMakeValid(s3)
    print(f"Input: '{s3}' -> Output: '{result3}'")
    
    # Test case 4: Already valid
    s4 = "(a(b(c)d))"
    result4 = minRemoveToMakeValid(s4)
    print(f"Input: '{s4}' -> Output: '{result4}'")
    
    # Test case 5: Mixed case
    s5 = "))((ab()c)("
    result5 = minRemoveToMakeValid(s5)
    print(f"Input: '{s5}' -> Output: '{result5}'")
    
    # Test case 6: Complex nested
    s6 = "((ab((()))c)("
    result6 = minRemoveToMakeValid(s6)
    print(f"Input: '{s6}' -> Output: '{result6}'")
    
    # Test case 7: Empty string
    s7 = ""
    result7 = minRemoveToMakeValid(s7)
    print(f"Input: '{s7}' -> Output: '{result7}'")
    
    # Test case 8: No parentheses
    s8 = "leetcode"
    result8 = minRemoveToMakeValid(s8)
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
        result = minRemoveToMakeValid(test_s)
        is_valid = is_valid_parentheses(result)
        print(f"Test {i}: '{test_s}' -> '{result}' (Valid: {is_valid})")
