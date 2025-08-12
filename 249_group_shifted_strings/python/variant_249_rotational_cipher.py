class Solution_249_Variant:
    def rotational_cipher(self, string: str, rotation_factor: int) -> str:
        """
        旋转密码变种：将字符串按给定因子进行右移旋转
        
        Args:
            string: 输入字符串
            rotation_factor: 旋转因子
            
        Returns:
            旋转后的字符串
        """
        if rotation_factor == 0:
            return string
        
        result = []
        for ch in string:
            if ch.islower():
                # 小写字母：a-z (97-122)
                result.append(chr((ord(ch) - ord('a') + rotation_factor) % 26 + ord('a')))
            elif ch.isupper():
                # 大写字母：A-Z (65-90)
                result.append(chr((ord(ch) - ord('A') + rotation_factor) % 26 + ord('A')))
            elif ch.isdigit():
                # 数字：0-9 (48-57)
                result.append(chr((ord(ch) - ord('0') + rotation_factor) % 10 + ord('0')))
            else:
                # 其他字符保持不变
                result.append(ch)
        
        return ''.join(result)

# 测试函数
def test_rotational_cipher():
    solution = Solution_249_Variant()
    
    # 测试用例
    test_cases = [
        # (输入字符串, 旋转因子, 期望输出)
        ("abc", 1, "bcd"),
        ("xyz", 1, "yza"),
        ("ABC", 1, "BCD"),
        ("XYZ", 1, "YZA"),
        ("123", 1, "234"),
        ("789", 1, "890"),
        ("Hello World!", 1, "Ifmmp Xpsme!"),
        ("Zebra-493?", 3, "Cheud-726?"),
        ("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39, "nopqrstuvwxyzABCDEFGHIJKLM9012345678"),
        ("All-convoYs-9-be:Alert1.", 4, "Epp-gsrzsCw-3-fi:Epivx5."),
        ("abcdZXYzxy-999.@", 200, "stuvRPQrpq-999.@"),
        ("", 5, ""),
        ("abc", 0, "abc"),
        ("abc", 26, "abc"),  # 旋转26次等于不旋转
        ("abc", 27, "bcd"),  # 旋转27次等于旋转1次
    ]
    
    for input_str, rotation, expected in test_cases:
        result = solution.rotational_cipher(input_str, rotation)
        print(f"输入: '{input_str}', 旋转因子: {rotation}")
        print(f"期望: '{expected}'")
        print(f"结果: '{result}'")
        print(f"正确: {result == expected}")
        print("-" * 50)
        
        assert result == expected, f"测试失败: 输入 '{input_str}', 旋转因子 {rotation}"
    
    print("所有测试通过!")

# 额外的实用函数
def create_rotational_cipher_table(rotation_factor: int) -> dict:
    """
    创建旋转密码对照表
    
    Args:
        rotation_factor: 旋转因子
        
    Returns:
        字符映射字典
    """
    cipher_table = {}
    
    # 小写字母映射
    for i in range(26):
        original = chr(ord('a') + i)
        shifted = chr((i + rotation_factor) % 26 + ord('a'))
        cipher_table[original] = shifted
    
    # 大写字母映射
    for i in range(26):
        original = chr(ord('A') + i)
        shifted = chr((i + rotation_factor) % 26 + ord('A'))
        cipher_table[original] = shifted
    
    # 数字映射
    for i in range(10):
        original = chr(ord('0') + i)
        shifted = chr((i + rotation_factor) % 10 + ord('0'))
        cipher_table[original] = shifted
    
    return cipher_table

def rotational_cipher_with_table(string: str, rotation_factor: int) -> str:
    """
    使用对照表的旋转密码实现（可能更高效）
    """
    if rotation_factor == 0:
        return string
    
    cipher_table = create_rotational_cipher_table(rotation_factor)
    return ''.join(cipher_table.get(ch, ch) for ch in string)

if __name__ == "__main__":
    test_rotational_cipher()
    
    # 演示对照表方法
    print("\n使用对照表方法:")
    solution = Solution_249_Variant()
    test_str = "Hello World!"
    rotation = 3
    
    result1 = solution.rotational_cipher(test_str, rotation)
    result2 = rotational_cipher_with_table(test_str, rotation)
    
    print(f"输入: '{test_str}', 旋转因子: {rotation}")
    print(f"方法1结果: '{result1}'")
    print(f"方法2结果: '{result2}'")
    print(f"结果一致: {result1 == result2}") 