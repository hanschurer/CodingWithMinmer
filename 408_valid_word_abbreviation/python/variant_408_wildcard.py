class Solution_408_Variant:
    """
    支持通配符'*'的单词缩写验证器
    
    通配符规则：
    1. '*'可以匹配任意数量的字符（包括0个）
    2. 数字表示跳过的字符数量
    3. 使用递归方法处理复杂的模式匹配
    """
    
    def _recurse(self, word: str, abbr: str, w: int, a: int) -> bool:
        """
        递归辅助函数，处理通配符匹配
        
        Args:
            word: 原单词
            abbr: 缩写
            w: 当前在单词中的位置
            a: 当前在缩写中的位置
            
        Returns:
            bool: 是否匹配
        """
        # 基本情况：都到达末尾
        if w == len(word) and a == len(abbr):
            return True
        
        # 单词结束但缩写还有剩余，检查剩余部分是否都是'*'
        if w == len(word) and a < len(abbr):
            for i in range(a, len(abbr)):
                if abbr[i] != '*':
                    return False
            return True
        
        # 缩写结束但单词还有剩余
        if w < len(word) and a == len(abbr):
            return False
        
        # 处理数字（跳过字符）
        if abbr[a].isdigit():
            skip = 0
            while a < len(abbr) and abbr[a].isdigit():
                skip = skip * 10 + (ord(abbr[a]) - ord('0'))
                a += 1
            
            w += skip
            if w > len(word):
                return False
            
            return self._recurse(word, abbr, w, a)
        
        # 处理通配符'*'
        if abbr[a] == '*':
            # '*'可以匹配0个字符（跳过）或1个字符（匹配）
            return (self._recurse(word, abbr, w, a + 1) or  # 跳过'*'
                    self._recurse(word, abbr, w + 1, a))     # 匹配一个字符
        
        # 处理普通字符匹配
        if word[w] == abbr[a]:
            return self._recurse(word, abbr, w + 1, a + 1)
        
        return False
    
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        验证支持通配符的单词缩写是否有效
        
        Args:
            word: 原单词
            abbr: 缩写（可能包含'*'）
            
        Returns:
            bool: 缩写是否有效
            
        Examples:
            >>> solution = Solution_408_Variant()
            >>> solution.validWordAbbreviation("hello", "h*lo")
            True
            >>> solution.validWordAbbreviation("hello", "h*o")
            True
        """
        return self._recurse(word, abbr, 0, 0)


# 测试代码
def test_wildcard_abbreviation():
    solution = Solution_408_Variant()
    
    # 测试用例1: 基本通配符功能
    word1, abbr1 = "hello", "h*lo"
    result1 = solution.validWordAbbreviation(word1, abbr1)
    expected1 = True
    print(f"Test 1: {result1 == expected1} - Word: '{word1}', Abbr: '{abbr1}', Expected: {expected1}, Got: {result1}")
    
    # 测试用例2: 通配符匹配多个字符
    word2, abbr2 = "hello", "h*o"
    result2 = solution.validWordAbbreviation(word2, abbr2)
    expected2 = True
    print(f"Test 2: {result2 == expected2} - Word: '{word2}', Abbr: '{abbr2}', Expected: {expected2}, Got: {result2}")
    
    # 测试用例3: 通配符匹配0个字符
    word3, abbr3 = "hello", "h*ello"
    result3 = solution.validWordAbbreviation(word3, abbr3)
    expected3 = True
    print(f"Test 3: {result3 == expected3} - Word: '{word3}', Abbr: '{abbr3}', Expected: {expected3}, Got: {result3}")
    
    # 测试用例4: 通配符在开头
    word4, abbr4 = "hello", "*ello"
    result4 = solution.validWordAbbreviation(word4, abbr4)
    expected4 = True
    print(f"Test 4: {result4 == expected4} - Word: '{word4}', Abbr: '{abbr4}', Expected: {expected4}, Got: {result4}")
    
    # 测试用例5: 通配符在结尾
    word5, abbr5 = "hello", "hell*"
    result5 = solution.validWordAbbreviation(word5, abbr5)
    expected5 = True
    print(f"Test 5: {result5 == expected5} - Word: '{word5}', Abbr: '{abbr5}', Expected: {expected5}, Got: {result5}")
    
    # 测试用例6: 多个通配符
    word6, abbr6 = "hello", "h*l*o"
    result6 = solution.validWordAbbreviation(word6, abbr6)
    expected6 = True
    print(f"Test 6: {result6 == expected6} - Word: '{word6}', Abbr: '{abbr6}', Expected: {expected6}, Got: {result6}")
    
    # 测试用例7: 通配符和数字混合
    word7, abbr7 = "hello", "h*2o"
    result7 = solution.validWordAbbreviation(word7, abbr7)
    expected7 = True
    print(f"Test 7: {result7 == expected7} - Word: '{word7}', Abbr: '{abbr7}', Expected: {expected7}, Got: {result7}")
    
    # 测试用例8: 无效匹配
    word8, abbr8 = "hello", "h*xo"
    result8 = solution.validWordAbbreviation(word8, abbr8)
    expected8 = False
    print(f"Test 8: {result8 == expected8} - Word: '{word8}', Abbr: '{abbr8}', Expected: {expected8}, Got: {result8}")
    
    # 测试用例9: 空字符串
    word9, abbr9 = "", ""
    result9 = solution.validWordAbbreviation(word9, abbr9)
    expected9 = True
    print(f"Test 9: {result9 == expected9} - Word: '{word9}', Abbr: '{abbr9}', Expected: {expected9}, Got: {result9}")
    
    # 测试用例10: 复杂模式
    word10, abbr10 = "internationalization", "i*12iz4n"
    result10 = solution.validWordAbbreviation(word10, abbr10)
    expected10 = True
    print(f"Test 10: {result10 == expected10} - Word: '{word10}', Abbr: '{abbr10}', Expected: {expected10}, Got: {result10}")


if __name__ == "__main__":
    test_wildcard_abbreviation()
