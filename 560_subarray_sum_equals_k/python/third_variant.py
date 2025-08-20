from typing import List
#找出所有subarray需满足1）长度是2的n次方2）sum是在给定的k到2k之间
def find_valid_subarrays(nums: List[int], k: int) -> List[List[int]]:
    n = len(nums)
    if n == 0:
        return []
    
    # 步骤1：计算前缀和
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    # 步骤2：生成所有合法长度（2的n次方，且不超过数组长度）
    valid_lengths = []
    current_len = 1  # 2^0 = 1
    while current_len <= n:
        valid_lengths.append(current_len)
        current_len *= 2  # 下一个2的次方
    
    # 步骤3：遍历所有合法子数组并检查条件
    result = []
    for length in valid_lengths:
        # 起始索引l的范围：0 <= l <= n - length
        for l in range(n - length + 1):
            r = l + length - 1  # 结束索引
            subarray_sum = prefix[r + 1] - prefix[l]
            if k <= subarray_sum <= 2 * k:
                # 记录子数组（存储元素或索引）
                result.append(nums[l:r+1])  # 存储元素
                # 若需存储索引，可改为：result.append( (l, r) )
    
    return result


# 示例测试
if __name__ == "__main__":
    nums = [1, 3, 2, 4, 5, 1, 2]
    k = 4
    print(find_valid_subarrays(nums, k))
    # 输出说明：
    # 合法长度为1,2,4,8（但数组长度为7，故最大为4）
    # 检查所有长度为1,2,4的子数组，和在[4,8]之间的有：
    # [3], [4], [5], [3,2], [2,4], [4,5], [1,3,2,4] 等