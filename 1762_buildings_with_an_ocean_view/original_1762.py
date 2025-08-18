def findBuildings(heights):
    """
    找到所有能看到海洋的建筑索引
    
    算法思路：
    1. 从右向左遍历建筑高度数组
    2. 维护右侧最大高度
    3. 如果当前建筑高度大于右侧最大高度，则能看到海洋
    4. 最后反转结果数组，保持从左到右的顺序
    
    时间复杂度: O(n)，其中n是建筑数量
    空间复杂度: O(k)，其中k是能看到海洋的建筑数量
    """
    n = len(heights)
    if n == 0:
        return []
    
    right_view = [n - 1]  # 最右边的建筑一定能看到海洋
    right_max = heights[n - 1]
    
    # 从右向左遍历
    for i in range(n - 2, -1, -1):
        if heights[i] > right_max:
            right_view.append(i)
            right_max = heights[i]
    
    # 反转结果，保持从左到右的顺序
    right_view.reverse()
    return right_view

def test_original_1762():
    """测试原始版本的算法"""
    print("测试原始版本算法:")
    
    # 测试用例1: 基本测试
    heights = [4, 2, 3, 1]
    result = findBuildings(heights)
    expected = [0, 2, 3]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例2: 递增序列
    heights = [1, 2, 3, 4]
    result = findBuildings(heights)
    expected = [3]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例3: 递减序列
    heights = [4, 3, 2, 1]
    result = findBuildings(heights)
    expected = [0, 1, 2, 3]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例4: 相同高度
    heights = [2, 2, 2, 2]
    result = findBuildings(heights)
    expected = [3]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例5: 单个建筑
    heights = [5]
    result = findBuildings(heights)
    expected = [0]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    # 测试用例6: 复杂情况
    heights = [6, 1, 2, 4, 2, 2, 2, 2, 3, 1]
    result = findBuildings(heights)
    expected = [0, 2, 3, 8]
    print(f"输入: {heights}, 结果: {result}, 期望: {expected}")
    assert result == expected, f"期望{expected}，实际{result}"
    
    print("所有测试通过！")

if __name__ == "__main__":
    test_original_1762()
