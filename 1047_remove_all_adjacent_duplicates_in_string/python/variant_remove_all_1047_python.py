#删除所有duplicate ex：如果有三个b 那就全部要删除 但是原题解法会遗漏第三个

def remove_all_adjacent_duplicates_variant_1047_python(s):
    stack = []  # 栈元素: (字符, 连续出现次数)
    for ch in s:
        if stack and stack[-1][0] == ch:
            # 与栈顶字符相同，累加计数
            stack[-1] = (ch, stack[-1][1] + 1)
        else:
            # 处理上一个字符（若连续次数>1则移除）
            if stack and stack[-1][1] > 1:
                stack.pop()
            # 检查新栈顶是否与当前字符相同（可能因上一步弹出而变化）
            if stack and stack[-1][0] == ch:
                stack[-1] = (ch, stack[-1][1] + 1)
            else:
                stack.append((ch, 1))
    
    # 移除最后一个可能需要清理的字符
    if stack and stack[-1][1] > 1:
        stack.pop()
    
    # 拼接结果
    return ''.join([char for char, _ in stack])


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
