def findBuildingViewCount_variant_1762(heights):
    """
    变体版本：返回能看到海洋的建筑数量， 左边也有海
    
    算法思路：
    1. 从右向左遍历建筑高度数组
    2. 维护右侧最大高度
    3. 如果当前建筑高度大于右侧最大高度，则能看到海洋，计数加1
    4. 返回总数量
    
    时间复杂度: O(n)，其中n是建筑数量
    空间复杂度: O(1)
    """
    n = len(heights)
    if n == 0:
        return 0
    
    count = 1  # 最右边的建筑一定能看到海洋
    right_max = heights[n - 1]
    
    # 从右向左遍历
    for i in range(n - 2, -1, -1):
        if heights[i] > right_max:
            count += 1
            right_max = heights[i]
    
    return count

def test_findBuildingViewCount_variant_1762():
    """测试第一变体版本的算法"""
    print("测试第一变体版本算法:")
    
    # 测试用例1: 基本测试
    heights = [4, 2, 3, 1]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 3
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例2: 复杂情况
    heights = [6, 1, 2, 4, 2, 2, 2, 2, 3, 1]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 4
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例3: 递减序列
    heights = [4, 3, 2, 1]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 4
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例4: 递增序列
    heights = [1, 3, 2, 4]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 1
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例5: 相同高度
    heights = [2, 2, 2, 2, 2, 2, 2]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 1
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例6: 山峰形状
    heights = [0, 1, 2, 3, 2, 1, 0]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 4
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例7: 递增序列
    heights = [1, 2, 3, 4]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 1
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例8: 单个建筑
    heights = [10]
    result = findBuildingViewCount_variant_1762(heights)
    expected = 1
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    print("所有测试通过！")

if __name__ == "__main__":
    test_findBuildingViewCount_variant_1762()
