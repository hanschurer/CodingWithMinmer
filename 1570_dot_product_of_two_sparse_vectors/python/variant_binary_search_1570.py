from collections import namedtuple
from bisect import bisect_left

#如果给定的两个vector相差很大，
class SparseVector:
    def __init__(self, nums: List[int]):
        # 存储非零元素的(索引, 值)对，按索引自然排序
        self.non_zero = []
        for idx, val in enumerate(nums):
            if val != 0:
                self.non_zero.append((idx, val))
        

    # 用二分查找优化点积计算
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        # 区分非零元素较少和较多的列表
        short, long = (self.non_zero, vec.non_zero) if len(self.non_zero) < len(vec.non_zero) else (vec.non_zero, self.non_zero)
        
        # 遍历较短列表，在较长列表中二分查找相同索引
        for idx, val in short:
            # 二分查找较长列表中索引等于idx的位置
            pos = bisect_left(long, (idx,))  # 利用元组比较，按索引查找
            # 检查是否找到匹配的索引
            if pos < len(long) and long[pos][0] == idx:
                res += val * long[pos][1]
        
        return res
