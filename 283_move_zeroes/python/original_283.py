from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    将数组中的所有0移动到末尾，同时保持非零元素的相对顺序
    
    Args:
        nums: 输入数组，将被原地修改
        
    Example:
        >>> nums = [0,1,0,3,12]
        >>> moveZeroes(nums)
        >>> print(nums)
        [1, 3, 12, 0, 0]
    """
    if not nums:
        return
    
    # 双指针技术：swap_index指向下一个非零元素应该放置的位置
    swap_index = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            # 交换当前非零元素到swap_index位置
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index += 1


# 测试代码
def test_move_zeroes():
    # 测试用例1: 基本功能
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    moveZeroes(nums1)
    print(f"Test 1: {nums1 == expected1} - Expected: {expected1}, Got: {nums1}")
    
    # 测试用例2: 没有零
    nums2 = [1, 2, 3, 4, 5]
    expected2 = [1, 2, 3, 4, 5]
    moveZeroes(nums2)
    print(f"Test 2: {nums2 == expected2} - Expected: {expected2}, Got: {nums2}")
    
    # 测试用例3: 全是零
    nums3 = [0, 0, 0, 0]
    expected3 = [0, 0, 0, 0]
    moveZeroes(nums3)
    print(f"Test 3: {nums3 == expected3} - Expected: {expected3}, Got: {nums3}")
    
    # 测试用例4: 空数组
    nums4 = []
    expected4 = []
    moveZeroes(nums4)
    print(f"Test 4: {nums4 == expected4} - Expected: {expected4}, Got: {nums4}")
    
    # 测试用例5: 只有一个元素
    nums5 = [0]
    expected5 = [0]
    moveZeroes(nums5)
    print(f"Test 5: {nums5 == expected5} - Expected: {expected5}, Got: {nums5}")
    
    nums6 = [1]
    expected6 = [1]
    moveZeroes(nums6)
    print(f"Test 6: {nums6 == expected6} - Expected: {expected6}, Got: {nums6}")


if __name__ == "__main__":
    test_move_zeroes()
