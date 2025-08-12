import random
from typing import List, Any, Dict
from collections import defaultdict

class ReservoirSamplingVariants:
    """蓄水池采样的各种变体实现"""
    
    @staticmethod
    def sample_one_element(nums: List[Any]) -> Any:
        """
        变体1：采样一个元素（k=1的蓄水池采样）
        时间复杂度：O(n)
        """
        if not nums:
            raise ValueError("数组不能为空")
        
        sample = nums[0]
        for i in range(1, len(nums)):
            # 以 1/(i+1) 的概率替换当前样本
            if random.randint(0, i) == 0:
                sample = nums[i]
        return sample
    
    @staticmethod
    def sample_one_index(nums: List[Any]) -> int:
        """
        变体2：采样一个索引（而不是元素值）
        时间复杂度：O(n)
        """
        if not nums:
            raise ValueError("数组不能为空")
        
        sample_index = 0
        for i in range(1, len(nums)):
            # 以 1/(i+1) 的概率替换当前索引
            if random.randint(0, i) == 0:
                sample_index = i
        return sample_index
    
    @staticmethod
    def sample_k_elements(nums: List[Any], k: int) -> List[Any]:
        """
        变体3：采样k个元素（标准蓄水池采样）
        时间复杂度：O(n)
        """
        if k > len(nums):
            raise ValueError("k不能大于数组长度")
        
        reservoir = nums[:k]
        for i in range(k, len(nums)):
            # 以 k/(i+1) 的概率替换蓄水池中的某个元素
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = nums[i]
        return reservoir
    
    @staticmethod
    def sample_k_indices(nums: List[Any], k: int) -> List[int]:
        """
        变体4：采样k个索引
        时间复杂度：O(n)
        """
        if k > len(nums):
            raise ValueError("k不能大于数组长度")
        
        reservoir_indices = list(range(k))
        for i in range(k, len(nums)):
            j = random.randint(0, i)
            if j < k:
                reservoir_indices[j] = i
        return reservoir_indices
    
    @staticmethod
    def weighted_reservoir_sampling(nums: List[Any], weights: List[float], k: int) -> List[Any]:
        """
        变体5：加权蓄水池采样
        时间复杂度：O(n)
        """
        if len(nums) != len(weights):
            raise ValueError("数组和权重长度必须相同")
        if k > len(nums):
            raise ValueError("k不能大于数组长度")
        
        reservoir = nums[:k]
        reservoir_weights = weights[:k]
        
        for i in range(k, len(nums)):
            # 计算当前元素的权重
            current_weight = weights[i]
            total_weight = sum(reservoir_weights) + current_weight
            
            # 以 current_weight/total_weight 的概率替换
            if random.random() < current_weight / total_weight:
                # 随机选择一个位置替换
                replace_idx = random.randint(0, k - 1)
                reservoir[replace_idx] = nums[i]
                reservoir_weights[replace_idx] = current_weight
        
        return reservoir
    
    @staticmethod
    def stream_reservoir_sampling(stream, k: int) -> List[Any]:
        """
        变体6：流式蓄水池采样（适用于数据流）
        时间复杂度：O(n)
        """
        reservoir = []
        count = 0
        
        for item in stream:
            count += 1
            if len(reservoir) < k:
                reservoir.append(item)
            else:
                # 以 k/count 的概率替换
                j = random.randint(0, count - 1)
                if j < k:
                    reservoir[j] = item
        
        return reservoir

# 测试函数
def test_reservoir_variants():
    """测试各种蓄水池采样变体"""
    nums = list(range(1, 11))  # [1, 2, 3, ..., 10]
    
    print("=== 蓄水池采样变体测试 ===")
    
    # 测试1：采样一个元素
    print("\n1. 采样一个元素:")
    for _ in range(5):
        result = ReservoirSamplingVariants.sample_one_element(nums)
        print(f"  采样结果: {result}")
    
    # 测试2：采样一个索引
    print("\n2. 采样一个索引:")
    for _ in range(5):
        index = ReservoirSamplingVariants.sample_one_index(nums)
        print(f"  采样索引: {index}, 对应元素: {nums[index]}")
    
    # 测试3：采样k个元素
    print("\n3. 采样3个元素:")
    for _ in range(3):
        result = ReservoirSamplingVariants.sample_k_elements(nums, 3)
        print(f"  采样结果: {result}")
    
    # 测试4：采样k个索引
    print("\n4. 采样3个索引:")
    for _ in range(3):
        indices = ReservoirSamplingVariants.sample_k_indices(nums, 3)
        elements = [nums[i] for i in indices]
        print(f"  采样索引: {indices}, 对应元素: {elements}")
    
    # 测试5：加权采样
    print("\n5. 加权采样（权重越大越容易被选中）:")
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 权重递增
    for _ in range(3):
        result = ReservoirSamplingVariants.weighted_reservoir_sampling(nums, weights, 3)
        print(f"  加权采样结果: {result}")
    
    # 测试6：流式采样
    print("\n6. 流式采样:")
    def number_stream():
        for i in range(1, 11):
            yield i
    
    result = ReservoirSamplingVariants.stream_reservoir_sampling(number_stream(), 3)
    print(f"  流式采样结果: {result}")

# 概率分布测试
def test_probability_distribution():
    """测试采样概率分布"""
    print("\n=== 概率分布测试 ===")
    
    nums = [1, 2, 3, 4, 5]
    n_samples = 10000
    counts = defaultdict(int)
    
    # 测试采样一个元素的概率分布
    for _ in range(n_samples):
        result = ReservoirSamplingVariants.sample_one_element(nums)
        counts[result] += 1
    
    print("采样一个元素的概率分布:")
    for num in nums:
        probability = counts[num] / n_samples
        expected = 1 / len(nums)
        print(f"  元素 {num}: {probability:.4f} (期望: {expected:.4f})")

if __name__ == "__main__":
    test_reservoir_variants()
    test_probability_distribution() 