# 找 list 中加起來最大的 pair, 兩個數字不能靠在一起
# = Example 1 =
# Input: [1, 2, 3, 4, 5]

# Output: 8

# = Example 2 =
# Input: [4, 1, 2, 3, 5]
# Output: 9

# [5, 4, 3, 2, 1]

def maxNoneAjacentPair(nums):
    res = float('-inf')
    n = len(nums)
    for i in range(n):
        # 寻找 i+2 及以后的最大元素
        for j in range(i+2, n):
            current = nums[i] + nums[j]
            if current > max_sum:
                max_sum = current
    return max_sum if max_sum != -float('inf') else 0  # 处理不足两个元素的情况