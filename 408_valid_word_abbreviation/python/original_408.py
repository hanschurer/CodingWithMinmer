def validWordAbbreviation(word: str, abbr: str) -> bool:
    idx = num = 0
    for i, v in enumerate(abbr):
        if v == "0" and num == 0:
            return False
        if v.isdigit():
            num = num*10+int(v)
        else:
            idx+=num
            num = 0
            if idx >=len(word) or  word[idx] != v:
                return False
            
            idx+=1
    
    idx +=num
    return len(word ) == idx



# 测试代码
def test_valid_word_abbreviation():
    # 测试用例1: 基本功能
    word1, abbr1 = "internationalization", "i12iz4n"
    result1 = validWordAbbreviation(word1, abbr1)
    expected1 = True
    print(f"Test 1: {result1 == expected1} - Word: '{word1}', Abbr: '{abbr1}', Expected: {expected1}, Got: {result1}")
    
    # 测试用例2: 简单缩写
    word2, abbr2 = "apple", "a2le"
    result2 = validWordAbbreviation(word2, abbr2)
    expected2 = True
    print(f"Test 2: {result2 == expected2} - Word: '{word2}', Abbr: '{abbr2}', Expected: {expected2}, Got: {result2}")
    

    # 测试用例4: 完全匹配
    word4, abbr4 = "hello", "hello"
    result4 = validWordAbbreviation(word4, abbr4)
    expected4 = True
    print(f"Test 4: {result4 == expected4} - Word: '{word4}', Abbr: '{abbr4}', Expected: {expected4}, Got: {result4}")
    
    # 测试用例5: 数字在开头
    word5, abbr5 = "hello", "5"
    result5 = validWordAbbreviation(word5, abbr5)
    expected5 = True
    print(f"Test 5: {result5 == expected5} - Word: '{word5}', Abbr: '{abbr5}', Expected: {expected5}, Got: {result5}")
    
    # 测试用例6: 数字在结尾
    word6, abbr6 = "hello", "h4"
    result6 = validWordAbbreviation(word6, abbr6)
    expected6 = True
    print(f"Test 6: {result6 == expected6} - Word: '{word6}', Abbr: '{abbr6}', Expected: {expected6}, Got: {result6}")
    
    # 测试用例7: 无效缩写（长度不匹配）
    word7, abbr7 = "hello", "h3"
    result7 = validWordAbbreviation(word7, abbr7)
    expected7 = False
    print(f"Test 7: {result7 == expected7} - Word: '{word7}', Abbr: '{abbr7}', Expected: {expected7}, Got: {result7}")

    



if __name__ == "__main__":
    test_valid_word_abbreviation()
