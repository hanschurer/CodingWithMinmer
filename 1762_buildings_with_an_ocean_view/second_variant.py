def findBuildingViewCount_second_variant_1762(heights):
    n = len(heights)
    if n == 0:
        return []
    
    # 预处理左侧最大高度（不包括当前位置）
    left_max = [0] * n
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i-1])
    
    # 预处理右侧最大高度（不包括当前位置）
    right_max = [0] * n
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i+1])
    
    # 收集所有满足条件的建筑
    result = [i for i in range(n) if heights[i] > left_max[i] or heights[i] > right_max[i]]
    return result

# 测试函数保持不变
def test_findBuildingViewCount_second_variant_1762():
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([1, 2, 3, 3, 2, 1], [0, 1, 2, 3, 4, 5]),
        ([1, 4, 3, 9, 8, 6], [0, 1, 3, 4, 5]),
        ([1, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1], [0, 1, 4, 9, 10, 11]),
        ([1, 1, 1, 1], [0, 3]),
        ([5], [0]),
        ([1, 10], [0, 1])
    ]
    
    for heights, expected in test_cases:
        result = findBuildingViewCount_second_variant_1762(heights)
        assert result == expected, f"对于输入 {heights}，期望结果 {expected}，但得到 {result}"
    
    print("所有测试用例均通过！")

# 运行测试
test_findBuildingViewCount_second_variant_1762()