from collections import deque
from typing import List

def find_anti_diagonal_order_1424_first_variant(nums: List[List[int]]) -> List[List[int]]:
    """
    反对角线遍历变种：返回反对角线遍历的列表
    
    Args:
        nums: 二维整数数组
        
    Returns:
        反对角线遍历的结果列表，每个子列表代表一条反对角线
    """
    if not nums or not nums[0]:
        return []
    
    result = []
    q = deque([(0, 0)])  # 使用deque替代queue
    
    while q:
        size = len(q)
        curr_level = []
        
        for _ in range(size):
            row, col = q.popleft()
            curr_level.append(nums[row][col])
            
            # 添加右邻居（如果存在）
            if col + 1 < len(nums[row]):
                q.append((row, col + 1))
            
            # 添加下邻居（如果当前是行的第一个元素且存在下一行）
            if col == 0 and row + 1 < len(nums):
                q.append((row + 1, col))
        
        result.append(curr_level)
    
    return result

# 测试函数
def test_anti_diagonal_traversal():
    # 测试用例
    test_cases = [
        # 测试用例1：3x3矩阵
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]], 
         [[1], [2, 4], [3, 5, 7], [6, 8], [9]]),
        
        # 测试用例2：2x3矩阵
        ([[1, 2, 3],
          [4, 5, 6]], 
         [[1], [2, 4], [3, 5], [6]]),
        
        # 测试用例3：3x2矩阵
        ([[1, 2],
          [3, 4],
          [5, 6]], 
         [[1], [2, 3], [4, 5], [6]]),
        
        # 测试用例4：1x1矩阵
        ([[1]], [[1]]),
        
        # 测试用例5：空矩阵
        ([], []),
        
        # 测试用例6：不规则矩阵
        ([[1, 2, 3],
          [4, 5],
          [6, 7, 8, 9]], 
         [[1], [2, 4], [3, 5, 6], [7, 8], [9]]),
    ]
    
    for i, (input_matrix, expected) in enumerate(test_cases, 1):
        result = find_anti_diagonal_order_1424_first_variant(input_matrix)
        print(f"测试用例 {i}:")
        print(f"输入矩阵:")
        for row in input_matrix:
            print(f"  {row}")
        print(f"期望结果: {expected}")
        print(f"实际结果: {result}")
        print(f"正确: {result == expected}")
        print("-" * 50)
        
        assert result == expected, f"测试用例 {i} 失败"
    
    print("所有测试通过!")

# 可视化函数
def print_matrix_with_anti_diagonals(matrix: List[List[int]]):
    """
    可视化矩阵的反对角线遍历
    """
    if not matrix:
        print("空矩阵")
        return
    
    print("矩阵:")
    for row in matrix:
        print(f"  {row}")
    
    result = find_anti_diagonal_order_1424_first_variant(matrix)
    print("\n反对角线遍历结果:")
    for i, diagonal in enumerate(result):
        print(f"  反对角线 {i}: {diagonal}")

# 更直观的实现（不使用队列）
def find_anti_diagonal_order_alternative(nums: List[List[int]]) -> List[List[int]]:
    """
    替代实现：直接计算反对角线
    优点：更直观，易于理解
    """
    if not nums or not nums[0]:
        return []
    
    rows, cols = len(nums), len(nums[0])
    result = []
    
    # 遍历所有可能的反对角线
    for sum_val in range(rows + cols - 1):
        diagonal = []
        # 对于每个和值，找到所有满足 row + col = sum_val 的位置
        for row in range(max(0, sum_val - cols + 1), min(rows, sum_val + 1)):
            col = sum_val - row
            if col < len(nums[row]):  # 确保列索引有效
                diagonal.append(nums[row][col])
        result.append(diagonal)
    
    return result

if __name__ == "__main__":
    # 运行测试
    test_anti_diagonal_traversal()
    
    # 演示可视化
    print("\n可视化演示:")
    demo_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_with_anti_diagonals(demo_matrix)
    
    # 比较两种实现
    print("\n比较两种实现:")
    result1 = find_anti_diagonal_order_1424_first_variant(demo_matrix)
    result2 = find_anti_diagonal_order_alternative(demo_matrix)
    print(f"队列实现: {result1}")
    print(f"直接计算: {result2}")
    print(f"结果一致: {result1 == result2}") 