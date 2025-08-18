from typing import List

def move_zeroes_to_front(nums: List[int]) -> None:
    """
    将数组中的所有0移动到前面，同时保持非零元素的相对顺序
    
    Args:
        nums: 输入数组，将被原地修改
        
    Example:
        >>> nums = [1,3,12,0,0,0]
        >>> move_zeroes_to_front(nums)
        >>> print(nums)
        [0, 0, 0, 1, 3, 12]
    """
    if not nums:
        return
    
    # 双指针技术：从后往前遍历，swap_index指向下一个非零元素应该放置的位置
    swap_index = len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            # 交换当前非零元素到swap_index位置
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index -= 1


# 测试代码
def test_move_zeroes_to_front():
    # 测试用例1: 基本功能
    nums1 = [1, 3, 12, 0, 0, 0]
    expected1 = [0, 0, 0, 1, 3, 12]
    move_zeroes_to_front(nums1)
    print(f"Test 1: {nums1 == expected1} - Expected: {expected1}, Got: {nums1}")
    
    # 测试用例2: 零分散分布
    nums2 = [0, 1, 0, 3, 12, 0]
    expected2 = [0, 0, 0, 1, 3, 12]
    move_zeroes_to_front(nums2)
    print(f"Test 2: {nums2 == expected2} - Expected: {expected2}, Got: {nums2}")
    
    # 测试用例3: 很多零
    nums3 = [1, 3, 12, 0, 0, 0, 0, 0, 0]
    expected3 = [0, 0, 0, 0, 0, 0, 1, 3, 12]
    move_zeroes_to_front(nums3)
    print(f"Test 3: {nums3 == expected3} - Expected: {expected3}, Got: {nums3}")
    
    # 测试用例4: 空数组
    nums4 = []
    expected4 = []
    move_zeroes_to_front(nums4)
    print(f"Test 4: {nums4 == expected4} - Expected: {expected4}, Got: {nums4}")
    
    # 测试用例5: 只有一个零
    nums5 = [0]
    expected5 = [0]
    move_zeroes_to_front(nums5)
    print(f"Test 5: {nums5 == expected5} - Expected: {expected5}, Got: {nums5}")
    
    # 测试用例6: 全是零
    nums6 = [0, 0, 0]
    expected6 = [0, 0, 0]
    move_zeroes_to_front(nums6)
    print(f"Test 6: {nums6 == expected6} - Expected: {expected6}, Got: {nums6}")
    
    # 测试用例7: 零和非零混合
    nums7 = [1, 0, 3, 0, 12]
    expected7 = [0, 0, 1, 3, 12]
    move_zeroes_to_front(nums7)
    print(f"Test 7: {nums7 == expected7} - Expected: {expected7}, Got: {nums7}")
    
    # 测试用例8: 没有零
    nums8 = [1, 2, 3, 4, 5]
    expected8 = [1, 2, 3, 4, 5]
    move_zeroes_to_front(nums8)
    print(f"Test 8: {nums8 == expected8} - Expected: {expected8}, Got: {nums8}")
    
    # 测试用例9: 零在前面
    nums9 = [0, 0, 3, 4, 5]
    expected9 = [0, 0, 3, 4, 5]
    move_zeroes_to_front(nums9)
    print(f"Test 9: {nums9 == expected9} - Expected: {expected9}, Got: {nums9}")


if __name__ == "__main__":
    test_move_zeroes_to_front()
