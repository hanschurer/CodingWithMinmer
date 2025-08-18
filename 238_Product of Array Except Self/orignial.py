class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = suf = 1
        res = [1] * n

        for i in range(n):
            res[i]*=pre
            pre *= nums[i]
        
        for i in range(n-1, -1, -1):
            res[i]*=suf
            suf*=nums[i]
        return res