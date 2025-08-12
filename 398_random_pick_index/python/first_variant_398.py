import random
from typing import List


# 蓄水池采样的核心思想是：每个元素被选入蓄水池的概率都是 k/n，n 是当前已处理元素的总数。
# 所以每次新元素到来时，要以 k/n 的概率决定是否把它放进蓄水池（并随机替换掉蓄水池中的一个元素）。

def random_pick_indices_first_variant_398(nums: List[int], k: int) -> List[int]:
    """
    蓄水池采样：从nums中随机采样k个数（不放回，相等概率）
    """
    if k > len(nums):
        raise ValueError("k不能大于数组长度")
    result = nums[:k]
    for i in range(k, len(nums)):
        n = i + 1
        r = random.randint(0, n - 1)
        if r < k:
            result[r] = nums[i]
    return result

# 测试函数
def test_reservoir_sampling():
    nums = list(range(100))
    k = 10
    samples = [random_pick_indices_first_variant_398(nums, k) for _ in range(5)]
    for i, sample in enumerate(samples, 1):
        print(f"第{i}次采样: {sample}")
    # 检查采样结果长度
    assert all(len(sample) == k for sample in samples)
    print("所有采样长度正确，采样算法运行正常！")

# VARIANT: 用蓄水池采样随机返回最大值的一个下标

def random_pick_index_second_variant_398(nums):
    max_number = float('-inf')
    picked_index = -1
    n = 0
    for i, curr_num in enumerate(nums):
        if curr_num < max_number:
            continue
        if curr_num > max_number:
            max_number = curr_num
            picked_index = i
            n = 1
        elif curr_num == max_number:
            n += 1
            r = random.randint(0, n - 1)
            if r == 0:
                picked_index = i
    return picked_index

if __name__ == "__main__":
    test_reservoir_sampling() 