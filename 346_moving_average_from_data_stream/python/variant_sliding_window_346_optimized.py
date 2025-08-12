from collections import deque
from typing import List

def compute_running_sum_variant_346_deque(nums: List[int], size: int) -> List[int]:
    """
    使用deque的滑动窗口版本
    优点：更直观，易于理解
    """
    if size <= 0 or not nums:
        return []
    
    result = []
    window = deque()
    window_sum = 0
    
    for num in nums:
        window.append(num)
        window_sum += num
        
        if len(window) > size:
            window_sum -= window.popleft()
        
        if len(window) == size:
            result.append(window_sum // size)
    
    return result

def compute_running_sum_variant_346_concise(nums: List[int], size: int) -> List[int]:
    """
    更简洁的版本，减少变量使用
    """
    if size <= 0 or not nums:
        return []
    
    result = []
    window_sum = sum(nums[:size])
    result.append(window_sum // size)
    
    for i in range(size, len(nums)):
        window_sum = window_sum - nums[i - size] + nums[i]
        result.append(window_sum // size)
    
    return result

def compute_running_sum_variant_346_itertools(nums: List[int], size: int) -> List[int]:
    """
    使用itertools的优雅版本
    """
    from itertools import islice
    
    if size <= 0 or not nums:
        return []
    
    result = []
    window_sum = sum(nums[:size])
    result.append(window_sum // size)
    
    for i in range(size, len(nums)):
        window_sum += nums[i] - nums[i - size]
        result.append(window_sum // size)
    
    return result

# 测试函数
def test_sliding_window_variants():
    test_cases = [
        ([1, 2, 3, 4, 5], 3, [2, 3, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [2, 3, 4, 5, 6]),
        ([1, 1, 1, 1, 1], 2, [1, 1, 1, 1]),
        ([1, 2, 3], 5, []),  # 窗口大于数组长度
        ([], 3, []),  # 空数组
        ([1, 2, 3, 4], 1, [1, 2, 3, 4]),  # 窗口大小为1
    ]
    
    functions = [
        compute_running_sum_variant_346_deque,
        compute_running_sum_variant_346_concise,
        compute_running_sum_variant_346_itertools
    ]
    
    for func in functions:
        print(f"\n测试函数: {func.__name__}")
        for nums, size, expected in test_cases:
            result = func(nums, size)
            print(f"输入: {nums}, 窗口大小: {size} -> 输出: {result}")
            assert result == expected, f"期望 {expected}, 得到 {result}"
        print("所有测试通过!")

if __name__ == "__main__":
    test_sliding_window_variants() 