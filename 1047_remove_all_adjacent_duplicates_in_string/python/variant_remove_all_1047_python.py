#删除所有duplicate ex：如果有三个b 那就全部要删除 但是原题解法会遗漏第三个

def remove_all_adjacent_duplicates_variant_1047_python(s):
    stack = []

    for c in s:
        if stack and stack[-1][0]  == c:
            stack[-1][1] +=1
        else:
            while stack and stack[-1][1] > 1:
                stack.pop()
            if stack and stack[-1][0] == c:
                stack[-1][1] +=1
            else:
                stack.append([c,1])
    #只有遇到不同的元素时才会pop 所以需要手动最后检查下 例子aabbccdd
    while stack and stack[-1][1]>1:
        stack.pop()
    
    return "".join(c for c, _ in stack)

if __name__ == '__main__':
    s = "azxxxzy"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ay"

    s = "abbaxx"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabbccdd"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aaabbaad"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "d"

    s = "abcdefg"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "abcdefg"

    s = "abbcddeff"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ace"

    s = "abcdeffedcba"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabccddeeffbbbbbbbbbf"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "f"

    s = "abbbacca"; # Cannot pick and choose duplicates in the middle to delete first
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "a"
