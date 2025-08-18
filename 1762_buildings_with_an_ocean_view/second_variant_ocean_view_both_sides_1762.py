def findBuildingViewCount_second_variant_1762(heights):
    """
    第二变体版本：找到所有在左侧或右侧能看到海洋的建筑
    
    算法思路：
    1. 使用双指针技巧，从两端向中间遍历
    2. 维护左侧和右侧的最大高度
    3. 比较左右两侧的最大高度，选择较小的一侧进行扩展
    4. 如果当前建筑高度大于对应侧的最大高度，则能看到海洋
    5. 最后合并左右两侧的结果
    
    时间复杂度: O(n)，其中n是建筑数量
    空间复杂度: O(n)，用于存储结果
    """
    n = len(heights)
    if n == 1:
        return [0]
    
    left = 0
    right = n - 1
    left_view = [left]  # 最左边的建筑一定能看到海洋
    right_view = [right]  # 最右边的建筑一定能看到海洋
    
    left_max = heights[left]
    right_max = heights[right]
    
    while left < right:
        if left_max < right_max:
            left += 1
            if left < right and heights[left] > left_max:
                left_view.append(left)
                left_max = heights[left]
        else:
            right -= 1
            if left < right and heights[right] > right_max:
                right_view.append(right)
                right_max = heights[right]
    
    # 合并左右两侧的结果，右侧结果需要反转
    left_view.extend(reversed(right_view))
    return left_view

def test_findBuildingViewCount_second_variant_1762():
    """测试第二变体版本的算法"""
    print("测试第二变体版本算法:")
    
    # 测试用例1: 递增序列
    heights = [1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 2]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例2: 对称序列
    heights = [1, 2, 3, 3, 2, 1]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 1, 2, 3, 4, 5]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例3: 复杂情况
    heights = [1, 4, 3, 9, 8, 6]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 1, 3, 4, 5]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例4: 更多复杂情况
    heights = [1, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 1, 4, 9, 10, 11]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例5: 相同高度
    heights = [1, 1, 1, 1]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 3]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例6: 单个建筑
    heights = [5]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例7: 两个建筑
    heights = [1, 10]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 1]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    print("所有测试通过！")

def test_edge_cases():
    """测试边界情况"""
    print("\n测试边界情况:")
    
    # 测试1: 空数组
    heights = []
    try:
        result = findBuildingViewCount_second_variant_1762(heights)
        print("空数组测试失败：应该抛出异常")
    except:
        print("空数组测试通过：正确抛出异常")
    
    # 测试2: 线性递增
    heights = [1, 2, 3, 4, 5]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [4]
    print(f"线性递增: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试3: 线性递减
    heights = [5, 4, 3, 2, 1]
    result = findBuildingViewCount_second_variant_1762(heights)
    expected = [0, 1, 2, 3, 4]
    print(f"线性递减: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    print("所有边界情况测试通过！")

if __name__ == "__main__":
    test_findBuildingViewCount_second_variant_1762()
    test_edge_cases()
