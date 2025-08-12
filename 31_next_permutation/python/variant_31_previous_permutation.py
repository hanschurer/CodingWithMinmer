
#find previous permutation

class Solution:
    def previousPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        def findNextBig():
            for i in range(n-2, -1, -1):
                if nums[i] > nums[i+1]:
                    return i
            return -1
        def findJustSmall(i):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]:
                    return j
            return i
        def reverse(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        i = findNextBig()
        if i != -1:
            j = findJustSmall(i)
            nums[i], nums[j] = nums[j], nums[i]
        reverse(i+1, n-1)
        return nums

if __name__ == "__main__":
    # Basic cases
    solution = Solution()
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 3, 5]
    nums = [3, 2, 1]
    solution.previousPermutation(nums)
    assert nums == [3, 1, 2]
    nums = [1, 2, 3]
    solution.previousPermutation(nums)
    assert nums == [3, 2, 1]
    nums = [9, 6, 5, 4, 3, 2]
    solution.previousPermutation(nums)
    assert nums == [9, 6, 5, 4, 2, 3]
    nums = [4, 5, 1, 1, 3, 7]
    solution.previousPermutation(nums)
    assert nums == [4, 3, 7, 5, 1, 1]
    nums = [1, 5, 8, 5, 1, 3, 4, 6, 7]
    solution.previousPermutation(nums)
    assert nums == [1, 5, 8, 4, 7, 6, 5, 3, 1]
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]

    # Single digit case
    nums = [5]
    solution.previousPermutation(nums)
    assert nums == [5]

    # Duplicate digits case
    nums = [1, 1, 1]
    solution.previousPermutation(nums)
    assert nums == [1, 1, 1]

    # Already smallest case (loops around)
    nums = [1, 2, 3, 4, 5, 6]
    solution.previousPermutation(nums)
    assert nums == [6, 5, 4, 3, 2, 1]
